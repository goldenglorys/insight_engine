"""
embeddings.py

This module provides a wrapper around Sentence Transformer embedding models.
It implements the Embeddings interface from LangChain, allowing it to be used
interchangeably with other embedding classes.

The main class, SentenceTransformerEmbeddings, offers methods to generate
embeddings for both individual queries and lists of documents.

Dependencies:
- sentence_transformers
- langchain
"""

from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings
from typing import List


class SentenceTransformerEmbeddings(Embeddings):
    """
    A class to generate embeddings using Sentence Transformers.

    This class implements the Embeddings interface from LangChain,
    allowing it to be used interchangeably with other embedding classes.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the SentenceTransformerEmbeddings.

        Args:
            model_name (str): The name of the Sentence Transformer model to use.
                              Defaults to "all-MiniLM-L6-v2".

        Raises:
            ValueError: If the specified model fails to load.
        """
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of documents.

        Args:
            texts (List[str]): A list of strings to embed.

        Returns:
            List[List[float]]: A list of embeddings, each embedding being 
            a list of floats.
        """
        embeddings = self.model.encode(texts)
        return embeddings.tolist()

    def embed_query(self, text: str) -> List[float]:
        """
        Generate an embedding for a single query string.

        Args:
            text (str): The query string to embed.

        Returns:
            List[float]: The embedding as a list of floats.
        """
        embedding = self.model.encode([text])[0]
        return embedding.tolist()
