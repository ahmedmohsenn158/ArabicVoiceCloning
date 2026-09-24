from app.tts.audar import AudarTTSAdapter

def test_audar_model_loading():
    model = AudarTTSAdapter(device="cpu")
    assert model.is_loaded() == False
    
    model.load()
    assert model.is_loaded() == True
    
    info = model.get_model_info()
    assert info["type"] == "audar"
    
    model.unload()
    assert model.is_loaded() == False
