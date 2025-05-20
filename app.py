import streamlit as st #type: ignore
import streamlit.components.v1 as components #type: ignore
from streamlit_lottie import st_lottie #type: ignore
import requests
import json

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Deven's Data Science Portfolio", layout="wide")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

animation = load_lottie_url("https://raw.githubusercontent.com/ShahaDeven/Portfolio_website/main/assets/Animation.json")


# ---- HEADER ----
st.title("👋 Hi, I'm Deven Shah")
st.markdown("""
🎓 Master's Student in Data Science @ University at Buffalo  
📊 Passionate about Machine Learning, Data Visualization, and Predictive Modeling  
📫 [LinkedIn](https://linkedin.com/in/deven-shaha) | [GitHub](https://github.com/ShahaDeven) | deven.rshaha@gmail.com
""")

# ---- ABOUT ME ----
st.header("👨‍💻 About Me")

col1, col2,col3 = st.columns([1, 2, 3])

with col1:
    st.image("https://raw.githubusercontent.com/ShahaDeven/Portfolio_website/main/assets/profile.jpeg", width=200)  
with col2:
    st_lottie(animation, height=180)
with col3:
    st.markdown("""
        **🎓 Deven Shah**  
        Master's Student in Data Science @ University at Buffalo  
        📫 deven.rshaha@gmail.com  
        🌐 [LinkedIn](https://linkedin.com/in/deven-shaha) | [GitHub](https://github.com/ShahaDeven)

        I'm a data science enthusiast passionate about machine learning, analytics, and storytelling through data.  
        I enjoy combining technical solutions with creativity, and I've worked on projects in computer vision, NLP, and data visualization.
        """)




# ---- MACHINE LEARNING PROJECTS ----
st.header("🧠 Machine Learning Projects")

with st.expander("🎓 Graduate Admission Prediction"):
    st.markdown("""
    - **Tools:** Python, Scikit-learn, Pandas, Jupyter Notebook  
    - Led an independent research project under Dr. David Doermann to predict graduate admissions using historical applicant data.  
    - Engineered features and ranked attributes using AHP (Analytic Hierarchy Process).  
    - Trained Random Forest, Neural Network, and Gradient Boosting models, achieving 74% accuracy with k-fold cross-validation.  
    - Visualized model performance and feature importance for interpretability.  
    """)

with st.expander("🐜 Fleet Management Optimization with Ant Colony"):
    st.markdown("""
    - **Tools:** Python, Jupyter Notebook  
    - Developed an optimized routing system using Ant Colony Optimization for large-scale vehicle fleets.  
    - Considered capacity, speed, and time constraints to compute efficient delivery paths.  
    - Applied Clark-weight cost modeling to compare VRP and non-VRP scenarios.  
    - 📄 [Published at IEEE Xplore](https://ieeexplore.ieee.org/document/10988157)
    """)

with st.expander("👤 Fake Account Detection (IEEE Publication)"):
    st.markdown("""
    - **Tools:** Python, Scikit-learn, TFIDF  
    - Built a classifier for identifying fake social media accounts with 87% accuracy.  
    - Preprocessing, feature scaling, and vectorization used for model performance.  
    - 📄 [Published at IEEE Xplore](https://ieeexplore.ieee.org/document/10459570)
    """)

with st.expander("📡 Deep Learning for Exoplanet Exploration"):
    st.markdown("""
    - **Tools:** Python, TensorFlow, Scikit-learn, NASA Exoplanet Archive Dataset  
    - Used artificial neural networks (ANNs) to detect exoplanets from light curve data with 88.3% accuracy.  
    - Employed Gradient Boosting to predict habitability scores, achieving 91.06% accuracy.  
    - Combined astronomy and machine learning to enhance detection of Earth-like exoplanets.  
    """)

with st.expander("😊 Happiness Prediction Model (SunHacks Winner)"):
    st.markdown("""
    - **Tools:** Python, NLP, Twitter API, ML  
    - Used Random Forest, MLP, Logistic Regression to predict user happiness.  
    - Analyzed Twitter sentiment & music preferences.  
    - 🏆 Won ‘Most Innovative and Outstanding Performance’ at SunHacks 2022
    """)

with st.expander("🌾 Agriculture Drone Fogging (Design Patent)"):
    st.markdown("""
    - Built a drone from scratch for pesticide fogging in farmlands.  
    - Strategically placed foggers and used a camera for field mapping.  
    - 🧾 Design Patent Granted: Patent No. 404133-001
    """)


# ---- TABLEAU PROJECTS ----
st.header("📊 Tableau Dashboards")

with st.expander("✈️ Aircraft Reviews Dashboard"):
    st.markdown("""
    - Analyzed airline passenger reviews across key categories: Cabin Staff, Entertainment, Food, Ground Service, Seat Comfort, and Value for Money.  
    - Included filter options for Passenger Type (e.g., solo, couple, business) and Seat Type (e.g., Economy, Business, First Class).  
    - Created an interactive dashboard to identify satisfaction trends and performance insights across airlines and travel classes.  
    - [View on Tableau Public](https://public.tableau.com/views/Aircraft_Reviews/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
    """)
    components.html(
        """
        <iframe src="https://public.tableau.com/views/Aircraft_Reviews/Dashboard1?:embed=y&:display_count=yes"
        width="1000" height="650" frameborder="0" allowfullscreen></iframe>
        """,
        height=650,
    )

# ---- RESUME ----
st.header("📄 Resume")
resume_url = "https://raw.githubusercontent.com/ShahaDeven/Portfolio_website/main/Deven_Rahul_Shah_Resume.pdf"
view_url = "https://github.com/ShahaDeven/Portfolio_website/blob/main/Deven_Rahul_Shah_Resume.pdf"

import requests
resume_file = requests.get(resume_url).content
st.download_button(
    label="⬇️ Download Resume (PDF)",
    data=resume_file,
    file_name="Deven_Rahul_Shah_Resume.pdf",
    mime="application/pdf"
)

st.markdown(f"[🔗 Open Resume in New Tab]({view_url})")

# ---- PUBLICATIONS ----
st.header("📚 Publications")

with st.expander("🚗 Fleet Management Optimization with Ant Colony - IEEE Xplore"):
    st.markdown("""
    - Published research on vehicle routing using Ant Colony Optimization.  
    - 📄 [View on IEEE Xplore](https://ieeexplore.ieee.org/document/10988157)
    """)

with st.expander("🕊️ Comparative Analysis of Object Identification Techniques for Bird Species - IEEE Xplore"):
    st.markdown("""
    - Conducted a performance comparison of YOLOv5 and YOLOv8 for bird species detection using custom video-based datasets.  
    - Demonstrated YOLOv8's superior accuracy on larger, multi-class datasets from tropical regions and sanctuaries.  
    - Aimed to improve identification accuracy for ornithological research and conservation efforts.  
    - 📄 [View on IEEE Xplore](https://ieeexplore.ieee.org/document/10837870)
    """)


with st.expander("👤 Fake Account Detection - IEEE Xplore"):
    st.markdown("""
    - Published research on machine learning techniques for fake account classification.  
    - Achieved 87% accuracy by enhancing feature preprocessing and model selection.  
    - 📄 [View on IEEE Xplore](https://ieeexplore.ieee.org/document/10459570)
    """)

# ---- CONTACT ----
st.header("📬 Contact Me")
st.markdown("""
- 📧 deven.rshaha@gmail.com  
- 🌐 [LinkedIn](https://linkedin.com/in/deven-shaha)  
- 💻 [GitHub](https://github.com/ShahaDeven)
""")
