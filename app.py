import streamlit as st

st.set_page_config(page_title="Rajasekar | Data Analyst Portfolio", layout="wide")

st.title("👋 Hi, I'm Rajasekar")

st.subheader("Aspiring Data Analyst")

st.write("""
Aspiring Data Analyst with a strong foundation in Python, MySQL, and data analysis libraries such as Pandas and NumPy.
Skilled in data cleaning, analysis, and visualization using Matplotlib and Power BI to derive meaningful insights from
structured datasets. Currently pursuing B.Tech at IFET College of Engineering, working on a final-year project titled
“A Machine Learning Approach to Disease Prediction and Drug Recommendation with Safety Validation.” Passionate about data-driven problem solving, database concepts, and continuously learning analytical tools to build impactful solutions.
""")

st.markdown("---")
st.subheader("🛠️ Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💻 Programming")
    st.write("- Python")
    st.write("- C (Basics)")

    st.markdown("### 🗄️ Databases")
    st.write("- MySQL")
    st.write("- Oracle (Basics)")

with col2:
    st.markdown("### 📊 Data Analysis & Visualization")
    st.write("- Pandas")
    st.write("- NumPy")
    st.write("- Matplotlib")
    st.write("- Power BI")

    st.markdown("### 📌 Core Knowledge")
    st.write("- Data Cleaning")
    st.write("- Exploratory Data Analysis")
    st.write("- Database Fundamentals")

st.markdown("---")
st.subheader("🎓 Final Year Project")

st.markdown("### 📌 Project Title")
st.write(
    "A Hybrid Machine Learning Framework for Disease Risk Assessment and Safe Drug Recommendation"
)

st.markdown("### 🧩 Problem Statement")
st.write("""
Traditional healthcare systems often handle disease prediction, drug recommendation,
and drug safety checks as separate processes. This fragmentation can lead to inefficiencies,
delayed decision-making, and potential medication risks.
""")

st.markdown("### 🎯 Objective")
st.write("""
The objective of this project is to develop an intelligent healthcare system that:
- Predicts diseases based on patient health data using machine learning
- Recommends suitable drugs for the predicted disease
- Performs safety validation to reduce potential medication risks
""")

st.markdown("### 🛠️ Tools & Technologies")
st.write("""
- Python  
- Pandas, NumPy  
- Machine Learning Algorithms  
- MySQL  
""")

st.markdown("### ⭐ Key Features")
st.write("""
- Machine learning–based disease prediction  
- Drug recommendation for predicted diseases  
- Safety validation to minimize medication risks  
- Structured data processing and analysis  
""")

st.markdown("### ✅ Outcome")
st.write("""
This project demonstrates the application of machine learning and data analytics
in healthcare to support disease prediction and safer drug recommendations.
""")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("---")
st.subheader("📊 Data Analytics Demo")

st.write("""
**Student Performance Analysis**

This demo showcases my ability to perform exploratory data analysis using Python.
The dataset contains student scores in mathematics, reading, and writing.
""")

# Load dataset safely
try:
    df = pd.read_csv("StudentsPerformance.csv")
    st.success("Dataset loaded successfully")
except FileNotFoundError:
    st.error("Dataset file not found. Please ensure 'StudentsPerformance.csv' is in the project folder.")
    st.stop()

# Dataset preview
st.markdown("### 🔍 Dataset Preview")
st.dataframe(df.head())

# Statistical summary
st.markdown("### 📈 Statistical Summary")
st.dataframe(df.describe())

st.markdown("### 📊 Average Scores by Gender")

gender_avg = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()

fig, ax = plt.subplots(figsize=(5, 3.2))


gender_avg.plot(
    kind="bar",
    ax=ax,
    width=0.6
)

ax.set_title("Average Scores by Gender", fontsize=12)
ax.set_ylabel("Average Score")
ax.set_xlabel("Gender")
ax.set_xticklabels(gender_avg.index, rotation=0)

# Legend outside top-right (no overlap)
ax.legend(
    title="Subject",
    loc="upper left",
    bbox_to_anchor=(1.02, 1),
    borderaxespad=0,
    frameon=False
)

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")
st.subheader("🎓 Education")

st.write("""
**B.Tech in Artificial Intelligence & Machine Learning (2022 – 2026)**  
IFET College of Engineering
""")

st.markdown("---")
st.subheader("🏢 Internship & Certifications")

st.markdown("### 💼 Internship Experience")

st.write("""
**Intern – Layercodes Technologies**  
Offline Internship | January 2025  

- Gained exposure to development workflows and real-world project environments  
- Worked with foundational programming and database-related concepts  
- Developed understanding of industry practices and teamwork  
""")

st.write("""
**Data Visualisation Virtual Intern – TATA**  
Micro-Internship | January 2025  

- Framing the Business Scenario  
- Choosing the Right Visuals
- Creating Effective Visuals
- Communicating Insights and Analysis
""")

st.markdown("### 📜 Certifications")

st.write("""
- **Python Certification** – GUVI (2023)  
- **Introduction to SQL** – Completed 2026  
""")

st.markdown("---")
st.subheader("📬 Contact")

st.write("""
📧 **Email:** rajasekar.d1410@gmail.com  

🔗 **LinkedIn:** https://www.linkedin.com/in/rajasekar-d-470170269  

💻 **GitHub:** https://github.com/rajasekar-1410  

📞 **Phone:** 9150664818  

📍 **Location:** Villupuram, Tamil Nadu, India
""")
