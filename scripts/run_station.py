import argparse
import sys
from pathlib import Path
import uvicorn

# Add project root to path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.utils.logging import logger

def main():
    parser = argparse.ArgumentParser(description="Run Arabic Voice Cloning Station")
    parser.add_argument("--model", type=str, default="audar_flash", help="Model to use")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host IP")
    parser.add_argument("--port", type=int, default=7860, help="Port")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()
    
    logger.info(f"Starting station on {args.host}:{args.port} using model {args.model}")
    
    uvicorn.run("app.main:app", host=args.host, port=args.port, reload=args.debug)

if __name__ == "__main__":
    main()
