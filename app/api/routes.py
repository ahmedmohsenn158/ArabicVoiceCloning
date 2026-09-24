from fastapi import APIRouter, HTTPException
from app.api.schemas import AudioValidationRequest, AudioValidationResponse, GenerationRequest, GenerationResponse
from app.audio.validation import validate_audio
from app.services.generation_service import generate_voice
from app.tts.audar import AudarTTSAdapter

router = APIRouter()

# Mocking global model state for API
model = AudarTTSAdapter()
model.load()

@router.get("/status")
def get_status():
    return {
        "gpu": {"device": "cuda:0", "memory": "mock_GB"},
        "model": model.get_model_info(),
        "queue": {"active": 0}
    }

@router.post("/audio/validate", response_model=AudioValidationResponse)
def validate_audio_endpoint(req: AudioValidationRequest):
    result = validate_audio(req.audio_path)
    return AudioValidationResponse(**result)

@router.post("/voice/generate", response_model=GenerationResponse)
def generate_voice_endpoint(req: GenerationRequest):
    if not req.consent_confirmed:
        raise HTTPException(status_code=400, detail="Consent not confirmed")
    
    result = generate_voice(model, req.reference_audio, req.text, req.reference_text)
    return GenerationResponse(**result)
