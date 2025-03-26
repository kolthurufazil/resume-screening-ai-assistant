def load_job_description(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().lower()

def extract_skills_from_text(text, skill_keywords):
    return list(set([skill for skill in skill_keywords if skill in text]))

def match_skills(resume_skills, jd_skills):
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    score = round((len(matched) / len(jd_skills)) * 100, 2) if jd_skills else 0
    return matched, missing, score

if __name__ == "__main__":
    # Sample skill list (keep same as resume_parser.py)
    skill_keywords = [
        "python", "java", "sql", "c++", "tensorflow", "pytorch", "keras", "opencv",
        "docker", "linux", "git", "scikit-learn", "machine learning", "deep learning",
        "nlp", "computer vision", "data preprocessing", "time series", "mysql", "jupyter"
    ]

    from resume_parser import extract_text_from_pdf, extract_entities

    resume_text = extract_text_from_pdf("example_resume.pdf")
    resume_skills, _ = extract_entities(resume_text)

    jd_text = load_job_description("job_description.txt")
    jd_skills = extract_skills_from_text(jd_text, skill_keywords)

    matched, missing, score = match_skills(resume_skills, jd_skills)

    print("\n Matched Skills:", matched)
    print(" Missing Skills:", missing)
    print(f"\n Match Score: {score}%")
