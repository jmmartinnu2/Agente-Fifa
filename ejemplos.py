
def calcular_pago_formacion(categoria_i, categoria_ii, categoria_iii, categoria_iv, jugadores_menores_edad):
    total_pago = 0
    
    # Calcula el pago de la comisión por formación
    total_pago += categoria_i * jugadores_menores_edad['Categoría I']
    total_pago += categoria_ii * jugadores_menores_edad['Categoría II']
    total_pago += categoria_iii * jugadores_menores_edad['Categoría III']
    total_pago += categoria_iv * jugadores_menores_edad['Categoría IV']
    
    return total_pago

# Simular jugadores menores de edad por categoría
jugadores_menores_edad = {
    'Categoría I': 10,
    'Categoría II': 20,
    'Categoría III': 30,
    'Categoría IV': 40
}

# Obtener las categorías del país seleccionado
cat_i, cat_ii, cat_iii, cat_iv = obtener_categoria_por_pais(pais_seleccionado)

if cat_i is not None:
    # Calcular el pago de la comisión por formación
    pago_total = calcular_pago_formacion(cat_i, cat_ii, cat_iii, cat_iv, jugadores_menores_edad)
    
    st.write(f"País: {pais_seleccionado}")
    st.write(f"Pago total por formación: {pago_total}")
else:
    st.write("El país seleccionado no está en la lista de la Confederación.")



paises_confederaciones = [
    "Afganistán", "Albania", "Alemania", "Andorra", "Angola", "Antigua y Barbuda", "Arabia Saudita", "Argelia", 
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaiyán", "Bahamas", "Baréin", "Bangladés", "Barbados", 
    "Bielorrusia", "Bélgica", "Belice", "Benín", "Bermudas", "Bután", "Bolivia", "Bosnia y Herzegovina", "Botsuana", 
    "Brasil", "Brunéi Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Camboya", "Camerún", 
    "Canadá", "Chad", "Chile", "China", "Chipre", "Colombia", "Comoras", "Congo", "República del Congo", "Corea del Norte", 
    "Corea del Sur", "Costa Rica", "Costa de Marfil", "Croacia", "Cuba", "Dinamarca", "Dominica", "Ecuador", "Egipto", 
    "El Salvador", "Emiratos Árabes Unidos", "Eritrea", "Eslovaquia", "Eslovenia", "España", "Estados Unidos", 
    "Estonia", "Eswatini", "Etiopía", "Federación de Rusia", "Federación de San Cristóbal y Nieves", 
    "Federación de Santa Lucía", "Federación de San Vicente y las Granadinas", "Filipinas", "Finlandia", "Fiyi", 
    "Francia", "Gabón", "Gambia", "Georgia", "Ghana", "Granada", "Grecia", "Guatemala", "Guinea", "Guinea Ecuatorial", 
    "Guinea-Bissau", "Guyana", "Haití", "Honduras", "Hong Kong", "Hungría", "India", "Indonesia", "Irán", "Iraq", 
    "Irlanda", "Islandia", "Islas Caimán", "Islas Cook", "Islas Feroe", "Islas Marshall", "Islas Salomón", 
    "Islas Turcas y Caicos", "Islas Vírgenes Británicas", "Israel", "Italia", "Jamaica", "Japón", "Jordania", "Kazajistán", 
    "Kenia", "Kirguistán", "Kuwait", "Laos", "Lesoto", "Letonia", "Líbano", "Liberia", "Libia", "Liechtenstein", 
    "Lituania", "Luxemburgo", "Macao", "Madagascar", "Malasia", "Malaui", "Maldivas", "Malí", "Malta", "Marruecos", 
    "Mauricio", "Mauritania", "México", "Mónaco", "Mongolia", "Montenegro", "Mozambique", "Namibia", "Nauru", "Nepal", 
    "Nicaragua", "Níger", "Nigeria", "Noruega", "Nueva Zelanda", "Omán", "Pakistán", "Palaos", "Palestina", "Panamá", 
    "Papúa Nueva Guinea", "Paraguay", "Países Bajos", "Perú", "Polonia", "Portugal", "Puerto Rico", "Qatar", "Reino Unido", 
    "República Centroafricana", "República Checa", "República Dominicana", "República Kirguisa", "República de Moldavia", 
    "República Árabe Saharaui Democrática", "República Árabe Siria", "República de Macedonia del Norte", "República de Serbia", 
    "República de Sudán del Sur", "República de Zambia", "República de Zimbabue", "República de Yibuti", 
    "República de Trinidad y Tobago", "República de Uzbekistán", "República de Yemén", "República del Congo", "Ruanda", 
    "Rumanía", "Rusia", "Samoa", "San Marino", "San Cristóbal y Nieves", "San Vicente y las Granadinas", "Santa Lucía", 
    "Santo Tomé y Príncipe", "Senegal", "Serbia", "Seychelles", "Sierra Leona", "Singapur", "Siria", "Somalia", 
    "Sri Lanka", "Suazilandia", "Sudáfrica", "Sudán", "Suecia", "Suiza", "Surinam", "Tailandia", "Taiwán", "Tanzania", 
    "Tayikistán", "Timor Oriental", "Togo", "Tonga", "Trinidad y Tobago", "Túnez", "Turkmenistán", "Turquía", "Tuvalu", 
    "Ucrania", "Uganda", "Uruguay", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Yibuti", "Zambia", "Zimbabue"
]

# Obtener la confederación de un país específico
def obtener_confederacion(pais):
    if pais in paises_confederaciones:
        return paises_confederaciones[pais]
    else:
        return None

# Ejemplo de uso
pais_seleccionado = "España"  # Puedes cambiar esto por la selección del usuario
confederacion = obtener_confederacion(pais_seleccionado)

if confederacion:
    st.write(f"El país {pais_seleccionado} pertenece a la confederación {confederacion}.")
else:
    st.write("No se encontró la confederación para el país seleccionado.")