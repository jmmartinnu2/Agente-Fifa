import streamlit as st
import pandas as pd
import smtplib
from email.message import EmailMessage

try:
    usuarios = pd.read_csv('usuarios.csv')
except FileNotFoundError:
    usuarios = pd.DataFrame(columns=['Username', 'Password'])
    usuarios.to_csv('usuarios.csv', index=False)

# Resto del código...

def registro():
    global usuarios  # Indica que la variable usuarios es global
    st.subheader("Registro")
    username = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")
    confirm_password = st.text_input("Confirmar Contraseña", type="password")

    if st.button("Registrar"):
        if password == confirm_password:
            if username in usuarios['Username'].values:
                st.error("El usuario ya está registrado.")
            else:
                nuevo_usuario = pd.DataFrame({'Username': [username], 'Password': [password]})
                usuarios = usuarios.append(nuevo_usuario, ignore_index=True)
                usuarios.to_csv('usuarios.csv', index=False)
                st.success("Usuario registrado correctamente.")
                send_email(username)  # Enviar correo electrónico al registrar un nuevo usuario
        else:
            st.error("Las contraseñas no coinciden.")


def login():
    st.subheader("Inicio de Sesión")
    username = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar Sesión"):
        usuarios = pd.read_csv('usuarios.csv')
        login_valido = ((usuarios['Username'] == username) & (usuarios['Password'] == password)).any()

        if login_valido:
            st.success("¡Inicio de sesión exitoso!")
            return True
        else:
            st.error("Nombre de usuario o contraseña incorrectos.")
            return False

def main():
    st.title("Sistema de Login y Registro")

    if 'username' not in st.session_state:
        page = st.sidebar.selectbox("Selecciona una opción", ["Login", "Registro"])

        if page == "Login":
            if login():
                st.session_state['username'] = st.text_input("Nombre de usuario")
        elif page == "Registro":
            registro()
    else:
        st.write(f"Bienvenido, {st.session_state['username']}")

if __name__ == "__main__":
    main()
