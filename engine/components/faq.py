"""
faq.py

This module contains the FAQ (Frequently Asked Questions) for the Insight Engine application.
It provides a function to display the FAQ in the Streamlit sidebar.

Dependencies:
- streamlit
"""

import streamlit as st


def faq() -> None:
    """
    Display the FAQ (Frequently Asked Questions) in the Streamlit sidebar.

    This function creates an expander in the sidebar and populates it with
    common questions and answers about the Insight Engine application.
    """
    st.markdown(
        """
# FAQ
## How does Insight Engine work?
When you upload a document, it will be divided into smaller chunks 
and stored in a special type of database called a vector index 
that allows for semantic search and retrieval.

When you ask a question, Insight Engine will search through the
document chunks and find the most relevant ones using the vector index.
Then, it will use LLAMA3:8b to generate a final answer.

## Is my data safe?
Yes, your data is safe. Insight Engine does not store your documents or
questions. All uploaded data is deleted after you close the browser tab.

## What do the numbers mean under each source?
For a PDF document, you will see a citation number like this: 3-12. 
The first number is the page number and the second number is 
the chunk number on that page. For DOCS and TXT documents, 
the first number is set to 1 and the second number is the chunk number.

## Are the answers 100% accurate?
No, the answers are not 100% accurate. Insight Engine uses LLAMA3:8b to generate
answers. LLAMA3:8b is a powerful language model, but it sometimes makes mistakes 
and is prone to hallucinations. Also, Insight Engine uses semantic search
to find the most relevant chunks and does not see the entire document,
which means that it may not be able to find all the relevant information and
may not be able to answer all questions (especially summary-type questions
or questions that require a lot of context from the document).

But for most use cases, Insight Engine is very accurate and can answer
most questions. Always check with the sources to make sure that the answers
are correct.
"""
    )
