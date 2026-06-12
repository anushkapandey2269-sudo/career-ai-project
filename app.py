import streamlit as st
import pandas as pd
from model import CareerModel

# PAGE CONFIG (must be first)
st.set_page_config(
    page_title="Career AI Dashboard",
    page_icon="🚀",
    layout="centered"
)

# ---------- HEADER ----------
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>
        🚀 Career AI Dashboard
    </h1>
    <p style='text-align: center; color: gray; font-size:18px;'>
        Discover your perfect job using AI
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- MODEL ----------
model = CareerModel()
jobs_df = pd.read_csv("data/jobs.csv")

# ---------- INPUT CARD ----------
st.markdown("### ✍️ Enter Your Resume")

resume = st.text_area(
    "",
    placeholder="e.g. I know Python, ML, SQL, Data Analysis...",
    height=150
)

# ---------- BUTTON ----------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    btn = st.button("🔍 Find Best Jobs")

# ---------- OUTPUT ----------
if btn:
    if resume.strip() == "":
        st.warning("Please enter your resume first ⚠️")
    else:
        result = model.match_jobs(resume, jobs_df)
        top = result.head(5)

        st.success("Top Job Matches Found 🎯")

        for i, row in top.iterrows():
            score = round(row['score'] * 100, 2)

            st.markdown(f"""
                <div style="
                    background-color:#111827;
                    padding:15px;
                    border-radius:12px;
                    margin-bottom:10px;
                    color:white;
                ">
                    <h3 style="color:#4CAF50;">💼 {row['job_title']}</h3>
                    <p>⭐ Match Score: <b>{score}%</b></p>
                </div>
            """, unsafe_allow_html=True)