def generar_contrato_representacion(nombre_cliente, direccion, nombre_agente, numero_licencia, duracion_acuerdo):
    contrato = f"""
    CONTRATO DE REPRESENTACIÓN

    Entre {nombre_cliente}, con domicilio en {direccion}, en adelante "El Cliente", y 
    {nombre_agente}, con número de licencia {numero_licencia}, en adelante "El Agente FIFA".

    Ambas partes acuerdan lo siguiente:
    - Duración del acuerdo: {duracion_acuerdo}
    - ...

    Firma: ___________________________           Firma: ___________________________
    Fecha: ___________________________           Fecha: ___________________________
    """
    return contrato

def generar_contrato_servicios(nombre_cliente, direccion, nombre_agente, numero_licencia):
    contrato = f"""
    CONTRATO DE SERVICIOS

    Entre {nombre_cliente}, con domicilio en {direccion}, en adelante "El Cliente", y 
    {nombre_agente}, con número de licencia {numero_licencia}, en adelante "El Agente FIFA".

    Ambas partes acuerdan lo siguiente:

    1. Servicios del Agente FIFA:
       a. Representación: El Agente FIFA actuará como representante exclusivo del Cliente para negociar contratos relacionados con su carrera como jugador de fútbol.
       b. Asesoramiento: El Agente FIFA brindará asesoramiento al Cliente en asuntos contractuales y financieros.

    2. Duración del Contrato: Este contrato tendrá una duración de [Duración del Contrato] meses/años a partir de la fecha de firma.

    3. Comisión: El Agente FIFA recibirá una comisión del [Porcentaje de Comisión] sobre los ingresos generados por el Cliente a través de contratos y patrocinios.

    Firma: ___________________________           Firma: ___________________________
    Fecha: ___________________________           Fecha: ___________________________
    """
    return contrato


def generar_contrato_asesoramiento(nombre_cliente, direccion, nombre_agente, numero_licencia):
    contrato = f"""
    CONTRATO DE ASESORAMIENTO

    Entre {nombre_cliente}, con domicilio en {direccion}, en adelante "El Cliente", y 
    {nombre_agente}, con número de licencia {numero_licencia}, en adelante "El Agente FIFA".

    Ambas partes acuerdan lo siguiente:

    1. Objeto del Contrato:
       a. El Agente FIFA prestará asesoramiento y orientación al Cliente en asuntos relacionados con su carrera como jugador de fútbol.
       b. El Cliente podrá consultar al Agente FIFA sobre cuestiones contractuales, financieras y estratégicas.

    2. Obligaciones del Agente FIFA:
       a. Brindar asesoramiento profesional al Cliente en la gestión de su carrera deportiva.
       b. Aconsejar al Cliente sobre oportunidades de contratación, estrategias de marketing y planificación financiera.

    3. Duración del Contrato: Este contrato tendrá una duración de [Duración del Contrato] meses/años a partir de la fecha de firma.

    4. Honorarios y Comisiones: 
       a. El Agente FIFA recibirá una compensación de [Cantidad/Modalidad de Pago] por sus servicios de asesoramiento.
       b. En caso de cierre de contratos o acuerdos, el Agente FIFA recibirá una comisión del [Porcentaje de Comisión] sobre los ingresos generados por el Cliente.

    5. Confidencialidad: Ambas partes acuerdan mantener la confidencialidad sobre la información intercambiada durante la relación contractual.

    Firma: ___________________________           Firma: ___________________________
    Fecha: ___________________________           Fecha: ___________________________
    """
    return contrato


def generar_contrato_segun_tipo(nombre_cliente, direccion, nombre_agente, numero_licencia, tipo_contrato, duracion_acuerdo=None):
    if tipo_contrato == "Contrato de Representación":
        contrato = generar_contrato_representacion(nombre_cliente, direccion, nombre_agente, numero_licencia, duracion_acuerdo)
    elif tipo_contrato == "Contrato de Servicios":
        contrato = generar_contrato_servicios(nombre_cliente, direccion, nombre_agente, numero_licencia)
    elif tipo_contrato == "Contrato de Asesoramiento":
        contrato = generar_contrato_asesoramiento(nombre_cliente, direccion, nombre_agente, numero_licencia)

    else:
        contrato = "Tipo de contrato no reconocido"

    return contrato
