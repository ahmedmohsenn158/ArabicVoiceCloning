from abc import ABC, abstractmethod

class BaseTTSModel(ABC):
    @abstractmethod
    def load(self):
        """Load the model into memory/GPU"""
        pass
        
    @abstractmethod
    def unload(self):
        """Unload the model and free memory"""
        pass
        
    @abstractmethod
    def is_loaded(self) -> bool:
        """Check if model is currently loaded"""
        pass
        
    @abstractmethod
    def clone_voice(self, reference_audio: str, reference_text: str = None):
        """Process reference audio for cloning (if separate step required)"""
        pass
        
    @abstractmethod
    def generate(self, text: str, voice_profile=None):
        """Generate speech from text using an existing voice profile"""
        pass
        
    @abstractmethod
    def clone_and_generate(self, reference_audio: str, text: str, reference_text: str = None) -> str:
        """Clone voice from reference and generate speech for text. Returns path to output audio."""
        pass
        
    @abstractmethod
    def get_model_info(self) -> dict:
        """Return model metadata (name, parameters, language support, etc.)"""
        pass
