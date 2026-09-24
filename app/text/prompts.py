import yaml
import os

def load_prompts(config_path: str = "configs/prompts.yaml") -> dict:
    if not os.path.exists(config_path):
        return {}
    with open(config_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return {p["label"]: p["text"] for p in data.get("prompts", [])}

PRESET_PROMPTS = load_prompts()

def get_preset_text(label: str) -> str:
    return PRESET_PROMPTS.get(label, "")
