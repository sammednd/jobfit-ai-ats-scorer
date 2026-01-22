import re

def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def make_preview(text: str, max_len: int = 400) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len].rstrip() + "..."
