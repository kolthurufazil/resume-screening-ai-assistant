import streamlit as st
from resume_parser import extract_text_from_pdf, extract_entities
from job_matcher import load_job_description, extract_skills_from_text, match_skills

# Predefined skill list (same as in other files)
skill_keywords = [
    "python", "java", "sql", "c++", "tensorflow", "pytorch", "keras", "opencv",
    "docker", "linux", "git", "scikit-learn", "machine learning", "deep learning",
    "nlp", "computer vision", "data preprocessing", "time series", "mysql", "jupyter"
]

st.set_page_config(page_title="Resume Screening AI Assistant", layout="centered")

st.title("🧠 Resume Screening AI Assistant")
st.markdown("Upload your resume and paste a job description to get a skill match score!")

# Upload resume
resume_file = st.file_uploader("📄 Upload Resume (PDF only)", type=["pdf"])

# Job Description
job_desc = st.text_area("📝 Paste Job Description Here", height=200)

if st.button("Analyze"):
    if resume_file and job_desc.strip():
        with st.spinner("Extracting and matching..."):
            # Save uploaded file temporarily
            with open("uploaded_resume.pdf", "wb") as f:
                f.write(resume_file.read())

            resume_text = extract_text_from_pdf("uploaded_resume.pdf")
            resume_skills, education = extract_entities(resume_text)

            jd_skills = extract_skills_from_text(job_desc.lower(), skill_keywords)

            matched, missing, score = match_skills(resume_skills, jd_skills)

        st.success(f" Match Score: {score}%")
        st.markdown(f"** Matched Skills:** {', '.join(matched) if matched else 'None'}")
        st.markdown(f"** Missing Skills:** {', '.join(missing) if missing else 'None'}")
        st.markdown(f"** Education Mentioned:** {', '.join(education) if education else 'Not found'}")
    else:
        st.warning("Please upload a resume and paste a job description.")
