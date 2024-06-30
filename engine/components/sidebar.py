import streamlit as st

from engine.components.faq import faq


def sidebar():
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
