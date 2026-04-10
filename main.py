from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend working 🚀"}

@app.post("/chat")
async def chat(message: str):
    return {"reply": f"You said: {message}"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    return {"analysis": "Working ✅"}