# Use uma imagem base com suporte a CUDA
FROM nvidia/cuda:12.0.1-runtime-ubuntu22.04

# Instalar pacotes essenciais e pip
RUN apt-get update && apt-get install -y \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Baixar o modelo Llama 3.1 com a rede host
RUN ollama serve & sleep 5 && ollama pull llama3.1

# Definir diretório de trabalho
WORKDIR /app

# Configurar a variável de ambiente para usar a GPU 0
ENV CUDA_VISIBLE_DEVICES=0

# A imagem estará pronta para servir como base para outras aplicações
