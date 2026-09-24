# Troubleshooting

- **CUDA errors / Out of memory**: Ensure no other large models are running on the GPU. Reduce batch size (if applicable) or use a smaller model.
- **Microphone problems**: Ensure the browser has permission to access the microphone. Check the audio input device in your OS settings.
- **Model download errors**: Check internet connectivity. Ensure you have the necessary huggingface permissions if accessing gated models.
- **Audio artifacts**: The reference audio might be noisy or over-processed. Try recording a cleaner reference in a quiet environment.
- **Slow inference**: Ensure the model is running on the GPU (`scripts/gpu_check.py`).
