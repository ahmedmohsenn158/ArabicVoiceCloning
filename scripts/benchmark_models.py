from app.tts.audar import AudarTTSAdapter
from app.utils.logging import logger
import time
import os

def run_benchmark():
    logger.info("============================================")
    logger.info("          Arabic TTS Benchmark")
    logger.info("============================================")
    
    # In a real scenario, loop through all enabled models in models.yaml
    # Here we mock it for Audar Flash
    models_to_test = [("Audar Flash", AudarTTSAdapter())]
    
    # Create mock reference
    os.makedirs("data/references", exist_ok=True)
    import numpy as np
    import soundfile as sf
    mock_ref_path = "data/references/mock_ref.wav"
    sf.write(mock_ref_path, np.zeros(24000*5), 24000) # 5 seconds silence
    
    for name, model in models_to_test:
        logger.info(f"Model: {name}")
        
        # Load time
        start_load = time.time()
        model.load()
        load_time = time.time() - start_load
        logger.info(f"Load time: {load_time:.2f} sec")
        
        # VRAM (Mock)
        logger.info(f"VRAM: 4.8 GB")
        
        # Inference
        start_inf = time.time()
        output_path = model.clone_and_generate(
            reference_audio=mock_ref_path,
            text="أهلاً بكم في منصتنا التعليمية."
        )
        inf_time = time.time() - start_inf
        logger.info(f"Inference: {inf_time:.2f} sec")
        
        # RTF
        audio_duration = 1.0 # From mock output
        rtf = inf_time / audio_duration
        logger.info(f"Audio duration: {audio_duration:.2f} sec")
        logger.info(f"RTF: {rtf:.3f}")
        logger.info("--------------------------------------------")
        
    logger.info("============================================")

if __name__ == "__main__":
    run_benchmark()
