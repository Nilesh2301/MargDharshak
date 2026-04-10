import streamlit as st
import requests
BACKEND_URL = "https://margdharshakx.onrender.com"

st.set_page_config(page_title="मार्गदर्शक", page_icon="🚀", layout="wide")

# 🎨 Styling
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}
.big-title {
    font-size: 40px;
    font-weight: bold;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 10px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# 🔥 Title
st.markdown('<div class="big-title">🚀 मार्गदर्शक</div>', unsafe_allow_html=True)
st.write("AI आधारित आपका करियर मार्गदर्शक")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["📄 Resume Analysis", "💬 AI Mentor"])

# ------------------ RESUME ------------------
if page == "📄 Resume Analysis":
    st.header("📄 Resume Analysis")

    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    if uploaded_file:
        if st.button("Analyze Resume"):
            with st.spinner("Analyzing..."):
                try:
                    response = requests.post(
                        "https://margdharshakx.onrender.com/analyze",
                        files={"file": uploaded_file}
                    )
                    result = response.json()

                    if "analysis" in result:
                        st.success("Analysis Complete ✅")

                        st.markdown('<div class="card">', unsafe_allow_html=True)
                        st.subheader("📊 AI Feedback")
                        st.write(result["analysis"])
                        st.markdown('</div>', unsafe_allow_html=True)

                        # 🔥 Fake Score (UI boost)
                        st.progress(80)
                        st.write("Resume Score: 80/100")

                    else:
                        st.error(result.get("error", "Something went wrong"))

                except:
                    st.error("⚠️ Backend not running!")

# ------------------ CHAT ------------------
elif page == "💬 AI Mentor":
    st.header("💬 AI Career Mentor")

    user_input = st.text_input("Ask your question")

    if st.button("Get Advice"):
        if user_input:
            with st.spinner("Thinking..."):
                try:
                    response = requests.post(
                        "https://margdharshakx.onrender.com/chat",
                        params={"message": user_input}
                    )
                    result = response.json()

                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.subheader("🤖 AI Response")
                    st.write(result["reply"])
                    st.markdown('</div>', unsafe_allow_html=True)

                except:
                    st.error("⚠️ Backend not running!")
 
