import time

def create_voice_profile(reference_audio: str, language: str = "ar", dialect: str = "egyptian") -> dict:
    return {
        "id": f"session_{int(time.time())}",
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "reference_audio": reference_audio,
        "language": language,
        "dialect": dialect,
        "consent_confirmed": True
    }
