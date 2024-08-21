import streamlit as st
import requests

# Configurar a URL do serviço com a nova porta
QA_PIPELINE_URL = "http://qa_pipeline_service:8100"

# Gerenciar o estado da interface
if 'pdf_uploaded' not in st.session_state:
    st.session_state['pdf_uploaded'] = False

st.title("Interface Conversacional")

# Seção para upload de PDF
if not st.session_state['pdf_uploaded']:
    st.header("Upload de PDF")
    uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

    if uploaded_file is not None:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(f"{QA_PIPELINE_URL}/process_pdf/", files=files)
        if response.status_code == 200:
            st.session_state['pdf_uploaded'] = True
            st.success("PDF processado com sucesso!")
            st.rerun()
        else:
            st.error("Erro ao processar o PDF.")
else:
    # Interface Conversacional
    st.header("Conversacional")
    
    # Área de chat com histórico
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    
    # Exibir o histórico de chat
    for chat in st.session_state['chat_history']:
        st.write(chat)
    
    # Seção para fazer perguntas
    question = st.text_input("Digite sua pergunta:")

    if st.button("Perguntar"):
        if question:
            response = requests.post(f"{QA_PIPELINE_URL}/ask_question/", json={"question": question})
            if response.status_code == 200:
                answer = response.json().get("answer", "Sem resposta disponível")
                st.session_state['chat_history'].append(f"Você: {question}")
                st.session_state['chat_history'].append(f"Sistema: {answer}")
                st.rerun()
            else:
                st.error("Erro ao obter resposta.")
        else:
            st.warning("Por favor, digite uma pergunta.")
