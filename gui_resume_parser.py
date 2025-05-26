from fastapi import FastAPI, File, UploadFile
import fitz
import re

app = FastAPI()

# --- Extraction Functions ---
def extract_email(text):
    return re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

def extract_phone(text):
    return re.findall(r"\+?\d[\d\s\-()]{8,}", text)

def extract_name(text):
    lines = text.split('\n')
    for line in lines:
        if line.strip() and len(line.strip().split()) <= 3:
            return line.strip()
    return "Unknown"

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files allowed."}

    contents = await file.read()
    try:
        doc = fitz.open(stream=contents, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()

        return {
            "filename": file.filename,
            "name": extract_name(text),
            "email": extract_email(text),
            "phone": extract_phone(text),
            "text_preview": text[:2000]
        }
    except Exception as e:
        return {"error": str(e)}
