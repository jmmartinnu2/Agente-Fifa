from pyvis.network import Network
import streamlit as st 
import pandas as pd



def mostrar_esquema_fifa():
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
    return network





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
            "Categoría I": ['40,000 USD', '30,000 USD', '40,000 USD', '50,000 USD', '30,000 USD', '90,000 EUR'],
            "Categoría II": ['10,000 USD', '10,000 USD', '10,000 USD', '30,000 USD', '10,000 USD', '60,000 EUR'],
            "Categoría III": ['2,000 USD', '2,000 USD', '2,000 USD', '10,000 USD', '2,000 USD', '30,000 EUR'],
            "Categoría IV": ['0 USD', '0 USD', '0 USD', '2,000 USD', '0 USD', '10,000 EUR']
        }
    }
    
    st.title("Esquema de Formación")
    
    st.header("Reglas")
    for regla in esquema.get("Reglas", []):
        st.write("✅ " + regla)

    st.header("Cálculo de Indemnización")
    for calculo in esquema.get("Calculo Indemnización", []):
        st.write("🔢 " + calculo)

    st.header("Tabla Confederación")
    df_confederacion = pd.DataFrame(esquema.get("Tabla Confederación", {}))
    st.write(df_confederacion)