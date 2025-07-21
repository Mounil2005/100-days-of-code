import streamlit as st
from utils.python import check_python_syntax
from utils.c import check_c_syntax

st.title("🧠 Syntax Checker")

language = st.selectbox("Select Language", ["Python", "C"])
code = st.text_area("Enter your code here", height=300)

if st.button("Check Syntax"):
    if language == "Python":
        result, _ = check_python_syntax(code)
        st.info(result)
    else:
        result = check_c_syntax(code)
        st.info(result)
