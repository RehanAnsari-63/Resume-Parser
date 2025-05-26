

````markdown
# Resume Parser

A Python-based Resume Parser with multiple interfaces:
- Local GUI (Tkinter)
- Web GUI (Streamlit)
- REST API (FastAPI)

Extracts text and key info (name, email, phone) from PDF resumes for HR automation.

---

## Features

- Parse PDF resumes to extract raw text.
- GUI app with Tkinter for local use.
- Streamlit app for clean, web-based UI.
- FastAPI backend with file upload and JSON output.
- Basic NLP extraction of emails, phone numbers, and candidate names.
- Easy to run locally or deploy on a server.
- Download parsed text as `.txt`.

---

## Installation

Clone the repo:

```bash
git clone https://github.com/yourusername/resume_parser.git
cd resume_parser
````

Create and activate a Python virtual environment (recommended):

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/macOS
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Local GUI (Tkinter)

```bash
python gui_resume_parser.py
```

### 2. Streamlit Web App

```bash
streamlit run streamlit_resume_parser.py
```

Open your browser at `http://localhost:8501`

### 3. FastAPI Backend

```bash
uvicorn app:app --reload
```

Open interactive docs at `http://127.0.0.1:8000/docs`

Upload PDF via `/upload/` endpoint to parse text.

---

## Code Snippet: Extract Emails, Phones, Names (NLP)

```python
import re

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
```

---

## Tech Stack

* Python 3.x
* PyMuPDF (fitz) for PDF text extraction
* Tkinter for desktop GUI
* Streamlit for web UI
* FastAPI + Uvicorn for REST API

---

## Contributing

Feel free to submit issues or pull requests to improve the parser or add features.

---

## License

[MIT License](LICENSE)

---

