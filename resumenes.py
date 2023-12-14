import streamlit as st

def mostrar_resumenes():
    # Información de las secciones
    secciones = [
        {
            "titulo": ":bookmark_tabs: Estatutos FIFA",
            "resumen": [
                "Texto resumen Estatutos FIFA..."
            ]
        },
        {
            "titulo": ":orange_book: Código Disciplinario",
            "resumen": [
                "Texto resumen Código Disciplinario..."
            ]
        },
        {
            "titulo": ":blue_book: Codigo de Etica",
            "resumen": [
                "Texto resumen Codigo de Etica..."
            ]
        },
        {
            "titulo": ":notebook_with_decorative_cover: Reglamento sobre el Estatuto y la Transferencia de jugadores",
            "resumen": [
                ":orange[***Artículo 7***:] La asociación que inscribe a un jugador debe entregar un pasaporte del jugador con todos los datos relevantes del jugador, que incluirá los clubes en los que ha estado inscrito desde el año en que cumplió 12 años.",
                ":orange[***Artículo 7***:] Para los derechos relacionados con las compensaciones por formación que están sujetos al Reglamento de la Cámara de Compensación de la FIFA, se generará un Pasaporte Electrónico del Jugador (EPP) que contiene información consolidada sobre la inscripción del jugador a lo largo de su carrera.",
                ":orange[***Artículo 8***:] La solicitud de inscripción debe presentarse con una copia del contrato del jugador profesional. El órgano competente puede considerar cualquier enmienda en el contrato o acuerdos adicionales que no se hayan presentado debidamente.",
                ":orange[***Artículo 9***:] Los jugadores solo pueden inscribirse en una nueva asociación cuando esta haya recibido el CTI de la asociación anterior, expedido gratuitamente y sin condiciones.",
                ":orange[***Artículo 9***:] Las asociaciones no pueden solicitar la expedición de un CTI para permitir a los jugadores participar en partidos amistosos en el contexto de una prueba.",
                ":orange[***Artículo 9***:] La nueva asociación debe informar por escrito a la asociación o asociaciones del club o clubes que formaron y educaron al jugador entre los 12 y los 23 años de edad sobre la inscripción del jugador como profesional una vez recibido el CTI.",
                ":orange[***Artículo 9***:] Los jugadores menores de 10 años no necesitan el CTI.",
                ":orange[***Artículo 10***:] Un club puede ceder en préstamo a un profesional a otro club basándose en un acuerdo por escrito. Durante el periodo de préstamo, las obligaciones contractuales entre el profesional y su club original quedan suspendidas, excepto si se especifica lo contrario por escrito.",
                ":orange[***Artículo 10***:] El contrato de préstamo puede prolongarse con el consentimiento por escrito del profesional",
                ":orange[***Artículo 10***:] Se prohíbe al nuevo club llevar a cabo un subpréstamo o transferencia permanente de un profesional a un tercer club",
                ":orange[***Artículo 10***:] Si el contrato entre el profesional y el nuevo club se rescinde unilateralmente antes de que concluya la duración acordada en el contrato de préstamo, el profesional tiene derecho a volver al club anterior.",
                ":orange[***Artículo 10***:] A partir del 1 de julio de 2024, se limitará el número de préstamos: un club podrá ceder en préstamo un máximo de seis profesionales y tener en plantilla un máximo de seis profesionales cedidos en préstamo.",
                ":orange[***Artículo 10***:] Existen excepciones para estos límites, por ejemplo, si el préstamo ocurre antes de que el profesional cumpla 21 años o si el profesional fue formado por el club original.",
                ":orange[***Artículo 10***:] Hay restricciones independientes de la edad del jugador o de si ha sido formado por el club: un club puede ceder en préstamo a un club específico un máximo de tres profesionales y tener en plantilla un máximo de tres profesionales cedidos en préstamo por un club específico.",
                ":orange[***Artículo 10***:] Existen periodos de transición para estas limitaciones",
                ":orange[***Artículo 16***:] Los contratos no pueden rescindirse de forma unilateral durante un periodo de competición.",
                ":orange[***Artículo 17***:] Las consecuencias de la ruptura de contratos sin justificación son: a. La parte que rompe el contrato tiene que pagar una indemnización, calculada de acuerdo con la legislación nacional, las características del deporte y otros criterios objetivos. b. Si un jugador no ha firmado un nuevo contrato después de la rescisión de su contrato anterior, la indemnización generalmente equivaldrá al valor residual del contrato que se ha rescindido prematuramente.",
                ":orange[***Artículo 17***:] Las consecuencias de la ruptura de contratos sin justificación son: c. En caso de que el jugador haya firmado un nuevo contrato antes de la decisión, el valor del nuevo contrato durante el periodo correspondiente al tiempo restante del contrato rescindido se deducirá del valor residual del contrato rescindido. d. Los acuerdos colectivos válidamente negociados pueden divergir de estos principios. e. El derecho a una indemnización no puede cederse a terceros.",
                ":orange[***Artículo 17***:] Las consecuencias de la ruptura de contratos sin justificación son: f. Si un jugador debe pagar una indemnización, él y su nuevo club son conjuntamente responsables de hacerlo. g. Se impondrán sanciones deportivas a un jugador que rompa un contrato durante un periodo protegido. h. Se impondrán sanciones deportivas a un club que rompa un contrato durante un periodo protegido, o que haya inducido a romper un contrato.",
                ":orange[***Artículo 18***:] Las disposiciones especiales relacionadas con los contratos entre jugadores profesionales y clubes son: a. Los contratos deben incluir el nombre del agente, su cliente, su número de licencia de la FIFA y su firma. b. La duración mínima de un contrato será desde la fecha de inscripción hasta el final de la temporada; la duración máxima será de cinco años. Los jugadores menores de 18 años no pueden firmar un contrato de una duración mayor de tres años.",
                ":orange[***Artículo 18***:] Las disposiciones especiales relacionadas con los contratos entre jugadores profesionales y clubes son: c. Un club que quiera firmar un contrato con un jugador profesional debe comunicar su intención por escrito al club del jugador antes de iniciar las negociaciones. d. La validez de un contrato no puede depender de los resultados de un examen médico o de la obtención de un permiso de trabajo. e. Si un jugador profesional firma más de un contrato para el mismo periodo, se aplicarán las disposiciones del capítulo IV.",
                ":orange[***Artículo 18***:] Las disposiciones especiales relacionadas con los contratos entre jugadores profesionales y clubes son: f. Las cláusulas contractuales que permiten al club un periodo adicional para pagar al jugador no serán reconocidas. g. Las jugadoras tienen derecho a disfrutar de la baja por maternidad durante el periodo de vigencia de su contrato, percibiendo dos terceras partes del salario estipulado en el contrato."
            ]
        },
        {
            "titulo": ":notebook: Reglamento de procedimiento del Tribunal del Fútbol",
            "resumen": [
                "Texto resumen Reglamento del Tribunal del Fútbol..."
            ]
        },
        {
            "titulo": ":green_book: Reglamento de la Cámara de Compensación",
            "resumen": [
                "Texto resumen Reglamento de la Cámara de Compensación..."
            ]
        },
        {
            "titulo": ":ledger: Reglamento sobre Agente Fifa",
            "resumen": [
                ":orange[***Importante***:] No se puede cobrar comision de por transferencia de jugadores a futuro cuando hemos gestionado un contrato.",
                ":orange[***Importante***:] Los agentes de fútbol solo pueden representar a un cliente si han firmado un contrato de representación con ese cliente.",
                ":orange[***Importante***:] Solo los agentes de fútbol pueden contactar a un posible cliente para servicios de representación.",
                ":orange[***Importante***:] Los contratos de representación entre un agente de fútbol y una persona no pueden exceder los dos años y deben renovarse a través de un nuevo contrato de representación. No se permiten cláusulas de renovación automática.",
                ":orange[***Importante***:] Los agentes de fútbol solo pueden tener un contrato de representación vigente con la misma persona a la vez. Deben informar al cliente sobre la necesidad de asesoría jurídica independiente y obtener confirmación por escrito de que el cliente ha obtenido o renunciado a dicha asesoría.",
                ":orange[***Importante***:] No existe un límite en la duración de los contratos de representación entre una entidad de origen o de destino y un agente de fútbol.",
                ":orange[***Importante***:] Los agentes de fútbol pueden firmar varios contratos de representación con la misma entidad de origen o de destino.",
                ":orange[***Importante***:] Un contrato de representación es válido solo si incluye detalles como la identidad de las partes, la duración, los honorarios del agente, la naturaleza de los servicios y las firmas de todas las partes.",
                ":orange[***Importante***:] Los agentes de fútbol solo pueden representar a una parte en una transacción, a menos que ambas partes consientan explícitamente la doble representación.",
                ":orange[***Importante***:] Los agentes de fútbol no pueden representar a más de una parte en una misma transacción, con una única excepción...",
                ":orange[***Importante***:] Un agente de fútbol y un agente vinculado no pueden representar a clientes diferentes en una misma transacción.",
                ":orange[***Importante***:] Todos los acuerdos de transferencia y contratos laborales deben especificar el nombre del agente de fútbol, su número de licencia de la FIFA, su firma y el nombre de su cliente.",
                ":orange[***Importante***:] Los clientes pueden negociar y formalizar transacciones sin la mediación de un agente de fútbol.",
                ":orange[***Importante***:] No se permiten cláusulas que limiten o penalicen a una persona por negociar o formalizar un contrato laboral sin un agente de fútbol.",
                ":orange[***Importante***:] Ambas partes pueden rescindir un contrato de representación en cualquier momento si hay una causa justificada. Si una parte rescinde un contrato sin causa justificada, debe compensar a la otra parte por cualquier daño resultante. Se considera causa justificada si ocurren ciertas circunstancias que hacen que sea inaceptable esperar que una de las partes mantenga la relación contractual.",
                ":green[***Resumen art. 12***:] El artículo 12 del Reglamento de Agentes de Fútbol de la FIFA establece las normas para los contratos de representación. Los contratos deben ser firmados antes de que un agente pueda representar a un cliente y no pueden exceder los dos años de duración si el cliente es una persona. Los agentes solo pueden representar a una persona a la vez, a menos que haya consentimiento explícito para la doble representación en una transacción. Todos los contratos deben incluir detalles específicos, y se permite que los clientes negocien transacciones sin un agente. Cualquier parte puede rescindir el contrato con causa justificada, y si se rescinde sin causa, se debe compensar a la otra parte.",
                ":blue[***Art.18***:] Los clientes que deciden no actuar en su propio nombre sólo pueden contratar a un agente de fútbol para la prestación de servicios de representación.",
                ":blue[***Art.18***:] Los clientes deben pagar los honorarios acordados con el agente de fútbol en los plazos establecidos en el reglamento y el contrato de representación.",
                ":blue[***Art.18***:] Los clientes deben verificar que el agente de fútbol tenga la licencia correspondiente de la FIFA antes de firmar el contrato de representación.",
                ":blue[***Art.18***:] Los clientes deben colaborar con la federación miembro, confederación y/o FIFA correspondiente en cualquier solicitud relacionada con el agente de fútbol.",
                ":blue[***Art.18***:] Los clientes tienen derecho a solicitar al agente de fútbol un calendario detallado de todos los pagos realizados (incluidos honorarios, gastos y otras remuneraciones).",
                ":blue[***Art.18***:] Los clientes, en caso de ser clubes, deben subir la información requerida al sistema de correlación de transferencias de la FIFA (TMS) en un plazo de catorce días después de su ocurrencia. Esto incluye la información requerida después de cada transferencia internacional, modificaciones del contrato de representación, contratos no relacionados con la representación y pagos de honorarios.",
                ":blue[***Art.18***:] Los clientes deben informar inmediatamente a la FIFA, las confederaciones o las federaciones miembro de cualquier incumplimiento de este reglamento.",
                ":blue[***Art.18***:] Los clientes y sus oficiales no pueden contratar a una persona sin licencia para la prestación de servicios de representación, ni aceptar o solicitar un beneficio indebido de un agente de fútbol.",
                ":blue[***Art.18***:] Los clientes no pueden ofrecer ninguna retribución a un agente de fútbol más allá de los honorarios acordados, interferir en la libre elección de una persona para seleccionar al agente que la representará, ni asistir en ninguna evasión de los límites de los honorarios establecidos en este reglamento.",
                ":blue[***Art.18***:] Los clientes no pueden tener intereses en una agencia o en la actividad de un agente de fútbol.",
                ":blue[***Art.18***:] Las federaciones miembro, clubes y ligas independientes no pueden inducir o coaccionar a una persona para que incumpla los términos del contrato de representación con su agente de fútbol.",
                ":blue[***Art.18***:] Los clientes no pueden permitir que un agente de fútbol o su agencia tengan interés en ellos, y deben informar inmediatamente a la FIFA de cualquier incumplimiento de este reglamento”",
                ":red[***Art.19***:] La FIFA publicará los nombres e información de todos los agentes de fútbol.",
                ":red[***Art.19***:] La FIFA divulgará los clientes que cada agente de fútbol representa, así como la vigencia y si su contrato de representación es exclusivo o no.",
                ":red[***Art.19***:] La FIFA publicará los servicios de representación que los agentes de fútbol prestan a cada cliente.",
                ":red[***Art.19***:] La FIFA revelará cualquier sanción impuesta a un agente de fútbol o a un cliente.",
                ":red[***Art.19***:] La FIFA publicará los datos de todas las transacciones en las que participan los agentes de fútbol, incluyendo los honorarios que perciben.",
                ":grey[***Art.20***:] La Cámara de Agentes del Tribunal del Fútbol tiene la jurisdicción para resolver disputas que surjan de, o estén relacionadas con, un acuerdo de representación de alcance internacional, siempre que la reclamación se realice de acuerdo con el Reglamento de Procedimiento del Tribunal del Fútbol y no hayan transcurrido más de dos años desde el hecho que provocó la disputa.",
                ":grey[***Art.20***:] Los procedimientos específicos para la resolución de disputas se detallan en el Reglamento de Procedimiento del Tribunal del Fútbol.",
                ":grey[***Art.20***:] En caso de disputas surgidas de, o relacionadas con, un contrato de representación de dimensión nacional, el órgano decisorio establecido en el reglamento nacional sobre agentes de fútbol de la federación miembro relevante tendrá la jurisdicción para resolver dichas disputas.",
                ":grey[***Art.20***:] Esto no limita el derecho de cualquier agente de fútbol o cliente a llevar un caso ante un tribunal ordinario.",
                ":violet[***Art.21***:] La Comisión Disciplinaria de la FIFA y, cuando corresponda, la Comisión de Ética independiente, tienen competencia para imponer sanciones a cualquier agente de fútbol o cliente que incumpla este reglamento, los Estatutos de la FIFA o cualquier otro reglamento de la FIFA. Tienen jurisdicción sobre toda conducta vinculada a un contrato de representación de dimensión internacional o a un traspaso internacional o una transacción internacional.",
                ":violet[***Art.21***:] La federación miembro correspondiente es responsable de ejecutar las sanciones impuestas a aquellos agentes de fútbol o clientes que incumplan el reglamento nacional sobre agentes de fútbol. Tienen jurisdicción sobre toda conducta vinculada a un contrato de representación de dimensión nacional o a un traspaso nacional o una transacción nacional.",
                ":green:[***Art.22***:] Los contratos de representación que venzan el 1 de octubre de 2023 o después de la fecha en la que sea aprobado el reglamento seguirán vigentes hasta su fecha natural de vencimiento, independientemente de si cumplen o no los requisitos mínimos establecidos en el artículo 12, apartado 7.",
                ":green[***Art.22***:] Los nuevos contratos de representación o aquellos que se renueven después de la aprobación de este reglamento deberán cumplir con las disposiciones del mismo a partir del 1 de octubre de 2023.",
                ":green[***Art.22***:] Cualquier persona que haya formalizado un contrato de representación bajo estas características estará obligada a obtener una licencia de acuerdo con el presente reglamento para poder seguir prestando servicios de representación a partir del 1 de octubre de 2023.",
                ":orange[***Art.23***:] Trata sobre: Agentes en posesión de una licencia en virtud de una versión anterior del reglamento sobre los agentes de jugadores de la FIFA",
                ":orange[***Art.23***:] Las personas que posean una licencia de agente según versiones anteriores del Reglamento sobre los Agentes de Jugadores de la FIFA (1991, 1995, 2001 o 2008) estarán exentas de aprobar el examen actual si cumplen con varias condiciones: Enviar una solicitud para la nueva licencia de acuerdo con este reglamento antes del 30 de septiembre de 2023. Demostrar que poseen una licencia de agente bajo las versiones anteriores del reglamento. Cumplir con los requisitos de elegibilidad relevantes en el momento de la solicitud. Acreditar su registro como intermediario, o como propietario, director o empleado de una persona jurídica registrada como intermediario, en una federación entre el 1 de abril de 2015 y la fecha de aprobación de este reglamento. Cumplir con lo estipulado en el artículo 7 de este reglamento, después de recibir la confirmación de la FIFA de que están exentos de presentar el examen.",
                ":orange[***Art.23***:] Si un agente con licencia previa cumple con las condiciones, se le otorgará la licencia de acuerdo con el artículo 8 de este reglamento. Luego estarán sujetos a los requisitos de licencia continua, incluyendo la obtención de un número determinado de créditos de desarrollo profesional continuo cada año durante cinco años.",
                ":orange[***Art.23***:] La Secretaría General de la FIFA es responsable de verificar el cumplimiento de los requisitos mencionados en el primer punto.",
                ":blue[***Art.24***:] Trata sobre: Reconocimiento de los sistemas de licencias nacionales",
                ":blue[***Art.24***:] La FIFA puede reconocer un sistema nacional de licencias para agentes deportivos que permita la prestación de servicios equivalentes a los servicios de representación en un país o territorio, siempre que se establezcan los requisitos de elegibilidad para los solicitantes y licenciatarios, y un requisito para que los solicitantes aprueben un examen que incluya preguntas relacionadas con los reglamentos de fútbol vigentes u otros requisitos formativos relevantes.",
                ":blue[***Art.24***:] La federación miembro del país o territorio en el que se aplicará el sistema deberá enviar a la Secretaría General de la FIFA las solicitudes de reconocimiento de sistemas de licencias de agentes deportivos establecidos de acuerdo con la legislación nacional.",
                ":blue[***Art.24***:] Cualquier titular de una licencia que acredite para prestar servicios equivalentes a los servicios de representación en un país o territorio específico quedará exento del requisito de aprobar el examen establecido en este reglamento, siempre que se cumplan ciertas condiciones, incluyendo que la federación miembro haya recibido reconocimiento por parte de la FIFA y que la persona cumpla con los requisitos de elegibilidad.",
                ":blue[***Art.24***:] Si un solicitante cumple con las condiciones correspondientes, se le otorgará la licencia de acuerdo con el artículo 8 de este reglamento. A partir de ese momento, estará sujeto a los requisitos continuos de licencia estipulados en este reglamento, incluyendo la obtención de un número determinado de créditos de desarrollo profesional continuo cada año durante cinco años.",
                ":blue[***Art.24***:] La Secretaría General de la FIFA es responsable de tomar decisiones sobre cualquier solicitud realizada en virtud de este artículo.",
                ":green[***Art.25***:] Trata sobre: Grupo de trabajo sobre los agentes de fútbol",
                ":green[***Art.25***:] La FIFA establecerá un grupo de trabajo específico compuesto por representantes de las partes interesadas del fútbol profesional y organizaciones de agentes.",
                ":green[***Art.25***:] Este grupo de trabajo actuará como un órgano consultivo permanente en cuestiones relacionadas con los agentes de fútbol.",
                ":grey[***Art.26***:] Trata sobre: Casos no previstos",
                ":grey[***Art.26***:] La Secretaría General de la FIFA tomará decisiones sobre cualquier asunto no cubierto por este reglamento.",
                ":grey[***Art.26***:] Los casos de fuerza mayor que afecten a este reglamento serán resueltos por el Consejo de la FIFA y sus decisiones serán definitivas.",
                ":red[***Art.27***:] Trata sobre: Idiomas oficiales",
                ":red[***Art.27***:] En caso de discrepancias en la interpretación de los textos en los diferentes idiomas de este reglamento, la versión en inglés será la que prevalezca.",
                ":orange[***Art.28***:] Trata sobre: Entrada en vigor",
                ":orange[***Art.28***:] Este reglamento fue aprobado por el Consejo de la FIFA en su sesión del 16 de diciembre de 2022, y entró en vigor de la siguiente manera: a) El 9 de enero de 2023: Los artículos 1 a 10 y 22 a 27, que se relacionan en general con el procedimiento para obtener la licencia. b) El 1 de octubre de 2023: El resto de los artículos, que se relacionan en general con la actividad de los agentes de fútbol, así como con las obligaciones de los agentes de fútbol y los clientes. Especifica que la obligación de los clientes de solo contratar a un agente de fútbol para la prestación de servicios de representación será efectiva para todas las transacciones a partir del 1 de octubre de 2023.",
                ":orange[***Art.28***:] El Reglamento de la FIFA sobre las Relaciones con Intermediarios quedó revocado a partir del 1 de octubre de 2023."
            ]
        },
        {
            "titulo": ":books: Herramientas de Salvaguardia de la infancia del programa FIFA Guardians",
            "resumen": [
                "Texto resumen Herramientas de Salvaguardia..."
            ]
        }
    ]

    for seccion in secciones:
        with st.expander(seccion["titulo"]):
            for resumen in seccion["resumen"]:
                st.write(resumen)


if __name__ == "__main__":
    mostrar_resumenes()
