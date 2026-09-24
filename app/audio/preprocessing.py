import librosa
import soundfile as sf
import numpy as np

def preprocess_reference(input_path: str, output_path: str, target_sr=24000):
    """
    Load, convert to mono, resample, and normalize amplitude without aggressive denoising.
    """
    # Load and convert to mono
    y, sr = librosa.load(input_path, sr=target_sr, mono=True)
    
    # Trim excessive silence at the beginning and end
    y_trimmed, _ = librosa.effects.trim(y, top_db=30)
    
    # Normalize amplitude
    max_amp = np.max(np.abs(y_trimmed))
    if max_amp > 0:
        y_normalized = y_trimmed / max_amp * 0.95  # Normalize to -0.45 dBFS
    else:
        y_normalized = y_trimmed
        
    # Save the processed audio
    sf.write(output_path, y_normalized, target_sr, subtype='PCM_16')
    return output_path
