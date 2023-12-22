import streamlit as st
import time

def verificar_sesion(contraseña_correcta):
    session_start_time = st.session_state.get("session_start_time")

    if not session_start_time:
        st.session_state.logged_in = False
        st.session_state.session_start_time = time.time()

    def obtener_estado_sesion():
        return st.session_state.logged_in

    def guardar_estado_sesion(estado):
        st.session_state.logged_in = estado

    def actualizar_tiempo_sesion():
        st.session_state.session_start_time = time.time()

    # Verificar el estado de la sesión
    session_state = obtener_estado_sesion()

    if not session_state:
        contraseña = st.text_input("Ingrese la contraseña", type="password")
        if not contraseña:  # Si no se ha ingresado ninguna contraseña
            st.warning("Por favor, ingrese una contraseña.")
        else:
            if contraseña == contraseña_correcta:
                guardar_estado_sesion(True)
                actualizar_tiempo_sesion()
            else:
                st.error("Contraseña incorrecta. Acceso denegado.")

    if session_state and time.time() - st.session_state.session_start_time > 60 * 60:  # 60 minutos
        st.session_state.logged_in = False

    return st.session_state.logged_in
