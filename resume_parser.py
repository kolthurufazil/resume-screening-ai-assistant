import spacy
import PyPDF2

# Load SpaCy's small English NLP model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

# Function to extract skills and education
def extract_entities(text):
    # 🔹 Predefined skill keywords (expand as needed)
    skill_keywords = [
        "python", "java", "sql", "c++", "tensorflow", "pytorch", "keras", "opencv",
        "docker", "linux", "git", "scikit-learn", "machine learning", "deep learning",
        "nlp", "computer vision", "data preprocessing", "time series", "mysql", "jupyter"
    ]

    # Normalize text for keyword matching
    text_lower = text.lower()

    # Find skills present in the text
    found_skills = [skill for skill in skill_keywords if skill in text_lower]

    # Extract education entities using SpaCy
    doc = nlp(text)
    education = [
        ent.text.strip()
        for ent in doc.ents
        if ent.label_ == "ORG" and "university" in ent.text.lower()
    ]

    return list(set(found_skills)), list(set(education))

# Main
if __name__ == "__main__":
    resume_text = extract_text_from_pdf("example_resume.pdf")
    print("Extracted Text (preview):\n", resume_text[:1000])  # Print a preview

    skills, education = extract_entities(resume_text)
    print("\nSkills:", skills)
    print("Education:", education)
