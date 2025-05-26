import fitz  # PyMuPDF
import streamlit as st
import re

st.title("📄 Resume PDF Parser")

uploaded_file = st.file_uploader("Upload a Resume PDF", type="pdf")

if uploaded_file:
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    st.subheader("🔍 Extracted Text:")
    st.text_area("Text from PDF", text, height=300)

    if st.download_button("Download as .txt", text, file_name="resume_text.txt"):
        st.success("Downloaded successfully.")




def extract_email(text):
    return re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

def extract_phone(text):
    return re.findall(r"\+?\d[\d -]{8,}\d", text)

def extract_name(text):
    lines = text.split('\n')
    for line in lines:
        if line.strip() and len(line.strip().split()) <= 3:
            return line.strip()
    return "Unknown"
