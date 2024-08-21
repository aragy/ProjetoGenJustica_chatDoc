# Use a imagem customizada como base
FROM custom_ollama_base

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt .

# Instalar as dependências adicionais necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY app/ ./app/

# Expor a porta necessária
EXPOSE 8100

# Comando para iniciar o serviço
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8100"]
