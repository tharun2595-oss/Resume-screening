import re

def clean_text(text):
    text = re.sub(r'\W', ' ', str(text))
    text = text.lower()
    return text
