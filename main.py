import streamlit as st
from random import sample
from preguntas import preguntas
import time

# Función para inicializar o resetear la sesión
def iniciar_sesion():
    return {
        'preguntas': [],
        'realizado_test': False,
    }

def mostrar_examen():
    st.title("Test de 20 preguntas")
    st.write("Responde las siguientes preguntas:")

    # Obtener la sesión actual o inicializarla si es la primera vez
    sesion = st.session_state.get('sesion', None)
    if sesion is None:
        sesion = iniciar_sesion()

    puntaje = 0
    respuestas_usuario = {}

    # Obtener las preguntas si no se ha realizado el test
    if not sesion['realizado_test']:
        sesion['preguntas'] = sample(preguntas, 20)

    for i, pregunta in enumerate(sesion['preguntas'], 1):
        pregunta_texto = pregunta['pregunta']
        opciones = pregunta['opciones']
        respuesta_correcta = pregunta['respuesta_correcta']

        st.write(f"{i}. {pregunta_texto}")

        # Generar una clave única basada en el índice de la pregunta
        key = f"pregunta_{i}_respuestas"

        respuesta_usuario = st.radio(f"Selecciona una respuesta: ", ['', *opciones], key=key)

        # Mostrar retroalimentación sobre la respuesta
        if respuesta_usuario == respuesta_correcta:
            st.success("¡Respuesta correcta!")
            puntaje += 5
        elif respuesta_usuario:
            st.error("Respuesta incorrecta")

        # Guardar la respuesta del usuario si se ha seleccionado alguna opción
        if respuesta_usuario:
            respuestas_usuario[pregunta_texto] = respuesta_usuario

    st.write(f"Tu puntaje total es: {puntaje}/100")

    if puntaje >= 75:
        st.success("¡Felicidades! ¡Has aprobado!")
    else:
        st.error("Lo siento, no has alcanzado el puntaje mínimo para aprobar.")

    # Marcar que se ha realizado el test
    sesion['realizado_test'] = True

    # Actualizar la sesión
    st.session_state['sesion'] = sesion
    


def main():
    tabs = ["Examenes", "Resumenes", "Esquemas", "Temario"]  # Nuevas secciones
    tab_select = st.sidebar.selectbox("Selecciona una sección", tabs, index=0)

    if tab_select == "Examenes":
        if st.button("Realizar otro examen"):
            # Borrar el contenido anterior antes de iniciar un nuevo examen
            st.session_state['sesion'] = iniciar_sesion()
            st.experimental_rerun()       
    
        mostrar_examen()
    elif tab_select == "Resumenes":
        # Título y resumen para cada sección
        secciones = [
            {
                "titulo": "Estatutos FIFA",
                "resumen": "Texto resumen..."
            },
            {
                "titulo": "Código Disciplinario",
                "resumen": "Texto resumen..."
            },
            {
                "titulo": "Codigo de Etica",
                "resumen": "Texto resumen..."
            },
            {
                "titulo": "Reglamento sobre el Estatuto y la Transferencia de jugadores",
                "resumen": "Texto resumen..."
            },
            {
                "titulo": " Reglamento de procedimiento del Tribunal del Fútbol",
                "resumen": "Texto resumen..."
            },
            {
                "titulo": "Reglamento de la Cámara de Compensación",
                "resumen": "Texto resumen..."
            },
            {
                "titulo": "Reglamento sobre Agente Fifa",
                "resumen": "Texto resumen..."
            },
            {
                "titulo": "Herramientas de Salvaguardia de la infancia del programa FIFA Guardians",
                "resumen": "Texto resumen..."
            },                        
        ]

        # Iterar sobre cada sección y mostrar el título y el resumen
        for seccion in secciones:
            titulo = seccion["titulo"]
            resumen = seccion["resumen"]

            st.subheader(titulo)  # Título de la sección
            st.markdown(resumen)  # Resumen de la sección en formato markdown
                
                
    elif tab_select == "Esquemas":
        st.write("Contenido de la sección Esquemas")
        # Agrega el contenido que desees para la sección Esquemas
    elif tab_select == "Temario":
        st.title("Temario Examen Agente FIFA")
        pdf_url = "https://digitalhub.fifa.com/m/1009119579a8c8c4/original/Materiales-de-estudio-sobre-el-examen-de-la-FIFA-para-agentes-de-futbol.pdf"
        st.markdown(f'<iframe src="{pdf_url}" width="100%" height="1000" style="border: none;"></iframe>', unsafe_allow_html=True)   



if __name__ == "__main__":
    main()
