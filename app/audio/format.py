import soundfile as sf
import librosa

def convert_to_wav(input_path: str, output_path: str, target_sr: int = 24000):
    """
    Ensure the output is 24 kHz mono PCM WAV.
    """
    y, sr = librosa.load(input_path, sr=target_sr, mono=True)
    sf.write(output_path, y, target_sr, subtype='PCM_16')
    return output_path
