import streamlit as st
import pandas as pd




def esquema_formacion():
    esquema = {
        "Reglas": [
            "Si el club anterior no ofrece contrato, no hay indemnización por Formación",
            "Para calcular la indemnización, se clasifican los clubes en máximo cuatro categorías",
            "Formación entre 12 y 15 años se estima según clubes de la cuarta categoría",
            "Tiempo límite para reclamar derecho de formación: final de temporada al cumplir 23 años",
            "Se paga por formación hasta los 21 años del jugador"
        ],
        "Calculo Indemnización": [
            "Si jugador pasa de categoría inferior a superior: promedio entre ambas categorías",
            "Si jugador pasa de categoría superior a inferior: indemnización según la menor"
        ],
        "Tabla Confederación": {
            "Confederación": ['AFC', 'CAF', 'Concacaf', 'CONMEBOL', 'OFC', 'UEFA'],
            "Categoría I": ['', '', '', '50,000 USD', '', '90,000 EUR'],
            "Categoría II": ['40,000 USD', '30,000 USD', '40,000 USD', '30,000 USD', '30,000 USD', '60,000 EUR'],
            "Categoría III": ['10,000 USD', '10,000 USD', '10,000 USD', '10,000 USD', '10,000 USD', '30,000 EUR'],
            "Categoría IV": ['2,000 USD', '2,000 USD', '2,000 USD', '2,000 USD', '2,000 USD', '10,000 EUR']
        }
    }
    
    st.title("Esquema de Formación")
    
    st.header("Reglas")
    for regla in esquema.get("Reglas", []):
        st.write("✅ " + regla)

    st.header("Cálculo de Indemnización")
    for calculo in esquema.get("Calculo Indemnización", []):
        st.write("🔢 " + calculo)

    st.header("Tabla Confederaciones")
    df_confederacion = pd.DataFrame(esquema.get("Tabla Confederación", {}))
    st.write(df_confederacion)
    
    
    
    
    


def confederacion_afc():
    confederacion_afc = {
        'Federación miembro': [
            'Afganistán', 'Arabia Saudí', 'Australia', 'Bangladés', 'Baréin', 'Brunéi Darusalam',
            'Bután', 'Camboya', 'Catar', 'China Taipéi', 'Emiratos Árabes Unidos', 'Filipinas',
            'Guam', 'Hong Kong', 'India', 'Indonesia', 'Irak', 'Japón', 'Jordania', 'Kuwait',
            'Laos', 'Líbano', 'Macao', 'Malasia', 'Maldivas', 'Mongolia', 'Myanmar', 'Nepal',
            'Omán', 'Pakistán', 'Palestina'
        ],
        'Categoría I': [
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '', '', '', 'X'
        ],
        'Categoría II': [
            '', '', 'X', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'X', '', '',
            '', '', '', '', '', '', '', '', '', '', ''
        ],
        'Categoría III': [
            '', '', 'X', '', '', '', '', '', '', '', '', '', '', '', '', '', 'X', 'X', '', '',
            'X', '', '', '', '', '', '', '', '', '', ''
        ],
        'Categoría IV': [
            'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
            'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'
        ]
    }

    df_afc = pd.DataFrame(confederacion_afc)
    return df_afc




def confederacion_caf():
    confederacion_caf = [
        ['Angola', '', '', '', 'X'],
        ['Argelia', '', 'X', 'X', 'X'],
        ['Benín', '', '', '', 'X'],
        ['Botsuana', '', '', '', 'X'],
        ['Burkina Faso', '', '', '', 'X'],
        ['Burundi', '', '', 'X', 'X'],
        ['Cabo Verde', '', '', '', 'X'],
        ['Camerún', '', 'X', 'X', 'X'],
        ['Chad', '', '', '', 'X'],
        ['Comoras', '', '', '', 'X'],
        ['Congo', '', '', '', 'X'],
        ['Costa de Marfil', '', 'X', 'X', 'X'],
        ['Egipto', '', '', 'X', 'X'],
        ['Eritrea', '', '', '', 'X'],
        ['Esuatini', '', '', '', 'X'],
        ['Etiopía', '', '', '', 'X'],
        ['Gabón', '', '', '', 'X'],
        ['Gambia', '', '', 'X', 'X'],
        ['Ghana', '', 'X', 'X', 'X'],
        ['Guinea', '', '', '', 'X'],
        ['Guinea-Bisáu', '', '', '', 'X'],
        ['Guinea Ecuatorial', '', '', '', 'X'],
        ['Kenia', '', '', '', 'X'],
        ['Lesoto', '', '', '', 'X'],
        ['Liberia', '', '', '', 'X'],
        ['Libia', '', '', 'X', 'X'],
        ['Madagascar', '', '', '', 'X'],
        ['Malaui', '', '', '', 'X'],
        ['Mali', '', '', 'X', 'X'],
        ['Marruecos', '', 'X', 'X', 'X'],
        ['Mauricio', '', '', '', 'X']
    ]

    column_names = ['Federación miembro', 'Categoría I', 'Categoría II', 'Categoría III', 'Categoría IV']
    df_caf = pd.DataFrame(confederacion_caf, columns=column_names)
    return df_caf




