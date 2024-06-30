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
## How does Insight Engine work its magic? 🎩✨
Picture this: Your document gets chopped up like a salad, tossed into a 
fancy vector index (it's like a library, but cooler), and served up on demand. 
When you ask a question, our digital bloodhound sniffs out the juiciest bits 
and feeds them to LLAMA3:8b (no, not a real llama, sadly). This AI then spits 
out an answer faster than you can say "semantic search"!

---

## Is my data going to run away and join the circus? 🎪
Nope! Your data is like a Vegas vacation - what happens here, stays here. 
Once you close the tab, poof! It's gone. Insight Engine is not data hoarders, it's more
more like... data one-night stands.

---

## What's with the numbers under the sources? Are you secretly teaching me math? 🔢
For PDFs, you'll see something like 3-12. It's not a Bible verse, promise! 
The first number is the page, the second is the chunk on that page. For DOCS 
and TXT, we're lazy, so the first number is always 1. It's like page numbers 
for ants!

---

## Are the answers 100% accurate, or should I take them with a grain of salt? 🧂
Let's be real - LLAMA3:8b is smart, but it's not your know-it-all cousin at 
Thanksgiving dinner. It makes mistakes, hallucinates (the AI kind, not the fun kind), 
and sometimes misses the point entirely. It's like a really smart parrot with 
occasional brain farts.

Insight Engine uses semantic search, which is fancy talk for "it looks for 
similar stuff." It doesn't read the whole document, so it might miss some 
context. For summary questions, it's like asking someone to recap a movie 
they've only seen the trailer for.

But hey, for most questions, it's pretty spot on! Just remember to double-check 
with the sources. Trust, but verify - it's not just for international diplomacy anymore!

---

## Can Insight Engine do my homework for me? 📚
Nice try, kiddo! While Insight Engine can help you understand your documents 
better, it's not a magic homework machine. Think of it as a really smart study 
buddy, not a cheat code for life. Your teacher will still know if you try to 
pass off AI-generated answers as your own. Stay in school!

---

## What if I ask Insight Engine the meaning of life? 🤔
Well, that's a deep one! Insight Engine might give you a philosophical answer 
based on the documents you've uploaded, but for the real meaning of life, 
you're better off asking a magic 8-ball or your local fortune cookie. Or, you 
know, figure it out the old-fashioned way - through years of existential crises!

"""
    )
