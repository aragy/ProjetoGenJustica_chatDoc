
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 8601

CMD ["streamlit", "run", "app/app.py", "--server.port", "8601", "--server.address", "0.0.0.0"]
