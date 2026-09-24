from app.text.normalization import normalize_arabic_text

def test_arabic_normalization():
    text = "  أهلاً    بكم في منصتنا  "
    normalized = normalize_arabic_text(text)
    assert normalized == "أهلاً بكم في منصتنا"
