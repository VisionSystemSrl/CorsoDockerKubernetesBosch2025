# Step 1: Use a base image
# A lightweight Python image is chosen for this example
FROM python:3.9-slim

# Step 2: Set build-time arguments (optional but useful for customization)
# ARG is used to define variables that can be overridden during the build process
ARG APP_VERSION=1.0

# Step 3: Set environment variables (useful for runtime configurations)
# ENV defines variables that the app can use during runtime
ENV APP_ENV=production \
    APP_VERSION=${APP_VERSION}

# Step 4: Set a working directory inside the container
# WORKDIR ensures all commands (e.g., copy, install) happen in this directory
WORKDIR /app

# Step 5: Copy application code into the container
# COPY <source> <destination>
# Copies everything in the current directory (.) into /app in the container
COPY . /app

# Step 6: Install dependencies
# Use RUN to execute shell commands inside the container at build time
RUN pip install --no-cache-dir -r requirements.txt

# Step 7: Expose a port (optional)
# EXPOSE makes a port accessible for networking (used here for the web server)
EXPOSE 8080

# Step 8: Specify the command to run the application
# CMD defines the default command to run when the container starts
CMD ["python", "app.py"]

# Step 9: Add metadata to the image
# Labels can provide useful metadata about the image
LABEL maintainer="Your Name <your.email@example.com>" \
      version=${APP_VERSION} \
      description="Generative AI text generation app using Hugging Face models."
