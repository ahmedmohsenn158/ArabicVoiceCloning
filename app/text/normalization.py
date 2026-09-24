import re

def normalize_arabic_text(text: str) -> str:
    """
    Normalizes Arabic text without aggressively removing diacritics
    or punctuation which TTS models might need for prosody.
    """
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    
    # Optional: Basic character normalization (e.g. standardizing alef)
    # text = re.sub(r'[إأآا]', 'ا', text) # Be careful with this, some TTS models expect exact alef
    
    return text.strip()
