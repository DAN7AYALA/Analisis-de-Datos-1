# Grupo 2 - Talento Tech
* Wallking Yalid Sepúlveda
* Daniel Mauricio Ayala Gamba

Reunión virtual 20/03/2024
- Distribución de Trabajo para la primera entrega, cada integrante inicia la arquitectura de la página y envía para revisión.
- El diseño sera seleccionado de acuerdo con cada propuesta.

Reunión virtual 05/04/2024
- Socializar el Backend y distribución de trabajo para realizar segunda entrega el 10 de Abril.
- Se sube a GitHub.

06/04/2024
Se realizan las siguientes modificaciónes:
- Nombre de la pestaña de la pagina
- En el Index.html, se conectó el botón "consultar" con la pagina que se desea cargar
- En el Index.html, se deja comentario sobre los miembros del equipo
- Se cambio el nombre de una pagina que será la que cargue al momento de consultar "Data_Analist.html"
- Se incluye en el "Navbar & Hero Start" la interconexion de paginas.
- En el Data_Analist.html, se incluyo una barra y boton donde se debe cargar el dataset del usuario.
- En el Data_Analist.html, Se creó botones para solicitar el tipo de analisis que desea el usuario
Nota: Ninguno de los botones está funcional.
Nota 2: Las partes modificadas se cometaron y existen otras que no se eliminaron porque podrian llegar a usarse más adelante.

09/04/2024
Se realizan las siguientes modificaciónes:
- Se incluye una pagina de visualizacióon de resultados "Dashboard".
- Se ajusta la pagina para su funcionamiento y conexión entre el inicio y el cargue de datos.
- Se modifica para que esté acorde con el modelo de front que se esta trabajando.
- Se realiza cambios en los botones de carga de datos, para que se pueda seleccionar el archivo en el pc del usuario.
- Se cambia los botones de seleción de modelo de analisis, para que el usuario tenga la libertad de escoger uno o varios modelos.

14/04/2024
Se inicia con el desarrollo del Backend
- Se crea la función que me ayudará a cargar el archivo
- Se añade la función de seleccionar el tipo de solicitud para la predicción.
- Se crea el back en y la API corespendiente
- Se comenta la sección del front donde se selecciona la tecnica y se coloca unicamente de unica slección, con el fin de probar que si funcione
- Se debe tener encuenta por donde se envía la solicitud en el enviar.js (por ahora esta en el puerto 50001)
(recordar que se puede ejecutar con ese puerto con el comando "flask run --port=5001")
- PENDIENTE: resolver error de respuesta en el boton al subir el archivo

15/04/2024
Se trabaja sobre los modelos
- Se intenta exportar los modelos, pero no se logra (aparentemete es por el dataset)
- Se modifica el app.ppy, para que cargue el archivo y responda a la solicitud del modelo (presenta problema, porque o se tiene el modelo exportado)
- Se hace validación de las condiciones para el uso de la planitilla del front modificado para no caer en derechos de Autor
- Se ajusta el footer para que tenga el nombre de la pagina y que conserve los derechos de Autor
- Se deja funcional el boton del footer de nombre reservado
- Se modicifo otro acceso al sitio para que incluyera un apartado sobre el tipo de proecto, la descripción y que se usó para desarrollarlo 


17/04/2024
Se trabaja sobre los modelos y se entrenan quedando con una presición de Knn = 76,45% y Ann = 82,59%
- Se exportan dos modelos (Knn y Ann)
- Se recibió tutoria relacionada con el proyecto y los errores que presentaba; así como, los modelos y la presición de los mismos.

22/04/2024
Se trabaja en el modelo de Regresión, se exporta con una presición 82,23%

27/04/2024
Se realiza revisión del codigo en la parte del back.
- Se modifican los llamados y solicitudes del app.py
- Se validan los llamados a los modelos
- Se integran los resultados al dashboard.html

07/05/2024
Se realizan cambios y ajustes sobre las paginas, para visualizar mejor la información