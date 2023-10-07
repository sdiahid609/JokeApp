import requests
from translate import Translator

#Los chistes pueden tener preguntas y respuestas o solo una 
#frase, por lo que hay que tener en cuenta los diferentes campos
def textOutput(joke):
    if 'joke' in joke:
        return str(joke['joke'])
    else:
        return str(joke['setup']) + ' ' + str(joke['delivery'])

def printJoke():
    url = 'https://v2.jokeapi.dev/joke/Any?lang=es'

    #Guardamos la respuesta de la url en la variable joke
    joke = requests.get(url)

    #Convertimos la variable joke en un diccionario usando json()
    joke = joke.json()

    return textOutput(joke)