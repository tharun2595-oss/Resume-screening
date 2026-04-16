import pandas as pd
from preprocessing import clean_text
from embeddings import get_embedding
from database import insert_resume

df = pd.read_csv("data/resumes.csv")

for i, row in df.iterrows():
    cleaned = clean_text(row['Resume_str'])
    emb = get_embedding(cleaned)
    insert_resume(cleaned, emb)

print(" Data loaded into PostgreSQL")
