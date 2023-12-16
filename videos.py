import streamlit as st
  
   
def get_videos():
    st.title("Clases Grabadas")
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
        {
            "clase": "Clase 13",
            "titulo": "Clase 13 - RTIJ VII",
            "url": "https://youtu.be/OULXUG7_oiM"
        },
        {
            "clase": "Clase 14",
            "titulo": "Clase 14 - RTIJ VIII",
            "url": "https://youtu.be/nlCv3KHdAcw"
        },        
                                                                            
    ]
    
    return videos  # Asegurémonos de retornar la lista de videos