"""
prompts.py

This module defines the prompt templates used in the Insight Engine application.
It contains a template for generating answers based on provided document excerpts.

The main components are:
- A template string for answer generation
- A PromptTemplate object (STUFF_PROMPT) that can be used with LangChain

Dependencies:
- langchain
"""

from langchain.prompts import PromptTemplate

## Need to use a shorter template to shorten the number of tokens in the prompt..
template = """Create a final answer to the given questions using the provided document excerpts(in no particular order) as references. ALWAYS include a "SOURCES" section in your answer including only the minimal set of sources needed to answer the question. If you are unable to answer the question, simply state that you do not know. Do not attempt to fabricate an answer and leave the SOURCES section empty.

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
