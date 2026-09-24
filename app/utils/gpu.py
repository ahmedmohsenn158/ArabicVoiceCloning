import torch

def get_gpu_info():
    if not torch.cuda.is_available():
        return {
            "available": False,
            "error": "CUDA GPU unavailable"
        }
    
    device = torch.device("cuda:0")
    properties = torch.cuda.get_device_properties(device)
    
    return {
        "available": True,
        "name": properties.name,
        "total_memory_gb": properties.total_memory / (1024**3),
        "cuda_version": torch.version.cuda
    }
