FROM ollama/ollama:latest

# Copy a script that will pull the model and start ollama
COPY init.sh /init.sh
RUN chmod +x /init.sh

# Pull the model during build
RUN ollama serve & \
    sleep 5 && \
    ollama pull qwen2.5:1.5b && \
    pkill ollama

# Install nvtop
RUN apt-get update && apt-get install -y nvtop

EXPOSE 11434

ENTRYPOINT ["/init.sh"]