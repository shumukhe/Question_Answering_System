import streamlit as st
from utils import get_answer

st.set_page_config(page_title="Question Answering System 🤖")

st.title("Ask Your Questions Here 🤖")

# 🔁 1. Context first with larger box
context = st.text_area("Enter the context passage:", height=300)

# 🔁 2. Question next
question = st.text_input("Enter your question:")

# 🔁 3. Answer generation
if st.button("Get Answer"):
    if question and context:
        answer = get_answer(question, context)
        st.success(f"**Answer:** {answer}")
    else:
        st.warning("Please enter both question and context.")