import streamlit as st
from random import sample
from preguntas import preguntas
from resumenes import mostrar_resumenes  # Importa la función desde resumenes.py
import time
from login import login, registro
from contratos import generar_contrato_segun_tipo
import matplotlib.pyplot as plt
from pyvis.network import Network
from examen_fifa import preguntas_fifa
import random



# Función para inicializar o resetear la sesión
def iniciar_sesion():
    return {
        'preguntas': [],
        'realizado_test': False,
    }



#Examenes 
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



#Videos de clases    
def mostrar_videos():
    st.title("Videos y Recursos Multimedia")
    st.write("Aquí encontrarás videos explicativos y recursos multimedia relacionados con el examen de FIFA.")

    # Lista de diccionarios con información sobre cada video
    videos = [
        {
            "clase": "Clase 1",
            "titulo": "Clase 1 - RFAF",
            "url": "https://youtu.be/mR3uhngzdnE"
        },
        {
            "clase": "Clase 2",
            "titulo": "Clase 2 - RFAF",
            "url": "https://youtu.be/RiYmZmLpaCU"
        },
        {
            "clase": "Clase 3",
            "titulo": "Clase 3 - RFAF",
            "url": "https://youtu.be/ROqi547z9Ng"
        },
        {
            "clase": "Clase 4",
            "titulo": "Clase 4 - RFAF",
            "url": "https://youtu.be/l0xXxcSUJqw"
        },
        {
            "clase": "Clase 5",
            "titulo": "Clase 5 - RFAF",
            "url": "https://youtu.be/921ggJ_gj4U"
        },
        {
            "clase": "Clase 6",
            "titulo": "Clase 6 - Examen Fifa sobre RFAF",
            "url": "https://youtu.be/aCo78ZSk7d4"
        },
        {
            "clase": "Clase 7",
            "titulo": "Clase 7 - RTIJ I",
            "url": "https://www.youtube.com/watch?v=nOJoeyhTCsc"
        },
        {
            "clase": "Clase 8",
            "titulo": "Clase 8 - RTIJ II",
            "url": "https://youtu.be/xKhvt-j48jQ"
        },
        {
            "clase": "Clase 9",
            "titulo": "Clase 9 - RTIJ III",
            "url": "https://www.youtube.com/watch?v=bySK5jUz7jk"
        },
        {
            "clase": "Clase 10",
            "titulo": "Clase 10 - RTIJ IV",
            "url": "https://youtu.be/lXjRsBjS7cQ"
        },
        {
            "clase": "Clase 11",
            "titulo": "Clase 11 - RTIJ V",
            "url": "https://www.youtube.com/watch?v=Yv-tBD6x_l8"
        },
        {
            "clase": "Clase 12",
            "titulo": "Clase 12 - RTIJ VI",
            "url": "https://youtu.be/EhN4OEU2kXY"
        },                                                            
    ]

    # Obtener las clases únicas para el selectbox
    clases_disponibles = list(set(video["clase"] for video in videos))
    clases_a_mostrar = [clase for clase in clases_disponibles if clase not in ["Clase 1", "Clase 2", "Clase 3", "Clase 4", "Clase 5", "Clase 6", "Clase 7", "Clase 8", "Clase 9", "Clase 10", "Clase 11", "Clase 12"]]

    # Crear la lista de opciones del selectbox
    opciones_clases = ["Ver todo"] + clases_a_mostrar + [f"Video {i+1}" for i in range(len(videos))]
    opcion_elegida = st.selectbox("¿Qué video deseas ver?", opciones_clases)

    # Mostrar videos según la opción seleccionada
    if opcion_elegida == "Ver todo":
        for video in videos:
            st.subheader(video["titulo"])
            st.video(video["url"])
    elif opcion_elegida in clases_a_mostrar:
        for video in videos:
            if video["clase"] == opcion_elegida:
                st.subheader(video["titulo"])
                st.video(video["url"])
    else:
        # Obtener el índice del video seleccionado
        index = int(opcion_elegida.split(" ")[1]) - 1
        st.subheader(videos[index]["titulo"])
        st.video(videos[index]["url"])



#Contratos generados
def generar_contrato():
    st.title("Generador de Contratos")

    nombre_cliente = st.text_input("Nombre del Cliente")
    direccion = st.text_input("Dirección")
    nombre_agente = st.text_input("Nombre del Agente FIFA")
    numero_licencia = st.text_input("Número de Licencia")
    duracion_acuerdo = st.number_input("Duración del acuerdo")

    tipo_contrato = st.selectbox(
        "Selecciona el tipo de contrato",
        [
            "Contrato de Representación",
            "Contrato de Servicios",
            "Contrato de Asesoramiento",
            "Contrato de Comisión"
        ]
    )

    if st.button("Generar Contrato"):
        contrato = generar_contrato_segun_tipo(nombre_cliente, direccion, nombre_agente, numero_licencia, tipo_contrato, duracion_acuerdo)
        st.subheader("Contrato Generado:")
        st.text_area("Contrato", contrato, height=400)
      
    
