import argparse
from app.utils.logging import logger

def download_models():
    parser = argparse.ArgumentParser(description="Download TTS Models")
    parser.add_argument("--model", type=str, default="all", help="Model to download (audar, omnivoice, f5tts, all)")
    args = parser.parse_args()
    
    logger.info(f"Starting model download for: {args.model}")
    logger.info("NOTE: This is a placeholder. In a real scenario, this would use huggingface_hub to download models into the models/ directory.")
    
    if args.model in ["audar", "all"]:
        logger.info("Downloading Audar Flash model...")
        # from huggingface_hub import snapshot_download
        # snapshot_download(repo_id="Audar/Audar-TTS-V1-Flash", local_dir="models/audar_flash")
        
    if args.model in ["omnivoice", "all"]:
        logger.info("Downloading OmniVoice model...")
        
    if args.model in ["f5tts", "all"]:
        logger.info("Downloading F5-TTS model...")
        
    logger.info("Model download complete.")

if __name__ == "__main__":
    download_models()
