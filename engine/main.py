"""
main.py

This module serves as the entry point for the Insight Engine application.
It sets up the Streamlit interface, handles file uploads, and orchestrates
the document processing, embedding, and question-answering pipeline.

The main features include:
- File upload for PDF, DOCX, and TXT documents
- Document parsing and indexing
- Question-answering based on the uploaded document
- Display of answers and sources

Dependencies:
- streamlit
- langchain
- langchain_community
- engine.components.sidebar
- engine.utils
"""

import streamlit as st
from typing import Optional

from engine.components.sidebar import sidebar
from engine.utils import (
    embed_docs,
    get_answer,
    get_sources,
    parse_docx,
    parse_pdf,
    parse_txt,
    search_docs,
    text_to_docs,
    wrap_text_in_html,
)

PAGE_TITLE = "Insight Engine"
PAGE_ICON = "📖"
SUPPORTED_FILE_TYPES = ["pdf", "docx", "txt"]


def setup_page():
    """
    Set up the Streamlit page configuration.

    This function configures the page title, icon, and layout.
    It also hides the default Streamlit menu and footer.
    """
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")
    st.header(f"{PAGE_ICON}{PAGE_TITLE}")

    hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
    st.markdown(hide_default_format, unsafe_allow_html=True)


def parse_document(uploaded_file) -> Optional[str]:
    """
    Parse the uploaded document based on its file type.

    Args:
        uploaded_file: The uploaded file object from Streamlit's file_uploader.

    Returns:
        Optional[str]: The parsed content of the document, or None if parsing fails.
    """
    if uploaded_file.name.endswith(".pdf"):
        return parse_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return parse_docx(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        return parse_txt(uploaded_file)
    else:
        st.error("File type not supported!")
        return None


def clear_submit() -> None:
    """
    Clear the submit state in the session state.

    This function is used as a callback when the file uploader or query input changes,
    ensuring that the submit button state is reset.
    """
    st.session_state["submit"] = False


def main() -> None:
    """
    Main function to run the Insight Engine application.

    This function sets up the Streamlit interface, handles file uploads,
    processes documents, and manages the question-answering flow.
    """
    setup_page()
    sidebar()

    uploaded_file = st.file_uploader(
        "Upload a pdf, docx, or txt file",
        type=SUPPORTED_FILE_TYPES,
        help="Scanned documents are not supported yet!",
        on_change=clear_submit,
    )

    index = None
    doc = None
    if uploaded_file:
        doc = parse_document(uploaded_file)
        if doc:
            text = text_to_docs(doc)
            try:
                with st.spinner("Indexing document... This may take a while⏳"):
                    index = embed_docs(text)
            except Exception as e:
                st.error(str(e))

    query = st.text_area("Ask a question about the document", on_change=clear_submit)
    with st.expander("Advanced Options"):
        show_all_chunks = st.checkbox("Show all chunks retrieved from vector search")
        show_full_doc = st.checkbox("Show parsed contents of the document")

    if show_full_doc and doc:
        with st.expander("Document"):
            # Hack to get around st.markdown rendering LaTeX
            st.markdown(f"<p>{wrap_text_in_html(doc)}</p>", unsafe_allow_html=True)

    button = st.button("Submit")
    if button or st.session_state.get("submit"):
        if not index:
            st.error("Please upload a document!")
        elif not query:
            st.error("Please enter a question!")
        else:
            st.session_state["submit"] = True
            # Output Columns
            answer_col, sources_col = st.columns(2)
            sources = search_docs(index, query)

            try:
                answer = get_answer(sources, query)
                if not show_all_chunks:
                    # Get the sources for the answer
                    sources = get_sources(answer, sources)

                with answer_col:
                    st.markdown("#### Answer")
                    st.markdown(answer["output_text"].split("SOURCES: ")[0])

                with sources_col:
                    st.markdown("#### Sources")
                    for source in sources:
                        st.markdown(source.page_content)
                        st.markdown(source.metadata["source"])
                        st.markdown("---")

            except Exception as e:
                st.error(e._message)


if __name__ == "__main__":
    main()