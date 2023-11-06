import streamlit as st
from langchain_helper import summarizeYTVideo

st.title("YouTube Video Summarizer")

url = st.text_input("Video URL: ")

if url:
    summary, title, author, lengthOfVideo = summarizeYTVideo(url)
    st.subheader(f"Title: {title}")
    st.subheader(f"Author: {author}")
    st.subheader(f"Length: {round(lengthOfVideo//60)} mins")
    st.divider()

    st.header("Summary: ")
    st.write(summary)