# Use a imagem base do Python com suporte a Streamlit
FROM python:3.11-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY app/ ./app/

# Expor a porta necessária
EXPOSE 8601

# Comando para iniciar o Streamlit
CMD ["streamlit", "run", "app/app.py", "--server.port", "8601", "--server.address", "0.0.0.0"]