def confederacion_concacaf():
    confederacion_norteamericana = [
        ['Anguila', '', '', '', 'X'],
        ['Antigua y Barbuda', '', '', '', 'X'],
        ['Aruba', '', '', '', 'X'],
        ['Bahamas', '', '', '', 'X'],
        ['Barbados', '', '', '', 'X'],
        ['Belice', '', '', '', 'X'],
        ['Bermudas', '', '', '', 'X'],
        ['Canadá', '', '', 'X', 'X'],
        ['Costa Rica', '', 'X', 'X', 'X'],
        ['Cuba', '', '', '', 'X'],
        ['Curasao', '', '', '', 'X'],
        ['Dominica', '', '', '', 'X'],
        ['EE. UU.', '', 'X', 'X', 'X'],
        ['El Salvador', '', '', 'X', 'X'],
        ['Granada', '', '', '', 'X'],
        ['Guatemala', '', 'X', 'X', 'X'],
        ['Guyana', '', '', '', 'X'],
        ['Haití', '', '', '', 'X'],
        ['Honduras', '', '', 'X', 'X'],
        ['Islas Caimán', '', '', '', 'X'],
        ['Islas Vírgenes Británicas', '', '', '', 'X'],
        ['Islas Vírgenes Estadounidenses', '', '', '', 'X'],
        ['Jamaica', '', '', 'X', 'X'],
        ['México', '', 'X', 'X', 'X'],
        ['Montserrat', '', '', '', 'X'],
        ['Nicaragua', '', '', '', 'X'],
        ['Panamá', '', '', '', 'X'],
        ['Puerto Rico', '', '', '', 'X'],
        ['República Dominicana', '', '', '', 'X'],
        ['San Cristóbal y Nieves', '', '', '', 'X'],
        ['Santa Lucía', '', '', '', 'X'],
        ['San Vicente y las Granadinas', '', '', '', 'X'],
        ['Surinam', '', '', '', 'X'],
        ['Trinidad y Tobago', '', '', 'X', 'X'],
        ['Turcas y Caicos', '', '', '', 'X']
    ]

    column_names = ['Federación miembro', 'Categoría I', 'Categoría II', 'Categoría III', 'Categoría IV']
    df_concacaf = pd.DataFrame(confederacion_norteamericana, columns=column_names)
    return df_concacaf




def confederacion_conmebol():
    confederacion_conmebol = [
        ['Argentina', 'X', 'X', 'X', 'X'],
        ['Bolivia', '', '', 'X', 'X'],
        ['Brasil', 'X', 'X', 'X', 'X'],
        ['Chile', '', 'X', 'X', 'X'],
        ['Colombia', '', '', 'X', 'X'],
        ['Ecuador', '', '', 'X', 'X'],
        ['Paraguay', '', '', 'X', 'X'],
        ['Perú', '', '', 'X', 'X'],
        ['Uruguay', '', 'X', 'X', 'X'],
        ['Venezuela', '', '', 'X', 'X']
    ]

    column_names = ['Federación miembro', 'Categoría I', 'Categoría II', 'Categoría III', 'Categoría IV']
    df_conmebol = pd.DataFrame(confederacion_conmebol, columns=column_names)
    return df_conmebol




