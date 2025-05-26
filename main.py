import fitz  # PyMuPDF
import re
import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3}[-.\s]?)?\(?\d{3,4}\)?[-.\s]?\d{3}[-.\s]?\d{3,4}', text)
    return match.group(0) if match else None

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text, skill_set):
    found = []
    for skill in skill_set:
        if skill.lower() in text.lower():
            found.append(skill)
    return list(set(found))

# Predefined skill list
skills_db = ["Python", "Java", "Excel", "SQL", "Recruitment", "Machine Learning", "Data Analysis"]

if __name__ == "__main__":
    resume_file = "Rehan_Ansari_DS_CV.pdf"
    text = extract_text_from_pdf(resume_file)

    data = {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text, skills_db)
    }

    df = pd.DataFrame([data])
    df.to_csv("output.csv", index=False)
    print("Extraction complete. Saved to output.csv")
