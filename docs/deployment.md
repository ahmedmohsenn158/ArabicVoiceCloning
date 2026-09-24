# Deployment

## RTX 5090 Setup
1. **Clone the repository**:
   ```bash
   git clone <repository_url> arabic-voice-cloning-station
   cd arabic-voice-cloning-station
   ```

2. **Create Python Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Verify GPU**:
   ```bash
   python scripts/gpu_check.py
   ```
   Ensure it outputs "CUDA: available" and detects the RTX 5090.

4. **Download Models**:
   ```bash
   python scripts/download_models.py --model audar_flash
   ```

5. **Start Station**:
   ```bash
   python scripts/run_station.py
   ```
   Access the UI at `http://127.0.0.1:7860`.