#Calculadora
def calcular_comision():
    st.title("Calculadora de Comisiones")

    tipos_clientes = [
        "Persona", 
        "Entidad de destino",
        "Entidad de origen", 
        "Doble representación (Persona y Entidad de destino)"
    ]
    tipo_cliente = st.selectbox("Tipo de cliente:", tipos_clientes)

    comision_primer_tramo = 0
    comision_segundo_tramo = 0
    comision_total = 0

    if tipo_cliente == "Doble representación (Persona y Entidad de destino)":
        valor_transferencia = st.number_input("Valor total de la transferencia en USD:", min_value=0.0, step=0.01)

        if valor_transferencia <= 200000:
            st.subheader("Elige el porcentaje negociado")
            comision_menor = st.number_input("Comisión (0% - 10%):", min_value=0, max_value=10, value=10)
            comision_primer_tramo = valor_transferencia * (comision_menor / 100)
        else:
            st.subheader("Elige el porcentaje negociado")
            comision_menor = st.number_input("Comisión (0% - 10%):", min_value=0, max_value=10, value=10)
            comision_hasta_200k = 200000 * (comision_menor / 100)
            
            excedente = valor_transferencia - 200000
            comision_despues_200k = st.number_input("Comisión después de $200,000 (0% - 6%):", min_value=0, max_value=6, value=6)
            comision_excedente = excedente * (comision_despues_200k / 100)
            
            comision_primer_tramo = comision_hasta_200k
            comision_segundo_tramo = comision_excedente
        
        comision_total = comision_primer_tramo + comision_segundo_tramo

    elif tipo_cliente in ["Persona", "Entidad de destino"]:
        valor_transferencia = st.number_input("Remuneración Anual de la Persona en USD (No incluir pagos variables):", min_value=0.0, step=0.01)

        if valor_transferencia <= 200000:
            st.subheader("Elige el porcentaje negociado")
            comision_menor = st.number_input("Comisión (0% - 5%):", min_value=0, max_value=5, value=5)
            comision_primer_tramo = valor_transferencia * (comision_menor / 100)
        else:
            st.subheader("Elige el porcentaje negociado")
            comision_menor = st.number_input("Comisión (0% - 5%):", min_value=0, max_value=5, value=5)
            comision_despues_200k = st.number_input("Comisión después de $200,000 (0% - 3%):", min_value=0, max_value=3, value=3)
            
            comision_hasta_200k = 200000 * (comision_menor / 100)
            excedente = valor_transferencia - 200000
            comision_excedente = excedente * (comision_despues_200k / 100)
            
            comision_primer_tramo = comision_hasta_200k
            comision_segundo_tramo = comision_excedente
        
        comision_total = comision_primer_tramo + comision_segundo_tramo

    elif tipo_cliente == "Entidad de origen":
        monto_indemnizacion = st.number_input("Monto de la Indemnización por Transferencia en USD:", min_value=0.0, step=0.01)
        st.subheader("Elige el porcentaje negociado")
        porcentaje_comision = st.number_input("Porcentaje de comisión (0% - 10%):", min_value=0, max_value=10, value=10)
        comision_total = monto_indemnizacion * (porcentaje_comision / 100)

    if st.button("Calcular"):
        if tipo_cliente == "Doble representación (Persona y Entidad de destino)":
            if valor_transferencia <= 200000:
                st.write(f"Comisión del primer tramo (0% - 10%): {comision_primer_tramo} USD")
            else:
                st.write(f"Comisión del primer tramo (0% - 10%): {comision_primer_tramo} USD")
                if comision_segundo_tramo > 0:
                    st.write(f"Comisión del segundo tramo (0% - 6%): {comision_segundo_tramo} USD")
        else:
            if tipo_cliente != "Entidad de origen":
                st.write(f"Comisión del primer tramo (0% - 5%): {comision_primer_tramo} USD")
            if comision_segundo_tramo > 0:
                st.write(f"Comisión del segundo tramo (0% - 3%): {comision_segundo_tramo} USD")
        if comision_total > 0:
            st.write(f"Comisión total: {comision_total} USD")

        if tipo_cliente != "Entidad de origen":
                    comision_efectiva = comision_total / valor_transferencia
                    st.write(f"Comisión efectiva: {comision_efectiva:.2%}")           
#Calculadora variables
def calcular_pagos_variables():
    st.title("Calculadora de Pagos Variables")

    tasa_efectiva = st.number_input("Tasa efectiva (%):", min_value=0.0, step=0.01)
    pagos_variables = st.number_input("Pagos variables (en USD):", min_value=0.0, step=0.01)

    if st.button("Calcular pagos", key="calcular_pagos"):
        cantidad_cobrada = pagos_variables * (tasa_efectiva / 100)
        st.write(f"El agente cobrará por pagos variables: {cantidad_cobrada:.2f} USD")


        
