import streamlit as st
from random import sample
from preguntas import preguntas
from resumenes import mostrar_resumenes  # Importa la función desde resumenes.py
from videos import get_videos
from examen_fifa import preguntas_agente_fifa, preguntas_estatuto_transferencia,preguntas_codigo_disciplinario,preguntas_estatutos_fifa,preguntas_salvaguardia
from esquemas import esquema_formacion,confederacion_afc,confederacion_caf,confederacion_concacaf,confederacion_conmebol,confederacion_ofc,confederacion_uefa
from login import verificar_sesion





contraseña_correcta = "12345"

session_state = verificar_sesion(contraseña_correcta)

if session_state:

    # Aquí va todo el contenido del tablero




    # Función para inicializar o resetear la sesión
    def iniciar_sesion():
        return {
            'preguntas': [],
            'realizado_test': False,
        }


    #Mostrar Inicio Readme
    def mostrar_inicio():
        st.title(":soccer: Tablero de Estudio ")

        st.write("""
        Este tablero ha sido creado para estudiar y revisar materiales relevantes relacionados con la preparación para el examen a Agente FIFA.
        Proporciona acceso a resúmenes, documentos oficiales, exámenes, videos y más.

        ## :mortar_board: Secciones Disponibles:
        - **📝 Examenes**: Realiza exámenes relacionados con la temática FIFA, tipo test.
        - **:book: Resúmenes**: Encuentra resúmenes organizados por temática.
        - **📚 Temario**: Acceso a documentos y materiales de estudio.
        - **:clapper: Videos**: Recopilación de videos educativos y explicativos de las clases impartidas.
        - **:heavy_division_sign: Calculadora**: Calculadora para realizar cálculos sobre Comsiones entre los distintos participantes.
        - **:dart: Exámenes Oficiales FIFA**: Preguntas oficiales sobre exámenes de la FIFA ya realizados.
        """)


    #Examenes tipo test 1 respuesta
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

            st.markdown(f"##### Pregunta {i}: {pregunta_texto}")  # Formato un poco más pequeño para la pregunta

            # Generar una clave única basada en el índice de la pregunta
            key = f"pregunta_{i}_respuestas"

            respuesta_usuario = st.radio(f"", ['', *opciones], key=key)

            # Mostrar retroalimentación sobre la respuesta
            if respuesta_usuario == respuesta_correcta:
                st.success("¡Respuesta correcta!")
                puntaje += 5
            elif respuesta_usuario:
                st.error("Respuesta incorrecta")

            # Guardar la respuesta del usuario si se ha seleccionado alguna opción
            if respuesta_usuario:
                respuestas_usuario[pregunta_texto] = respuesta_usuario

            st.markdown("---")  # Línea horizontal para separar preguntas

        st.write(f"Tu puntaje total es: {puntaje}/100")

        if puntaje >= 75:
            st.success("¡Felicidades! ¡Has aprobado!")
        else:
            st.error("Lo siento, no has alcanzado el puntaje mínimo para aprobar.")

        # Marcar que se ha realizado el test
        sesion['realizado_test'] = True

        # Actualizar la sesión
        st.session_state['sesion'] = sesion



    def mostrar_pdf_seleccionado():
        st.title("Selección y visualización de PDF")

        nombres_archivos = {
            "Estatutos de la FIFA": {
                "Páginas": (6, 105)
            },
            "Código Disciplinario de la FIFA": {
                "Páginas": (106, 160)
            },
            "Código de Ética de la FIFA": {
                "Páginas": (161, 208)
            },
            "Reglamento sobre el Estatuto y la Transferencia de Jugadores": {
                "Páginas": (209, 309)
            },
            "Reglamento de procedimiento del Tribunal del Fútbol": {
                "Páginas": (310, 343)
            },
            "Reglamento de la Cámara de Compensación de la FIFA": {
                "Páginas": (344, 379)
            },
            "Reglamento de la FIFA sobre Agentes de fútbol": {
                "Páginas": (380, 420)
            }
        }

        tema_seleccionado = st.selectbox("Selecciona un tema", list(nombres_archivos.keys()))

        if tema_seleccionado:
            inicio_pagina, _ = nombres_archivos[tema_seleccionado]["Páginas"]
            
            st.write(f"Visualización de {tema_seleccionado}: Página {inicio_pagina}")
            
            # Embed del PDF usando JavaScript para cambiar las páginas
            pdf_embed = f"""
            <iframe id="pdf_view" src="https://digitalhub.fifa.com/m/1009119579a8c8c4/original/Materiales-de-estudio-sobre-el-examen-de-la-FIFA-para-agentes-de-futbol.pdf#page={inicio_pagina}" 
            width="800" height="600"></iframe>
            <script>
                var pdf_view = document.getElementById('pdf_view');
                pdf_view.src = pdf_view.src.replace(/#page=\d+/, '#page={inicio_pagina}');
            </script>
            """
            st.markdown(pdf_embed, unsafe_allow_html=True)

   
    
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


    #Examen oficial fifa test
    def mostrar_examen_fifa(preguntas):
        st.title("Examen Oficial FIFA")

        tema_seleccionado = st.selectbox("Selecciona el tema del examen", [
            "Selecciona el Examen Agente FIFA a realizar por tema...",
            "Reglamento sobre Agente FIFA",
            "Reglamento del Estatuto y la Transferencia del Jugador",
            "Preguntas sobre Código Disciplinario",
            "Preguntas sobre Estatutos de la FIFA",
            "Preguntas sobre Salvaguardia de la infancia"
        ])

        if tema_seleccionado and tema_seleccionado != "Selecciona el Examen Agente FIFA a realizar por tema...":
            preguntas_seleccionadas = preguntas.get(tema_seleccionado, [])
            puntaje = 0

            for i, pregunta in enumerate(preguntas_seleccionadas, 1):
                pregunta_texto = pregunta['pregunta']
                opciones = pregunta['opciones']

                respuesta_correcta = pregunta.get('respuesta_correcta')  # Busca la respuesta_correcta si existe

                st.markdown(f"##### Pregunta {i}: {pregunta_texto}")  # Formato más pequeño para la pregunta

                estados_checkboxes = [st.checkbox(opcion, key=f"checkbox_{i}_{indice}") for indice, opcion in enumerate(opciones)]

                respuestas_seleccionadas = [opcion for opcion, estado in zip(opciones, estados_checkboxes) if estado]
                respuestas_seleccionadas.sort()

                if st.button(f"Ver respuesta {i}"):
                    if respuesta_correcta:  # Si la respuesta_correcta existe
                        if sorted(respuesta_correcta) == sorted(respuestas_seleccionadas):
                            st.success(f"**Respuesta {i}: ¡Correcto! {respuesta_correcta}**")
                            puntaje += 1
                        else:
                            st.error(f"**Respuesta {i}: Incorrecto. La respuesta correcta es: {respuesta_correcta}**")
                    else:  # Si no existe, utilizamos respuestas_correctas
                        respuestas_correctas = pregunta.get('respuestas_correctas', [])
                        if sorted(respuestas_correctas) == sorted(respuestas_seleccionadas):
                            st.success(f"**Respuesta {i}: ¡Correcto! {respuestas_correctas}**")
                            puntaje += 1
                        else:
                            st.error(f"**Respuesta {i}: Incorrecto. La respuesta correcta es: {respuestas_correctas}**")

                st.markdown("---")  # Línea horizontal para separar preguntas

            if preguntas_seleccionadas:  # Si hay preguntas seleccionadas
                st.write(f"**Puntaje total: {puntaje}/{len(preguntas_seleccionadas)}**")
            else:
                st.write("No hay preguntas cargadas para este examen.")
        else:
            st.write("")




    #Funcion Ventanas de mercado calendarios
    def ventana_mercado(pdf_url):
        st.title("Ventanas de mercados")
        st.markdown(f'<iframe src="{pdf_url}" width="100%" height="600px" style="border: none;"></iframe>', unsafe_allow_html=True)








    #Visualizacion
    def main():
        tabs = ["Inicio","Examen oficial FIFA", "Examenes para practicar", "Resumenes", "Formación", "Temario", "Videos", "Calculadora"]  # Nuevas secciones
        tab_select = st.sidebar.selectbox("Selecciona una sección", tabs, index=0)

        if tab_select == "Inicio":
            mostrar_inicio()

        elif tab_select == "Examenes para practicar":
            mostrar_examen()
            if st.button("Realizar otro examen"):
                # Borrar el contenido anterior antes de iniciar un nuevo examen
                st.session_state['sesion'] = iniciar_sesion()
                st.experimental_rerun()       
        

            
        elif tab_select == "Resumenes":
            st.subheader("Ver resúmenes por temática")
            mostrar_resumenes()  # Llama a la función desde resumenes.py para mostrar los resúmenes
                    
                    
        elif tab_select == "Formación":

            # Definir las opciones del menú desplegable
            opciones_esquemas = {
                "Tabla Formación": esquema_formacion,
                "Tabla Confederación AFC": confederacion_afc,
                "Tabla Confederación CAF": confederacion_caf,
                "Tabla Confederación CONCACAF": confederacion_concacaf,
                "Tabla Confederación CONMEBOL": confederacion_conmebol,
                "Tabla Confederación OFC": confederacion_ofc,
                "Tabla Confederación UEFA": confederacion_uefa,
            }

            # Seleccionar el esquema a mostrar
            selected_option = st.selectbox("Selecciona un esquema", list(opciones_esquemas.keys()))

            # Mostrar el esquema seleccionado
            esquema_funcion = opciones_esquemas[selected_option]
            if selected_option in ["Tabla Formación"]:
                esquema_funcion()
            else:
                tabla_confederacion = esquema_funcion()
                st.write(tabla_confederacion)

        
            
            
        elif tab_select == "Temario":
            mostrar_pdf_seleccionado() 
            
        elif tab_select == "Videos":

            if tab_select == "Videos":
                videos = get_videos()  # Obtener la lista de videos

                # Obtener los títulos de los videos para el selector
                video_titles = [video['clase'] for video in videos]
                
                # Selector para elegir el video
                selected_video = st.selectbox("Selecciona un video", video_titles)

                # Mostrar el video seleccionado con st.video
                for video in videos:
                    if video['clase'] == selected_video:
                        st.header(f"{video['clase']} - {video['titulo']}")
                        st.video(video['url'])


            
        elif tab_select == "Calculadora":
            calcular_comision() 
            calcular_pagos_variables()

        elif tab_select == "Examen oficial FIFA":
            mostrar_examen_fifa({
                "Reglamento sobre Agente FIFA": preguntas_agente_fifa,
                "Reglamento del Estatuto y la Transferencia del Jugador": preguntas_estatuto_transferencia,
                "Preguntas sobre Código Disciplinario": preguntas_codigo_disciplinario,
                "Preguntas sobre Estatutos de la FIFA": preguntas_estatutos_fifa,
                "Preguntas sobre Salvaguardia de la infancia": preguntas_salvaguardia
            })
            

                    
                    
                    
                    

    if __name__ == "__main__":
        main()  

    else:
        st.error("Contraseña incorrecta. Acceso denegado.")

