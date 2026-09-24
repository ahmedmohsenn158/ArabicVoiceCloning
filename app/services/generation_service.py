import os
import time
from app.audio.validation import validate_audio
from app.audio.preprocessing import preprocess_reference
from app.tts.base import BaseTTSModel
from app.utils.logging import logger
from librosa import get_duration

def generate_voice(
    model: BaseTTSModel,
    reference_audio: str,
    text: str,
    reference_text: str = None
) -> dict:
    
    start_time = time.time()
    
    # 1. Validate Reference
    validation_result = validate_audio(reference_audio)
    if not validation_result["valid"]:
        logger.error(f"Invalid reference audio: {validation_result['errors']}")
        return {"success": False, "error": f"Invalid reference audio: {validation_result['errors']}"}
        
    logger.info("Reference recording accepted")
    
    # 2. Preprocess Reference
    processed_audio_path = f"data/temporary/proc_{int(time.time())}.wav"
    os.makedirs("data/temporary", exist_ok=True)
    
    preprocess_start = time.time()
    processed_audio = preprocess_reference(reference_audio, processed_audio_path)
    ref_processing_time = time.time() - preprocess_start
    
    # 3. Model Inference (includes text normalization internally or we do it here)
    # TODO: Add text normalization here
    
    logger.info("Starting generation")
    inference_start = time.time()
    try:
        output_audio_path = model.clone_and_generate(
            reference_audio=processed_audio,
            text=text,
            reference_text=reference_text
        )
    except Exception as e:
        logger.error(f"Generation failed: {str(e)}")
        return {"success": False, "error": f"Generation failed: {str(e)}"}
        
    inference_time = time.time() - inference_start
    
    logger.info("Generation complete")
    
    # Post-processing (omitted for now since output is already saved by adapter)
    post_process_time = 0.0
    
    total_time = time.time() - start_time
    
    
    audio_duration = get_duration(filename=output_audio_path)
    rtf = total_time / audio_duration if audio_duration > 0 else 0
    
    logger.info(f"RTF={rtf:.2f}")
    
    return {
        "success": True,
        "output_path": output_audio_path,
        "metrics": {
            "ref_processing": ref_processing_time,
            "inference": inference_time,
            "post_processing": post_process_time,
            "total_time": total_time,
            "audio_duration": audio_duration,
            "rtf": rtf
        }
    }
