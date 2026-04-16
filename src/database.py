import psycopg2

conn = psycopg2.connect(
    dbname="resume_db",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

def insert_resume(text, embedding):
    cursor.execute(
        "INSERT INTO resumes (content, embedding) VALUES (%s, %s)",
        (text, embedding.tolist())
    )
    conn.commit()
