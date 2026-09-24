from pydantic import BaseModel
from typing import Optional

class AudioValidationRequest(BaseModel):
    audio_path: str

class AudioValidationResponse(BaseModel):
    valid: bool
    duration: float
    rms: float
    clipping: bool
    silence_ratio: float
    errors: list[str]

class GenerationRequest(BaseModel):
    reference_audio: str
    text: str
    reference_text: Optional[str] = None
    consent_confirmed: bool

class GenerationResponse(BaseModel):
    success: bool
    output_path: Optional[str] = None
    error: Optional[str] = None
    metrics: Optional[dict] = None
