# Tutorial: Access GPU Inside a Docker Container and Monitor GPU Usage

This guide will help you set up a Docker container that can access your system's GPU and demonstrate how to monitor GPU usage within the container.


## Prerequisites

1. **NVIDIA GPU**: Ensure you have an NVIDIA GPU installed on your system.
2. **NVIDIA Drivers**: Install the appropriate NVIDIA drivers for your GPU.
3. **Docker Installed**: Ensure Docker is installed on your system.
4. **NVIDIA Container Toolkit**: Install the NVIDIA Container Toolkit to enable GPU access in Docker.

### Install NVIDIA Container Toolkit

Follow these steps to install the NVIDIA Container Toolkit:

```bash
# Add the NVIDIA package repository
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list

# Update and install
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

# Restart the Docker service
sudo systemctl restart docker
```


## Step 1: Create a Simple Docker Image

Create a new folder and add the following `Dockerfile` to define a simple image with GPU support.

### **Dockerfile**
```dockerfile
FROM nvidia/cuda:11.8.0-runtime-ubuntu20.04

# Install Python and required tools
RUN apt-get update && apt-get install -y python3 python3-pip

# Install a Python library (e.g., PyTorch with GPU support)
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Build the Docker Image

Run the following command to build the image:

```bash
docker build -t gpu-app:1.0 .
```


## Step 2: Run the Container with GPU Access

Use the `--gpus` flag to grant the container access to your GPU:

```bash
docker run -it --gpus all --name gpu-container gpu-app:1.0
```

**Explanation**:
- `--gpus all`: Grants the container access to all available GPUs.
- `-it`: Starts the container in interactive mode.
- `--name gpu-container`: Assigns the container a name for easier reference.
- `gpu-app:1.0`: Specifies the Docker image to use.


## Step 3: Verify GPU Access Inside the Container

Once inside the container, you can verify GPU access using the `nvidia-smi` command:

```bash
nvidia-smi
```

You should see a list of your GPU(s) along with their current usage statistics.


## Step 4: Monitor GPU Usage

### Using `nvidia-smi` on the Host

Run the following command on your host machine to monitor GPU usage:

```bash
nvidia-smi
```

This provides real-time information about GPU usage, memory consumption, and running processes.


## Step 5: Stop and Remove the Container

Stop the container when you're finished:

```bash
docker stop gpu-container
```

Remove the container:

```bash
docker rm gpu-container
```


## Additional Notes

- To limit GPU access to specific GPUs, use the `--gpus` flag with device IDs, e.g., `--gpus '"device=0,1"'`.
- For GPU-intensive tasks, consider using Docker images preconfigured with ML/AI libraries, such as `nvidia/cuda` or frameworks like TensorFlow or PyTorch.
