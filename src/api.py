from fastapi import FastAPI
from pydantic import BaseModel
from src.embeddings import get_embedding
from src.matching import match
import psycopg2
import numpy as np

app = FastAPI()

class JobRequest(BaseModel):
    text: str
@app.get("/")
def home():
    return {"meassage": "Resume Screening API Runnning"}

def fetch_resumes():
    conn = psycopg2.connect(
        dbname="resume_db",
        user="postgres",
        password="postgres",
        host="localhost"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT content, embedding FROM resumes")
    data = cursor.fetchall()
    return data

@app.post("/match")
def match_resumes(request: JobRequest):
    #  Create embedding
    job_emb = get_embedding(request.text)

    #  Fetch data
    data = fetch_resumes()
    texts = [d[0] for d in data]
    embeddings = [np.array(d[1], dtype=float) for d in data]

    #  Match
    scores = match(job_emb, embeddings)

    #  Sort results
    results = sorted(
        list(zip(texts, scores)),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    return {"top_matches": results}

