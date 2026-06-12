import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import clean_text

class CareerModel:
    def match_jobs(self, resume, jobs_df):
        resume = clean_text(resume)
        jobs_df["skills"] = jobs_df["skills"].apply(clean_text)

        all_text = [resume] + jobs_df["skills"].tolist()

        vectorizer = TfidfVectorizer()
        tfidf = vectorizer.fit_transform(all_text)

        scores = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()
        jobs_df["score"] = scores

        return jobs_df.sort_values(by="score", ascending=False)
    def skill_gap(resume, job_skills):
    resume_words = set(resume.lower().split())
    job_words = set(job_skills.lower().split())
    missing = job_words - resume_words
    return list(missing)