# Arabic Voice Cloning Station

A fully local Arabic voice-cloning station designed to record a short reference audio and synthesize high-quality speech with cloned voices using zero-shot TTS models.

## Features
- Microphone recording & validation
- Zero-shot voice cloning (5-15s reference)
- Text normalization & preset prompts
- Supports Audar Flash, OmniVoice, F5-TTS
- Local API & Gradio UI

## Quick Start
See `docs/deployment.md` for detailed instructions on setting up the environment, downloading models, and running the station.

## Architecture
```
                         LOCAL MACHINE
                              │
                              ▼
                 ┌────────────────────────┐
                 │   Arabic Voice Station │
                 │                        │
                 │       Gradio UI        │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │       FastAPI          │
                 │     Application API    │
                 └───────────┬────────────┘
                             │
            ┌────────────────┼─────────────────┐
            │                │                 │
            ▼                ▼                 ▼
       Audio Service    Voice Service     Text Service
            │                │                 │
            └────────────────┼─────────────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │    TTS Abstraction   │
                  └──────────┬───────────┘
                             │
             ┌───────────────┼───────────────┐
             │               │               │
             ▼               ▼               ▼
        Audar Flash      OmniVoice       F5-TTS
             │               │               │
             └───────────────┼───────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   RTX 5090 GPU  │
                    │                 │
                    │ Model in VRAM   │
                    └────────┬────────┘
                             │
                             ▼
                    Generated WAV
                             │
                             ▼
                       Audio Player
```