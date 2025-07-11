# import streamlit
import streamlit as st
from main import get_score, get_missingwords

st.set_page_config(page_title="AI Resume Matcher",page_icon="🧠")
st.title("🧠 AI-Powered Resume Matcher")
st.markdown("Match your resume against any job description and discover missing skills instantly.")
st.header("📄 Upload Your Resume")
uploaded_file=st.file_uploader("Drag or Drop the Resume File:",type=["pdf","txt"],accept_multiple_files=False)
st.subheader("📋 Paste Job Description")
jd_string=st.text_area("Paste the Job Description Below and Click Ctrl+Enter to Submit:")
resume_string=""
if uploaded_file is not None:
    if uploaded_file.type=="application/pdf":
        import fitz
        #open the pdf file
        pdf_doc=fitz.open(stream=uploaded_file,filetype="pdf")
        for page in pdf_doc:
            resume_string+=page.get_text()
    elif uploaded_file.type=="text/plain":
        resume_string=uploaded_file.read().decode("utf-8")

if resume_string.strip() and jd_string.strip():
    score=get_score(resume_string,jd_string)
    missing=get_missingwords(resume_string,jd_string)
    st.success(f"✅ Resume Match Score: **{score}**")
    if (missing):
        st.write("Missing Technical Skills are:")
        st.text(f"{missing.upper()}")
    else:
        st.success("Hurrah,No Technical Skills are missing")  
