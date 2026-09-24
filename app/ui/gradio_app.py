import gradio as gr
import os
import time
from app.services.generation_service import generate_voice
from app.tts.audar import AudarTTSAdapter
from app.utils.logging import logger

from app.text.prompts import PRESET_PROMPTS

# Initialize Model (Mocking global state for UI simplicity)
model = AudarTTSAdapter()
model.load()

def update_text_from_preset(preset_key):
    return PRESET_PROMPTS.get(preset_key, "")

def handle_generation(audio_in, text_in, consent_checked):
    if not consent_checked:
        return None, "⚠ Please confirm speaker consent before generating.", ""
        
    if not audio_in:
        return None, "⚠ Please record or upload a reference voice.", ""
        
    if not text_in.strip():
        return None, "⚠ Please enter text to generate.", ""
        
    result = generate_voice(model, audio_in, text_in)
    
    if not result["success"]:
        return None, f"⚠ Error: {result['error']}", ""
        
    metrics = result["metrics"]
    stats = (
        f"Generation time: {metrics['total_time']:.1f} sec\n"
        f"Audio duration: {metrics['audio_duration']:.1f} sec\n"
        f"RTF: {metrics['rtf']:.3f}"
    )
    
    return result["output_path"], "✓ Generation successful", stats

def create_ui():
    with gr.Blocks(title="Arabic Voice Station") as demo:
        gr.Markdown("# 🎙️ Arabic Voice Cloning Station")
        
        with gr.Row():
            gr.Markdown("**GPU:** RTX 5090 ● READY (Mock)")
            gr.Markdown("**Model:** Audar Flash")
            
        with gr.Group():
            gr.Markdown("### 1. RECORD YOUR VOICE")
            audio_input = gr.Audio(sources=["microphone", "upload"], type="filepath", label="Reference Voice (5-15s)")
            
            consent_checkbox = gr.Checkbox(label="I confirm that I am the speaker or have permission from the speaker to clone this voice.")
            
        with gr.Group():
            gr.Markdown("### 2. CHOOSE TEXT")
            preset_dropdown = gr.Dropdown(choices=list(PRESET_PROMPTS.keys()), label="Select phrase (Optional)")
            text_input = gr.Textbox(label="اكتب النص العربي هنا...", lines=3, max_lines=5)
            
            preset_dropdown.change(fn=update_text_from_preset, inputs=preset_dropdown, outputs=text_input)
            
            generate_btn = gr.Button("Generate Voice", variant="primary")
            
        with gr.Group():
            gr.Markdown("### 3. GENERATED VOICE")
            audio_output = gr.Audio(label="Output Audio", interactive=False)
            status_output = gr.Markdown("")
            stats_output = gr.Markdown("")
            
        generate_btn.click(
            fn=handle_generation,
            inputs=[audio_input, text_input, consent_checkbox],
            outputs=[audio_output, status_output, stats_output]
        )
        
    return demo

if __name__ == "__main__":
    demo = create_ui()
    demo.launch(server_name="127.0.0.1", server_port=7860)
