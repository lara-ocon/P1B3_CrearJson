# Practica1Bloque3
Pasar leaks a un fichero json - Adquisición de Datos - IMAT
Autor : Lara Ocón Madrid


Para esta práctica vamos a tomar el csv con los leaks obtenidos en la práctica 1 (obtenido al ejecutar el fichero "git_leaks.py") a un fichero json.

Para ello, vamos a emplear una estructura ETL:

1) Extraemos el csv obtenido en la práctica de git leaks donde encontramos cada mensaje con su hash.

2) Tranformamos los datos, pasando toda la información a un diccionario del tipo {hash : mensajes}

3) Cargamos el diccionario de un fichero json : "leaks.json"
