import numpy as np
import librosa

def validate_audio(audio_path: str, min_duration=5.0, max_duration=15.0):
    try:
        y, sr = librosa.load(audio_path, sr=None, mono=True)
    except Exception as e:
        return {"valid": False, "error": f"Failed to load audio: {str(e)}"}
    
    duration = librosa.get_duration(y=y, sr=sr)
    
    # Calculate RMS volume (in dB)
    rms = librosa.feature.rms(y=y)[0]
    rms_db = 20 * np.log10(np.mean(rms) + 1e-9)
    
    # Check clipping (peaks close to 1.0 or -1.0)
    max_amp = np.max(np.abs(y))
    clipping = max_amp >= 0.99
    
    # Calculate silence ratio (simple heuristic using RMS)
    silence_threshold = 1e-3
    silence_ratio = np.sum(rms < silence_threshold) / len(rms)
    
    valid = True
    errors = []
    
    if duration < min_duration:
        valid = False
        errors.append(f"Duration too short ({duration:.1f}s < {min_duration}s)")
    elif duration > max_duration:
        valid = False
        errors.append(f"Duration too long ({duration:.1f}s > {max_duration}s)")
        
    if rms_db < -40.0:  # arbitrary threshold for "too quiet"
        valid = False
        errors.append("Recording is too quiet")
        
    if silence_ratio > 0.5:
        valid = False
        errors.append("Excessive silence detected")
        
    return {
        "valid": valid,
        "duration": float(duration),
        "rms": float(rms_db),
        "clipping": bool(clipping),
        "silence_ratio": float(silence_ratio),
        "errors": errors
    }
