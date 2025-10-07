from fastapi import FastAPI

app = FastAPI()

notes = [
    {"id": 1, "text": "Купить молоко"},
    {"id": 2, "text": "Сделать дз"}
]

@app.get("/notes")

def get_notes():
    return notes