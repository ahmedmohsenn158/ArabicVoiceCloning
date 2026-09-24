from app.tts.base import BaseTTSModel
from app.tts.audar import AudarTTSAdapter
from app.tts.omnivoice import OmniVoiceAdapter
from app.tts.f5tts import F5TTSAdapter

def get_tts_model(model_name: str, device: str = "cuda") -> BaseTTSModel:
    model_name = model_name.lower()
    if model_name == "audar_flash":
        return AudarTTSAdapter(device=device)
    elif model_name == "omnivoice":
        return OmniVoiceAdapter(device=device)
    elif model_name == "f5tts_ar":
        return F5TTSAdapter(device=device)
    else:
        raise ValueError(f"Unknown model: {model_name}")
