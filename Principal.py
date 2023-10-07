import requests
from translate import Translator

#Los chistes pueden tener preguntas y respuestas o solo una 
#frase, por lo que hay que tener en cuenta los diferentes campos
def textOutput():
    if 'joke' in joke:
        return str(joke['joke'])
    else:
        return str(joke['setup']) + ' ' + str(joke['delivery'])

lang = input('Introduce el idioma:')

#Comprobamos el idioma seleccionado
if lang.lower() in ["español", "es", "spanish"]:
    url = 'https://v2.jokeapi.dev/joke/Any?lang=es'
    es=True
else:
    url = 'https://v2.jokeapi.dev/joke/Any?lang=en'
    es=False

#Guardamos la respuesta de la url en la variable joke
joke = requests.get(url)

#Convertimos la variable joke en un diccionario usando json()
joke = joke.json()

if es==False:
    #Ponemos el proveedor mymemory y indicamos los idiomas
    translator = Translator(provider='mymemory', from_lang='en', to_lang='es')
    #Guardamos la traducción en translation
    translation = translator.translate(textOutput())
    print (translation)
else:
    print(textOutput())