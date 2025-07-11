""" In this the functions takes two string type arguments namely resume_string and jd_string one function returns
where as other returns missing_words """

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_score(resume_string,jd_string):
    resume_string=resume_string.lower()
    jd_string=jd_string.lower()
    # Creating a Tfidfvectorizer object
    tfidfvectorizer= TfidfVectorizer()
    # Use fit_transform to vectorize them
    tfid_matrix=tfidfvectorizer.fit_transform([resume_string,jd_string])
    tfid_matrix.toarray()
    # Compare them using Cossine_similarity this compares each position in both array and assigns values
    score=cosine_similarity(tfid_matrix)[0][1]*100
    return f"{score:.2f}%"

def get_missingwords(resume_string,jd_string):
    # convert the string into list using split then remove special characters using strip
    resume_words=resume_string.lower().split()
    cleaned_resume=set()
    for resume_word in resume_words:
        resume_word=resume_word.strip(".,:;()[]{}")
        resume_word=resume_word.replace("-","")
        cleaned_resume.add(resume_word)
    jd_words=jd_string.lower().split()
    cleaned_jd=set()
    for jd_word in jd_words:
        jd_word=jd_word.strip(".,:;()[]{}")
        jd_word=jd_word.replace("-","")
        cleaned_jd.add(jd_word)
    #skills
    # to return only skills not other words
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
    missing_skills=set()
    for missing_skill in skills:
        if missing_skill not in cleaned_resume and missing_skill in cleaned_jd:
            missing_skills.add(missing_skill)
    missing=""
    for word in missing_skills:
        missing+= word +"\n"
    return missing


    
