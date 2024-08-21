# ProjetoGenJustica_chatDoc

**ProjetoGenJustica_chatDoc** is a Proof of Concept (POC) modularized AI-powered solution that allows for processing PDFs, generating embeddings, and performing question-answering tasks over legal documents using advanced machine learning models.
## Project Structure

   - `qa_pipeline_service`: Handles the processing of PDFs, generating embeddings, and performing vector-based searches.
   - `chat_interface`: A Streamlit-based interface for interacting with the services.

## Requirements

   - Docker
   - NVIDIA GPU with drivers and CUDA installed
   - Python 3.10 (for local development)

## Getting Started
1. Clone the Repository


```bash
git clone git@github.com:aragy/ProjetoGenJustica_chatDoc.git
cd ProjetoGenJustica_chatDoc
```

2. Set Up Environment

Ensure your environment variables are correctly set up. Use a .env file if necessary.

3. Build the `custom_ollama_base` Image

To create the custom_ollama_base image, navigate to the project root directory where the Dockerfile is located and run:

```bash
sudo docker build -t custom_ollama_base -f Dockerfile .
```

4. Build and Run Docker Containers

Build the containers and start the services:


```bash
sudo docker-compose up --build
```
5. Start the Ollama Service
Access the qa_pipeline_service container via terminal and start the Ollama service:

```bash
sudo docker exec -it qa_pipeline_service bash
ollama serve
```

6. Access the Application

  -  QA Pipeline Service: Available on http://localhost:8100
  -  Chat Interface: Accessible via http://localhost:8601

7. Stopping the Services

To stop the services, run:


```bash
sudo docker-compose down

```
## Usage

   - Upload a PDF via the chat interface.
   - Ask questions related to the content of the PDF.
   - Receive contextual answers from the trained model.

## Customization

   - Model Weights: The project uses custom model weights. Ensure that these are correctly downloaded and placed in the appropriate directory.
   - GPU Allocation: Modify the docker-compose.yml file to specify GPU allocation.

## Troubleshooting

   - Ensure your GPU is correctly configured and accessible by Docker.
   - Verify internet connectivity if models fail to download.


## License

This project is licensed under the MIT License.