from fastapi import FastAPI
import requests

app = FastAPI()

OPENROUTER_KEY = "YOUR_KEY"
HF_KEY = "YOUR_KEY"

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/chat")
async def chat(data: dict):
    msg = data["message"]
    model = data["model"]

    if model == "smart":
        return openrouter(msg)
    elif model == "fast":
        return huggingface(msg)

def openrouter(msg):
    res = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_KEY}"},
        json={
            "model": "mistralai/mixtral-8x7b",
            "messages": [{"role": "user", "content": msg}]
        }
    )
    return res.json()

def huggingface(msg):
    res = requests.post(
        "https://api-inference.huggingface.co/models/google/flan-t5-large",
        headers={"Authorization": f"Bearer {HF_KEY}"},
        json={"inputs": msg}
    )
    return res.json()

@app.post("/image")
async def image(data: dict):
    prompt = data["prompt"]

    res = requests.post(
        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
        headers={"Authorization": f"Bearer {HF_KEY}"},
        json={"inputs": prompt}
    )

    return {"image": res.content}
