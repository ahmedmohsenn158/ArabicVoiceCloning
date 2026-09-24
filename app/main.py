import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.ui.gradio_app import create_ui
import gradio as gr

from app.api.routes import router

app = FastAPI(title="Arabic Voice Cloning Station API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "gpu": "Mock RTX 5090",
        "cuda": True,
        "model": "audar_flash",
        "model_loaded": True
    }

# Mount Gradio app
demo = create_ui()
app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=7860, reload=False)
