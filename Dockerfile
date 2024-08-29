
FROM nvidia/cuda:12.0.1-runtime-ubuntu22.04


RUN apt-get update && apt-get install -y \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*


RUN curl -fsSL https://ollama.com/install.sh | sh


RUN ollama serve & sleep 5 && ollama pull llama3.1


WORKDIR /app


ENV CUDA_VISIBLE_DEVICES=0


