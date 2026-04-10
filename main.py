from fastapi import FastAPI, UploadFile, File
import pdfplumber
import requests

app = FastAPI()

# 🔐 Put your OpenRouter API key here
OPENROUTER_API_KEY = "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"

# ------------------ HOME ------------------
@app.get("/")
def home():
    return {"message": "Backend working 🚀"}

# ------------------ CHAT ------------------
@app.post("/chat")
async def chat(message: str):
    prompt = f"""
    You are an AI Career Coach.

    Student says:
    {message}

    Give helpful guidance.
    """

    reply = call_ai(prompt)
    return {"reply": reply}

# ------------------ ANALYZE RESUME ------------------
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    # 📄 Extract text from PDF
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    if not text:
        return {"analysis": "Could not read PDF properly ❌"}

    # 🤖 AI Prompt
    prompt = f"""
    Analyze this resume:

    {text}

    Give:
    1. Resume Score out of 100
    2. Skills
    3. Weakness
    4. Career Suggestions
    5. 2-week improvement roadmap
    """

    result = call_ai(prompt)

    return {"analysis": result}

# ------------------ AI CALL FUNCTION ------------------
def call_ai(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "Margdarshak"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return "AI Error: " + response.text