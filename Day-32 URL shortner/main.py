import streamlit as st
import pyshorteners
import webbrowser

st.set_page_config(page_title="URL Shortener", page_icon="🔗")
st.title("🔗 URL Shortener")
st.write("Enter a long URL and get a short one!")

# Input
long_url = st.text_input("Paste your long URL here")

if long_url:
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        st.success(f"Shortened URL: {short_url}")
        
        # Buttons
        col1, col2 = st.columns(2)
        with col1:
            st.button("Open Short URL", on_click=lambda: webbrowser.open(short_url))
        with col2:
            st.code(short_url, language='text')

    except Exception as e:
        st.error(f"❌ Error: {e}")
