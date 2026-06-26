from fastapi import FastAPI

app = FastAPI(title="Chatbot API")


@app.get("/")
def read_root():
    return {"message": "Welcome to my first FastAPI app!"}

@app.get("/about")
def health():
    return {
        "message " : "hi i am dhruv"
    }

import random

facts = [
    "Python was released in 1991.",
    "FastAPI is built on Starlette.",
    "Uvicorn is an ASGI server.",
    "JSON is language-independent."
]


@app.get("/random-fact")
def random_fact():
    return {
        "fact": random.choice(facts)
    }

