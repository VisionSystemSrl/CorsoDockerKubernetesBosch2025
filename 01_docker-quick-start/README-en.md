# Quick Start: Run a Generative AI App Using Docker

This guide explains how to run a Docker container for a Generative AI app using an image from Docker Hub. You'll also learn how to manage the lifecycle of the container (start, stop, restart, view logs, etc.).

## Step 1: Pull the Pre-Built Docker Image

We'll use a pre-built image from Docker Hub that provides a Generative AI API based on Hugging Face's GPT-2 model.

Run the following command to pull the image:

```bash
docker pull fabiovisionsystem/generative-ai-app:1.0
```

**Explanation**:
- `docker pull`: Downloads the Docker image from a registry (in this case, Docker Hub or GitHub Container Registry).
- `fabiovisionsystem/generative-ai-app:1.0`: The full name of the image, where:
  - `fabiovisionsystem/generative-ai-app`: The repository containing the image.
  - `1.0`: Specifies the version of the image.

## Step 2: Run the Docker Container

Start the container with the following command:

```bash
docker run -d -p 8080:8080 --name gpt2-app fabiovisionsystem/generative-ai-app:1.0
```

**Explanation**:
- `docker run`: Starts a new container.
- `-d`: Runs the container in detached mode (in the background).
- `-p 8080:8080`: Maps port 8080 on your machine to port 8080 in the container. This allows you to access the app locally.
- `--name gpt2-app`: Assigns a name (gpt2-app) to the container for easier management.
- `fabiovisionsystem/generative-ai-app:1.0`: Specifies the image to use.

After running this command, the Generative AI app is now running in a Docker container.

## Step 3: Test the Generative AI App

You can test the running app by sending a POST request to the API endpoint. Use curl or a tool like Postman.

**Using curl**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Once upon a time"}' http://localhost:8080/generate
```

**Expected Response**:
```json
{
 "generated_text": "Once upon a time, in a faraway kingdom, a young prince discovered an ancient treasure..."
}
```

## Managing the Container Lifecycle

Here are some common commands for managing the container lifecycle:

### 1. View Running Containers

To see a list of all running containers:
```bash
docker ps
```

### 2. Stop the Container

To stop the gpt2-app container:
```bash
docker stop gpt2-app
```

### 3. Restart the Container

To restart the gpt2-app container:
```bash
docker restart gpt2-app
```

### 4. View Logs

To see the logs for the gpt2-app container:
```bash
docker logs gpt2-app
```

### 5. Remove the Container

If you no longer need the container, stop it first and then remove it:
```bash
docker rm gpt2-app
```

### 6. Remove the Docker Image

If you want to clean up the image from your system:
```bash
docker rmi fabiovisionsystem/generative-ai-app:1.0
```