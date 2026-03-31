import streamlit as st

# Configuration de la page pour le responsive
st.set_page_config(page_title="Mon IA Chat", layout="centered")

st.title("🤖 Assistant IA")
st.caption("Application responsive exécutée via Python")

# Initialisation de la mémoire (session_state)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Salut ! Je suis ton IA. Tape quelque chose pour commencer."}
    ]

# Affichage fluide des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Zone de saisie (fixée en bas sur mobile et PC)
if prompt := st.chat_input("Écris ton message ici..."):
    
    # 1. Ajouter et afficher le message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Logique de l'IA (L'Echo pour l'instant)
    with st.chat_message("assistant"):
        response = f"Echo : {prompt}"
        st.markdown(response)
    
    # 3. Sauvegarder la réponse
    st.session_state.messages.append({"role": "assistant", "content": response})
