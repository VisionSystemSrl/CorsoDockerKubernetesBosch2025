# How to Build and Run the Generative AI App with Docker

This guide explains how to build and run a Dockerized Generative AI app that uses Hugging Face's transformers library and a Flask API.

## Step 1: Prepare Your Files

Ensure the following directory structure and files are present:

```
generative-ai-app/
├── app.py
├── requirements.txt
└── Dockerfile
```

**File Descriptions**:
- `app.py`: Python application code that sets up a Flask API and uses Hugging Face's transformers library for text generation.
- `requirements.txt`: Lists all the Python dependencies needed to run the application.
- `Dockerfile`: Defines the steps to create a Docker image for the app.

## Step 2: Build the Docker Image

Run the following command in your terminal from the generative-ai-app directory:

```bash
docker build -t generative-ai-app:1.0 .
```

**Explanation**:
- `docker build`: The command to build a Docker image.
- `-t generative-ai-app:1.0`: Tags the image with the name generative-ai-app and version 1.0.
- `.`: Specifies the current directory as the build context.

## Step 3: Run the Docker Container

Run the container using the built image:

```bash
docker run -d -p 8080:8080 --name generative-app generative-ai-app:1.0
```

**Explanation**:
- `docker run`: Starts a new container.
- `-d`: Runs the container in detached mode (in the background).
- `-p 8080:8080`: Maps port 8080 on your machine to port 8080 in the container.
- `--name generative-app`: Assigns the container a name (generative-app).
- `generative-ai-app:1.0`: Specifies the Docker image to use.

## Step 4: Test the App

Test the running app by sending a POST request to the API endpoint. You can use curl or a tool like Postman.

**Using curl**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Once upon a time"}' http://localhost:8080/generate
```

**Expected Response**:
```json
[
 {
 "generated_text": "Once upon a time, in a faraway land, there lived a wise old king..."
 }
]
```

## Step 5: Monitor Resource Usage
You can monitor the resource usage (CPU, memory, etc.) of your container with the following command:
```
docker stats
```

**Description**:
- `docker stats`: Displays real-time resource usage of all running containers. You can identify the desired container by its name or ID.

## Step 6: Stop and Remove the Container

Stop the container when you're finished:

```bash
docker stop generative-app
```

Remove the container:

```bash
docker rm generative-app
```

## Step 7: Deploy the Docker Image to Docker Hub

You can share your Docker image by deploying it to Docker Hub.

### 1. Log In to Docker Hub

Run the following command and enter your Docker Hub credentials:

```bash
docker login
```

### 2. Tag the Image

Tag your image with your Docker Hub username and desired repository name:

```bash
docker tag generative-ai-app:1.0 <your-dockerhub-username>/generative-ai-app:1.0
```

**Example**:

```bash
docker tag generative-ai-app:1.0 johndoe/generative-ai-app:1.0
```

### 3. Push the Image to Docker Hub

Push the tagged image to Docker Hub:

```bash
docker push <your-dockerhub-username>/generative-ai-app:1.0
```

**Example**:

```bash
docker push johndoe/generative-ai-app:1.0
```

After the push is complete, your image will be available on Docker Hub under your account.

### 4. Verify the Image on Docker Hub

Log in to Docker Hub via the website and check your repositories to ensure the image is listed.

## Additional Notes

- If you need to rebuild the image after making changes to the code or Dockerfile, re-run the `docker build` command.
- To check running containers, use:
  ```bash
  docker ps
  ```
- To view logs from the running container, use:
  ```bash
  docker logs generative-app
  ```