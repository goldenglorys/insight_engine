"""
sidebar.py

This module defines the sidebar component for the Insight Engine Streamlit application.
It includes functionality for displaying the sidebar, handling API key input, and showing FAQ.

Dependencies:
- streamlit
- engine.components.faq
"""

import streamlit as st

from engine.components.faq import faq


def sidebar() -> None:
    """
    Display and handle the sidebar for the Insight Engine application.

    This function sets up the sidebar, including:
    - API key input
    - FAQ display
    - Application information
    """
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Upload a pdf, docx, or txt file📄 (Currently we don't support scanned PDF)\n"
            "2. Ask a question about the document💬\n"
            "   Or you can ask Insight  Engine to give you some questions about the document💬\n"
        )
        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖Insight Engine allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
            "You can use it to research a paper or practice your exam. "
        )
        st.markdown("This tool is a work in progress. ")

        faq()
