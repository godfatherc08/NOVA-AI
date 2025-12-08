import re

def clean_text(text: str) -> str:
    # Remove timestamps like “1/3/23 10:24 PM”
    text = re.sub(r'\b\d{1,2}\/\d{1,2}\/\d{2,4}\s+\d{1,2}:\d{2}\s*(AM|PM)\b', ' ', text)

    # Remove page numbers like “14 / FEBRUARY 2023”
    text = re.sub(r'\b\d+\s*\/\s*[A-Z]+\s+\d{4}\b', ' ', text)

    # Remove “indd” artifacts
    text = re.sub(r'\b\w*\.?indd\b.*', ' ', text)

    # Remove sequences of numbers (page numbers, figure numbers)
    text = re.sub(r'\b\d{1,4}\b', ' ', text)

    # Remove ALL CAPS lines (magazine section headers)
    text = re.sub(r'^[A-Z0-9 ,\-]{8,}$', ' ', text, flags=re.MULTILINE)

    # Remove broken hyphenated line endings: "cinematog-\nrapher"
    text = re.sub(r'-\s*\n\s*', '', text)

    # Normalize newlines
    text = re.sub(r'\n\s*\n+', '\n\n', text)

    # Collapse excessive spaces
    text = re.sub(r'\s{2,}', ' ', text)

    return text.strip()
