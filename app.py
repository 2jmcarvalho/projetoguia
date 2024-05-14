# projetoguia

import os
import streamlit as st
import sqlite3
import streamlit_authenticator as stauth

st.set_page_config(layout="wide")
st.title("Guaaia do Universitario🤓")

def register(username, password):
    with open("user_credentials.txt", "a") as file:
        file.write(f"{username}:{password}\n")

def login(username, password):
    with open("user_credentials.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                return True
    return False

def main():
    st.title("Login e Registro")

    username = st.text_input("Nome de usuário")
    password = st.text_input("Senha", type="password")


    if st.button("Registrar"):
        if len(username) == 0 or len(password) == 0:
            st.warning("Por favor, preencha todos os campos.")
        else:
            register(username, password)
            st.success("Registro realizado com sucesso. Você pode fazer login agora.")
    if st.button("Login"):
        if len(username) == 0 or len(password) == 0:
            st.warning("Por favor, preencha todos os campos.")
        else:
            if os.path.exists("user_credentials.txt"):
                if login(username, password):
                    st.success("Login bem-sucedido!")
                    st.empty()
                    next_page(username)  # Chamada para a próxima página após o login
                else:
                    st.error("Credenciais inválidas.")
            else:
                st.error("Nenhum usuário registrado. Por favor, registre-se primeiro.")


def next_page(username):
    st.title(f"Bem-vindo, {username}!")
    tab1, tab2, tab3 = st.tabs(["Inicio", "Créditos", "Monitoria(em breve)"])

    with tab1:
        st.subheader("canais recomendados")
        
        st.subheader("videos recomendados")



    with tab2:
        col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.header("A Crara")
        st.image("./img/clara.jpeg", width=200 )
        st.link_button("Github", "https://github.com/CraraMaria")
    
    with col2:
        st.header("JohnK")
        st.image("./img/johnk.jpeg", width=200)
        st.link_button("Github", "https://github.com/2jmcarvalho")

    with col3:
        st.header("Ana")
        st.image("./img/ana.jpeg", width=200)
        st.link_button("Github", "https://gist.github.com/AnaSouza-Dev")

    with col4:
        st.header("kore")
        st.image("./img/kore.jpeg", width=200)
        st.link_button("Github", "https://github.com/AnaKanashiro")

    with col5:
        st.header("Tutu")
        st.image("./img/tutu.png", width=200)
        st.link_button("Github", "https://github.com/TutsXD1")
        

    


if __name__ == "__main__":
    main()
