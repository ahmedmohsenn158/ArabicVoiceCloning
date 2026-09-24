import torch

def initialize_gpu():
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

if __name__ == "__main__":
    print("Checking GPU...")
    result = initialize_gpu()
    if result["available"]:
        print("CUDA: available")
        print("GPU: detected")
        print(f"Device: cuda:0 ({result['name']})")
        print(f"VRAM: {result['total_memory_gb']:.2f} GB")
        print(f"CUDA Version: {result['cuda_version']}")
    else:
        print("CUDA: unavailable")
        print("GPU: not detected")
        print("⚠ CPU DEVELOPMENT MODE: Voice generation will be significantly slower.")