#Esquemas
def mostrar_jerarquia_fifa():
    # Crear un objeto Network
    network = Network(height="750px", width="100%", notebook=True)

    # Agregar nodos
    nodos = [
        ('Órganos', 'Congreso'),
        ('Órganos', 'Consejo'),
        ('Órganos', 'Presidente'),
        ('Órganos', 'Secretaría General'),
        ('Órganos', 'Bureau del Consejo'),
        ('Órganos', 'Comisiones Permanentes'),
        ('Comisiones Permanentes', 'Comisión de Finanzas'),
        ('Comisiones Permanentes', 'Comisión de Desarrollo'),
        ('Comisiones Permanentes', 'Comisión Organizadora de Competiciones de la FIFA'),
        ('Comisiones Permanentes', 'Comisión de Grupos de Interés del Fútbol'),
        ('Comisiones Permanentes', 'Comisión de Federaciones Miembro'),
        ('Comisiones Permanentes', 'Comisión de Árbitros'),
        ('Comisiones Permanentes', 'Comisión de Medicina')
    ]

    for parent, child in nodos:
        network.add_node(parent, parent, title=parent)
        network.add_node(child, child, title=child)
        network.add_edge(parent, child)

    # Mostrar la red
    network.show("fifa_hierarchy_organs_updated.html")
    st.components.v1.html(open("fifa_hierarchy_organs_updated.html").read(), height=900)
         


#Examen oficial fifa test
def mostrar_examen_fifa():
    st.title("Examen Oficial FIFA")
    st.write("Responde las siguientes preguntas:")

    sesion = st.session_state.get('sesion', None)
    if sesion is None:
        sesion = iniciar_sesion()

    puntaje = 0
    respuestas_usuario = {}

    for i, pregunta in enumerate(sesion['preguntas_fifa'], 1):
        pregunta_texto = pregunta['pregunta']
        opciones = pregunta['opciones']

        st.write(f"{i}. {pregunta_texto}")  # Muestra la pregunta

        # Muestra las opciones de respuesta como botones de radio
        respuesta_usuario = st.radio(f"Respuesta {i}", opciones)
        respuestas_usuario[i] = respuesta_usuario

    st.write(respuestas_usuario)  # Muestra las respuestas seleccionadas por el usuario



#Funcion Ventanas de mercado calendarios
def ventana_mercado(pdf_url):
    st.title("Ventanas de mercados")
    st.markdown(f'<iframe src="{pdf_url}" width="100%" height="600px" style="border: none;"></iframe>', unsafe_allow_html=True)




#Visualizacion
def main():
    tabs = ["Examenes", "Resumenes", "Esquemas", "Temario", "Videos", "Contratos", "Calculadora", "Examen oficial FIFA", "Ventanas de fichajes"]  # Nuevas secciones
    tab_select = st.sidebar.selectbox("Selecciona una sección", tabs, index=0)

    if tab_select == "Examenes":
        if st.button("Realizar otro examen"):
            # Borrar el contenido anterior antes de iniciar un nuevo examen
            st.session_state['sesion'] = iniciar_sesion()
            st.experimental_rerun()       
    
        mostrar_examen()
    elif tab_select == "Resumenes":
        mostrar_resumenes()  # Llama a la función desde resumenes.py para mostrar los resúmenes
                
                
    elif tab_select == "Esquemas":
        st.title('Jerarquía FIFA')
        mostrar_jerarquia_fifa()
        
    elif tab_select == "Temario":
        st.title("Temario Examen Agente FIFA")
        pdf_url = "https://digitalhub.fifa.com/m/1009119579a8c8c4/original/Materiales-de-estudio-sobre-el-examen-de-la-FIFA-para-agentes-de-futbol.pdf"
        st.markdown(f'<iframe src="{pdf_url}" width="100%" height="1000" style="border: none;"></iframe>', unsafe_allow_html=True)   
        
    elif tab_select == "Videos":
        mostrar_videos()  # Llama a la función para mostrar los videos

    elif tab_select == "Contratos":
        generar_contrato()

        
    elif tab_select == "Calculadora":
        calcular_comision() 
        calcular_pagos_variables()

    elif tab_select == "Examen oficial FIFA":
        mostrar_examen_fifa()

    elif tab_select == "Ventanas de fichajes":
        # Llamada a la función con la URL
        pdf_url_ejemplo = "https://digitalhub.fifa.com/m/680099dc838c2961/original/Transfer-Window-Calendar_MFA_S_20211201.pdf"
        ventana_mercado(pdf_url_ejemplo)

if __name__ == "__main__":
    main()
