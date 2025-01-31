import requests

from fastapi import FastAPI, Response

app = FastAPI()

@app.get('/')
def home():
    return {"Chat" : "Bot"}

@app.get('/ask')
def ask(prompt :str):
    res = requests.post('http://ollama:11434/api/generate', json={
        "prompt": prompt,
        "stream" : False,
        "model" : "llama3.1"
    })

    return Response(content=res.text, media_type="application/json")