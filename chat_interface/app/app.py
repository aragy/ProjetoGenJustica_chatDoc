import streamlit as st
import requests

# Configurar a URL do serviço com a nova porta
QA_PIPELINE_URL = "http://qa_pipeline_service:8100"

st.title("Interface Conversacional")

# Seção para upload de PDF
st.header("Upload de PDF")
uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{QA_PIPELINE_URL}/process_pdf/", files=files)
    if response.status_code == 200:
        st.success("PDF processado com sucesso!")
    else:
        st.error("Erro ao processar o PDF.")

# Seção para fazer perguntas
st.header("Faça uma Pergunta")
question = st.text_input("Digite sua pergunta:")

if st.button("Perguntar"):
    if question:
        response = requests.post(f"{QA_PIPELINE_URL}/ask_question/", json={"question": question})
        if response.status_code == 200:
            answer = response.json().get("answer", "Sem resposta disponível")
            st.write("Resposta:", answer)
        else:
            st.error("Erro ao obter resposta.")
    else:
        st.warning("Por favor, digite uma pergunta.")
