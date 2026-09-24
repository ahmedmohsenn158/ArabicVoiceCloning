from app.audio.validation import validate_audio
import os
import soundfile as sf
import numpy as np

def test_duration_validation(tmp_path):
    audio_path = tmp_path / "test.wav"
    # Create a 2 second audio file (too short)
    sf.write(str(audio_path), np.zeros(24000*2), 24000)
    
    result = validate_audio(str(audio_path))
    assert result["valid"] == False
    assert any("Duration too short" in err for err in result["errors"])
    
    # Create an 8 second audio file (valid duration, but might fail on quietness)
    sf.write(str(audio_path), np.random.randn(24000*8), 24000)
    result = validate_audio(str(audio_path))
    assert result["valid"] == True