def confederacion_ofc():
    confederacion_ofc = [
        ['Fiyi', '', '', '', 'X'],
        ['Islas Cook', '', '', '', 'X'],
        ['Islas Salomón', '', '', '', 'X'],
        ['Nueva Caledonia', '', '', '', 'X'],
        ['Nueva Zelanda', '', '', 'X', 'X'],
        ['Papúa Nueva Guinea', '', '', '', 'X'],
        ['Samoa', '', '', '', 'X'],
        ['Samoa Estadounidense', '', '', '', 'X'],
        ['Tahití', '', '', '', 'X'],
        ['Tonga', '', '', '', 'X'],
        ['Vanuatu', '', '', '', 'X']
    ]

    column_names = ['Federación miembro', 'Categoría I', 'Categoría II', 'Categoría III', 'Categoría IV']
    df = pd.DataFrame(confederacion_ofc, columns=column_names)
    return df





def confederacion_uefa():
    confederacion_uefa = [
        ['Albania', '', '', 'X', 'X'],
        ['Alemania', 'X', 'X', 'X', 'X'],
        ['Andorra', '', '', '', 'X'],
        ['Armenia', '', '', 'X', 'X'],
        ['Austria', '', 'X', 'X', 'X'],
        ['Azerbaiyán', '', '', 'X', 'X'],
        ['Bélgica', 'X', 'X', 'X', 'X'],
        ['Bielorrusia', '', '', 'X', 'X'],
        ['Bosnia y Herzegovina', '', '', 'X', 'X'],
        ['Bulgaria', '', '', 'X', 'X'],
        ['Chipre', '', '', 'X', 'X'],
        ['Croacia', '', '', 'X', 'X'],
        ['Dinamarca', '', 'X', 'X', 'X'],
        ['Escocia', '', 'X', 'X', 'X'],
        ['Eslovaquia', '', '', 'X', 'X'],
        ['Eslovenia', '', '', 'X', 'X'],
        ['España', 'X', 'X', 'X', 'X'],
        ['Estonia', '', '', 'X', 'X'],
        ['Finlandia', '', '', 'X', 'X'],
        ['Francia', 'X', 'X', 'X', 'X'],
        ['Gales', '', '', 'X', 'X'],
        ['Georgia', '', '', 'X', 'X'],
        ['Gibraltar', '', '', '', 'X'],
        ['Grecia', '', 'X', 'X', 'X'],
        ['Hungría', '', 'X', 'X', 'X'],
        ['Inglaterra', 'X', 'X', 'X', 'X'],
        ['Irlanda del Norte', '', '', 'X', 'X'],
        ['Islandia', '', '', 'X', 'X'],
        ['Islas Feroe', '', '', '', 'X'],
        ['Israel', '', '', 'X', 'X'],
        ['Italia', 'X', 'X', 'X', 'X'],
        ['Kazajistán', '', '', 'X', 'X'],
        ['Kosovo', '', '', 'X', 'X'],
        ['Letonia', '', '', 'X', 'X'],
        ['Liechtenstein', '', '', '', 'X'],
        ['Lituania', '', '', 'X', 'X'],
        ['Luxemburgo', '', '', 'X', 'X'],
        ['Macedonia del Norte', '', '', 'X', 'X'],
        ['Malta', '', '', 'X', 'X'],
        ['Moldavia', '', '', 'X', 'X'],
        ['Montenegro', '', '', '', 'X'],
        ['Noruega', '', 'X', 'X', 'X'],
        ['Países Bajos', 'X', 'X', 'X', 'X'],
        ['Polonia', '', '', 'X', 'X'],
        ['Portugal', '', 'X', 'X', 'X'],
        ['República Checa', '', '', 'X', 'X'],
        ['República de Irlanda', '', 'X', 'X', 'X'],
        ['Rumanía', '', '', 'X', 'X'],
        ['Rusia', '', 'X', 'X', 'X'],
        ['San Marino', '', '', '', 'X'],
        ['Serbia', '', '', 'X', 'X'],
        ['Suecia', '', 'X', 'X', 'X'],
        ['Suiza', '', 'X', 'X', 'X'],
        ['Turquía', '', 'X', 'X', 'X'],
        ['Ucrania', '', 'X', 'X', 'X']
    ]

    column_names = ['Federación miembro', 'Categoría I', 'Categoría II', 'Categoría III', 'Categoría IV']
    df = pd.DataFrame(confederacion_uefa, columns=column_names)
    return df

# Ejemplo de uso de la función
tabla_confederacion_uefa = confederacion_uefa()
print(tabla_confederacion_uefa)