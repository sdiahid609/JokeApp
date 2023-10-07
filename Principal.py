import requests

lang = input('Introduce el idioma:')

#Comprobamos el idioma seleccionado
if lang.lower() in ["español", "es", "spanish"]:
    url = 'https://v2.jokeapi.dev/joke/Any?lang=es'
else:
    url = 'https://v2.jokeapi.dev/joke/Any?lang=en'

#Guardamos la respuesta de la url en la variable joke
joke = requests.get(url)

#Convertimos la variable joke en un diccionario usando json()
joke = joke.json()

#Los chistes pueden tener preguntas y respuestas o solo una 
#frase, por lo que hay que tener en cuenta los diferentes campos
if 'joke' in joke:
    print (str(joke['joke']))
else:
    print (str(joke['setup']))
    print (str(joke['delivery']))