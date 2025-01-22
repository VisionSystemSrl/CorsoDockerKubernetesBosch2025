FROM nvidia/cuda:11.8.0-runtime-ubuntu20.04

# Install Python and required tools
RUN apt-get update && apt-get install -y python3 python3-pip

# Install a Python library (e.g., PyTorch with GPU support)
RUN pip3 install torch torchvision torchaudio
