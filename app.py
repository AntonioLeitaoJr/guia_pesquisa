import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Redirecionando...", layout="centered")

# Mensagem visual ao usuário
st.markdown("""
    <div style="text-align:center; padding:40px;">
        <h2 style="color:#ff914d;">🔄 Redirecionando para a pesquisa...</h2>
        <p>Se isso não acontecer em alguns segundos, 
        <a href="https://guiaairbnbleitao.streamlit.app/?pesquisa=sim">
        clique aqui</a>.</p>
    </div>
""", unsafe_allow_html=True)

# Redirecionamento automático via JavaScript
components.html("""
    <script>
        window.location.replace("https://guiaairbnbleitao.streamlit.app/?pesquisa=sim");
    </script>
""", height=0)

