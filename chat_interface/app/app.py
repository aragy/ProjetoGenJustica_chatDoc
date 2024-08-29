import streamlit as st
import requests


QA_PIPELINE_URL = "http://qa_pipeline_service:8100"


st.set_page_config(page_title="Interface Conversacional", page_icon=":speech_balloon:")


st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: center; border-bottom: 2px solid red; padding: 10px; background-color: white;">
        <img src="https://www.tjms.jus.br/storage/cms-arquivos/3a9585dff89cf61ef2256f1db0b6ddd1.png" alt="TJMS" style="height: 60px; margin-right: 20px;">
        <h3 style="color: black; margin: 0;">Tribunal de Justiça de Mato Grosso do Sul</h3>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        color: black;  
    }
    .stMarkdown h2, .stMarkdown h1, .stMarkdown h3 {
        color: black;  
        border-bottom: 2px solid red;
        padding-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


if 'pdf_uploaded' not in st.session_state:
    st.session_state['pdf_uploaded'] = False

st.title("Interface Conversacional")


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
   
    st.header("Conversacional")
    
    
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    
    
    for chat in st.session_state['chat_history']:
        st.write(chat)
    
   
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
