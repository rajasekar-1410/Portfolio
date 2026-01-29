import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
# ================================
# 📌 PROJECTS SECTION
# ================================

st.markdown("---")
st.subheader("📂 Projects")

# ------------------------------------------------
# PROJECT 1: END-TO-END CUSTOMER ANALYTICS & CHURN
# ------------------------------------------------
st.markdown("## 📈 End-to-End Customer Analytics and Churn Prediction Platform")

st.write("""
Developed an end-to-end analytics and machine learning platform to analyze customer behavior
and predict churn risk. The system helps businesses identify high-risk customers, understand
churn patterns, and simulate churn risk for new customer profiles to support data-driven
retention strategies.
""")

st.markdown("### 🛠️ Key Contributions")
st.write("""
- Cleaned and preprocessed real-world telecom customer data using Pandas  
- Performed customer analytics and KPI-based churn analysis  
- Built and evaluated Logistic Regression, Decision Tree, and Random Forest models  
- Selected Random Forest for deployment based on performance and recall  
- Implemented churn probability scoring with Low / Medium / High risk classification  
- Persisted trained models using Pickle for reuse without retraining  
- Built an interactive Streamlit dashboard for analytics, prediction, and simulation  
""")

st.markdown("**Technologies:** Python, Pandas, NumPy, Scikit-learn, Pickle, Streamlit, Git, GitHub")

# ------------------------------------------------
# PROJECT 2: SALES DATA ANALYSIS DASHBOARD
# ------------------------------------------------
st.markdown("---")
st.markdown("## 📊 Sales Data Analysis Dashboard")

st.write("""
Developed a data analytics dashboard to analyze sales performance across regions, products,
and time periods. The project focuses on transforming raw sales data into meaningful insights
to support business decision-making.
""")

st.markdown("### 🛠️ Key Contributions")
st.write("""
- Cleaned and processed raw sales data using Pandas  
- Performed exploratory data analysis to identify trends and patterns  
- Stored structured data using SQLite for lightweight database operations  
- Created visualizations using Matplotlib for key sales metrics  
- Built an interactive Streamlit dashboard to display KPIs and charts  
""")

st.markdown("**Technologies:** Python, Pandas, NumPy, SQLite, Matplotlib, Streamlit, Git, GitHub")

# ------------------------------------------------
# PROJECT 3: FINAL YEAR PROJECT (ACADEMIC)
# ------------------------------------------------
st.markdown("---")
st.markdown("## 🎓 Final Year Project")
st.markdown("### A Hybrid Machine Learning Framework for Disease Risk Assessment and Safe Drug Recommendation")

st.markdown("### 🧩 Problem Statement")
st.write("""
Traditional healthcare systems often treat disease prediction, drug recommendation,
and safety validation as separate processes, leading to inefficiencies and increased
medication risk.
""")

st.markdown("### 🎯 Objective")
st.write("""
- Predict diseases based on patient health data using machine learning  
- Recommend suitable drugs for the predicted disease  
- Validate drug safety to reduce potential medication risks  
""")

st.markdown("### ⭐ Key Features")
st.write("""
- Machine learning–based disease prediction  
- Drug recommendation logic  
- Safety validation layer  
- Structured data processing and analysis  
""")

st.markdown("**Technologies:** Python, Pandas, NumPy, Machine Learning Algorithms, MySQL")

# ------------------------------------------------
# PROJECT 4: DATA ANALYTICS DEMO
# ------------------------------------------------
st.markdown("---")
st.subheader("📊 Data Analytics Demo – Student Performance Analysis")

st.write("""
This demo showcases exploratory data analysis skills using Python.
The dataset contains student scores in mathematics, reading, and writing.
""")

# Load dataset safely
try:
    df = pd.read_csv("StudentsPerformance.csv")
    st.success("Dataset loaded successfully")
except FileNotFoundError:
    st.error("Dataset file not found. Please ensure 'StudentsPerformance.csv' is in the project folder.")
    st.stop()

st.markdown("### 🔍 Dataset Preview")
st.dataframe(df.head())

st.markdown("### 📈 Statistical Summary")
st.dataframe(df.describe())

st.markdown("### 📊 Average Scores by Gender")

gender_avg = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()

fig, ax = plt.subplots(figsize=(5, 3.2))

gender_avg.plot(kind="bar", ax=ax, width=0.6)

ax.set_title("Average Scores by Gender", fontsize=11)
ax.set_ylabel("Average Score")
ax.set_xlabel("Gender")
ax.set_xticklabels(gender_avg.index, rotation=0)

ax.legend(
    title="Subject",
    loc="upper left",
    bbox_to_anchor=(1.02, 1),
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

📍 **Location:** Villupuram, Tamil Nadu, India
""")
