# Architecture

## Components
- **Gradio UI**: Frontend interface for the station.
- **FastAPI API**: Backend application layer.
- **Audio Service**: Handles microphone recording, validation, preprocessing, and postprocessing.
- **Voice Service**: Manages temporary voice profiles.
- **Text Service**: Handles Arabic text normalization and predefined prompts.
- **TTS Abstraction (BaseTTSModel)**: Ensures the UI/Backend do not depend on any specific model implementation.

## Data Flow
Microphone -> Validation -> Preprocessing -> TTS Model -> GPU Inference -> Generated WAV -> Audio Player

## GPU Pipeline
The application initializes CUDA at startup, loads the configured TTS model into GPU VRAM, and runs a warmup inference to initialize CUDA kernels. Subsequent generations use the pre-loaded model to minimize latency.
