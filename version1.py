# Resume Matcher
import streamlit as st
import fitz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
resume_name=input("Enter the resume file name: ")
job_description=input("Paste the Job Description: ").lower()

st.title("Resume Matcher")
st.header("Resume Matcher")

if(resume_name.endswith(".pdf")):
    pdf_doc=fitz.open(resume_name)
    totalp=pdf_doc.page_count
    for i in range(0,totalp):
       obj=pdf_doc.load_page(i)
       content=obj.get_text()
       with open("new.txt","a",encoding='utf-8') as f:
            f.write(content)
    resume_name="new.txt"


try:
    with open(resume_name,encoding='utf-8') as main_file:
        words_found=main_file.read()
        words_found=words_found.lower()
        tfid_vectorizer= TfidfVectorizer()
        tfid_matrix=tfid_vectorizer.fit_transform([words_found,job_description])
        tfid_matrix.toarray()
        score=cosine_similarity(tfid_matrix)[0][1]*100
        print(f"Your Score is: {score:.2f}%")
except FileNotFoundError:
    print("File Not Found")

# Missing Words
skills =[
    'python', 'java', 'c++', 'c', 'c#', 'javascript', 'typescript', 'ruby', 'go', 'rust', 'kotlin', 'swift', 'php',
    'html', 'css', 'sql', 'mysql', 'postgresql', 'mongodb', 'sqlite', 'oracle',
    'flask', 'django', 'fastapi', 'spring', 'express', 'rails', 'laravel', 'nodejs',
    'react', 'angular', 'vue', 'svelte', 'nextjs', 'nuxtjs',
    'pandas', 'numpy', 'scikit-learn', 'matplotlib', 'seaborn', 'tensorflow', 'keras', 'pytorch', 'nltk', 'spacy',
    'opencv', 'huggingface', 'transformers',
    'aws', 'gcp', 'azure', 'firebase', 'heroku', 'vercel', 'netlify',
    'docker', 'kubernetes', 'jenkins', 'terraform', 'ansible',
    'linux', 'windows', 'bash', 'powershell',
    'git', 'github', 'gitlab', 'bitbucket',
    'vscode', 'pycharm', 'intellij', 'eclipse', 'netbeans',
    'rest', 'graphql', 'postman', 'swagger',
    'redis', 'elasticsearch', 'cassandra',
    'hadoop', 'spark', 'hive', 'bigquery',
    'excel', 'tableau', 'powerbi', 'looker',
    'jupyter', 'colab',
    'unit testing', 'pytest', 'jest', 'mocha', 'cypress',
    'agile', 'scrum', 'jira', 'confluence',
    'oop', 'dsa', 'api', 'jwt', 'authentication', 'authorization',
    'regex', 'encryption', 'multithreading', 'parallel computing', 'sockets'
]

missing_words=set()
cleaned_jd=[]
cleaned_resume=[]
resume_list=words_found.lower().split()
jd_list=job_description.lower().split()
for word1 in jd_list:
    cleaned_word=word1.strip(".,:;()[]{}")
    cleaned_jd.append(cleaned_word)
for word2 in resume_list:
    cleaned_word2=word2.strip(".,:;()[]{}")
    cleaned_resume.append(cleaned_word2)
updated_skills=[]
for skillex in skills:
    if skillex in cleaned_jd:
        updated_skills.append(skillex)
for keyword in updated_skills:
    if keyword not in cleaned_resume:
        missing_words.add(keyword)

if len(missing_words)==0:
    print("Hurrah No Skills are Missing!")
else:
    print("Skills that are missing in your resume are: ")
    for missing_skills in missing_words:
        print(missing_skills) 




