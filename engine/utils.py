"""
utils.py

This module contains utility functions for the Insight Engine application.
It provides functionality for parsing different document types, text processing,
document embedding, and question-answering.

The main features include:
- Parsing PDF, DOCX, and TXT files
- Converting text to document objects
- Embedding documents using FAISS
- Searching similar documents
- Generating answers to questions using a language model

Dependencies:
- streamlit
- docx2txt
- pypdf
- langchain
- langchain_community
- sentence_transformers
"""

import re
from io import BytesIO
from typing import Any, Dict, List, Union

import docx2txt
import streamlit as st
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import VectorStore
from langchain_community.vectorstores import FAISS
from pypdf import PdfReader

from langchain_community.chat_models.ollama import ChatOllama

from engine.embeddings import SentenceTransformerEmbeddings
from engine.prompts import STUFF_PROMPT


@st.cache_data
def parse_docx(file: BytesIO) -> str:
    """
    Parse a .docx file and return its content as a string.

    Args:
        file (BytesIO): The .docx file as a BytesIO object.

    Returns:
        str: The parsed content of the .docx file.
    """
    text = docx2txt.process(file)
    # Remove multiple newlines
    return re.sub(r"\n\s*\n", "\n\n", text)


@st.cache_data
def parse_pdf(file: BytesIO) -> List[str]:
    """
    Parse a PDF file and return its content as a list of strings, one per page.

    Args:
        file (BytesIO): The PDF file as a BytesIO object.

    Returns:
        List[str]: A list of strings, each representing a page in the PDF.
    """
    pdf = PdfReader(file)
    output = []
    for page in pdf.pages:
        text = page.extract_text()
        # Merge hyphenated words
        text = re.sub(r"(\w+)-\n(\w+)", r"\1\2", text)
        # Fix newlines in the middle of sentences
        text = re.sub(r"(?<!\n\s)\n(?!\s\n)", " ", text.strip())
        # Remove multiple newlines
        text = re.sub(r"\n\s*\n", "\n\n", text)
        output.append(text)
    return output


@st.cache_data
def parse_txt(file: BytesIO) -> str:
    """
    Parse a .txt file and return its content as a string.

    Args:
        file (BytesIO): The .txt file as a BytesIO object.

    Returns:
        str: The parsed content of the .txt file with redundant newlines removed.
    """
    text = file.read().decode("utf-8")
    # Remove multiple newlines
    text = re.sub(r"\n\s*\n", "\n\n", text)
    return text


@st.cache_data
def text_to_docs(text: str | List[str]) -> List[Document]:
    """
    Converts a string or list of strings to a list of Documents with metadata.

    Args:
        text (Union[str, List[str]]): The input text, either as a single string or a list of strings.

    Returns:
        List[Document]: A list of Document objects, each representing a chunk of the input text.
    """
    if isinstance(text, str):
        # Take a single string as one page
        text = [text]
    page_docs = [Document(page_content=page) for page in text]
    # Add page numbers as metadata
    for i, doc in enumerate(page_docs):
        doc.metadata["page"] = i + 1
    # Split pages into chunks
    doc_chunks = []
    for doc in page_docs:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""],
            chunk_overlap=0,
        )
        chunks = text_splitter.split_text(doc.page_content)
        for i, chunk in enumerate(chunks):
            doc = Document(
                page_content=chunk, metadata={"page": doc.metadata["page"], "chunk": i}
            )
            # Add sources a metadata
            doc.metadata["source"] = f"{doc.metadata['page']}-{doc.metadata['chunk']}"
            doc_chunks.append(doc)
    return doc_chunks


def embed_docs(docs: List[Document]) -> VectorStore:
    """
    Embeds a list of Documents and returns a FAISS index.

    Args:
        docs (List[Document]): A list of Document objects to be embedded.

    Returns:
        VectorStore: A FAISS index containing the embedded documents.
    """
    # Embed the chunks
    embeddings = SentenceTransformerEmbeddings()
    index = FAISS.from_documents(docs, embeddings)

    return index


def search_docs(index: VectorStore, query: str) -> List[Document]:
    """
    Searches a FAISS index for similar chunks to the query and returns a list of Documents.

    Args:
        index (VectorStore): The FAISS index to search.
        query (str): The query string to search for.

    Returns:
        List[Document]: A list of similar Document objects.
    """
    # Search for similar chunks
    docs = index.similarity_search(query, k=5)
    return docs


def get_answer(docs: List[Document], query: str) -> Dict[str, Any]:
    """
    Gets an answer to a question from a list of Documents using a language model.

    Args:
        docs (List[Document]): A list of relevant Document objects.
        query (str): The question to be answered.

    Returns:
        Dict[str, Any]: A dictionary containing the answer and other relevant information.
    """
    chat_model = ChatOllama(model="llama3:8b")

    chain = load_qa_with_sources_chain(
        chat_model,
        chain_type="stuff",
        prompt=STUFF_PROMPT,
    )

    answer = chain.invoke(
        {"input_documents": docs, "question": query}, return_only_outputs=True
    )
    return answer


def get_sources(answer: Dict[str, Any], docs: List[Document]) -> List[Document]:
    """
    Gets the source documents for an answer.

    Args:
        answer (Dict[str, Any]): The answer dictionary returned by get_answer().
        docs (List[Document]): The list of all available Document objects.

    Returns:
        List[Document]: A list of Document objects that were used as sources for the answer.
    """
    source_keys = [s for s in answer["output_text"].split("SOURCES: ")[-1].split(", ")]

    source_docs = []
    for doc in docs:
        if doc.metadata["source"] in source_keys:
            source_docs.append(doc)

    return source_docs


def wrap_text_in_html(text: str | List[str]) -> str:
    """
    Wrap each text block separated by newlines in <p> tags.

    Args:
        text (Union[str, List[str]]): The text to wrap, either as a string or list of strings.

    Returns:
        str: The HTML-wrapped text.
    """
    if isinstance(text, list):
        # Add horizontal rules between pages
        text = "\n<hr/>\n".join(text)
    return "".join([f"<p>{line}</p>" for line in text.split("\n")])
