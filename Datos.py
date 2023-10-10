import requests
from translate import Translator

#Los chistes pueden tener preguntas y respuestas o solo una 
#frase, por lo que hay que tener en cuenta los diferentes campos
def textOutput(joke):
    if 'joke' in joke:
        return str(joke['joke'])
    else:
        return str(joke['setup']) + ' ' + str(joke['delivery'])

def printJoke(esp, category, flag, search):
    #URL https://v2.jokeapi.dev/joke/Programming?lang=es&blacklistFlags=religious
    #Categoría
    url='https://v2.jokeapi.dev/joke/'
    if category=="Programming":
        url+='Programming?'
    elif category=="Misc":
        url+='Misc?'
    elif category=="Dark":
        url+='Dark?'
    elif category=="Pun":
        url+='Pun?'
    elif category=="Spooky":
        url+='Spooky?'
    elif category=="Christmas":
        url+='Christmas?'
    else:
        url+='Any?'
    #Idioma
    if esp:
        url += 'lang=es'
    #Si no pones lang, el idioma por defecto es EN

    #Flags
    if flag=="nsfw":
        url+='&blacklistFlags=nsfw'
    elif flag=="religious":
        url+='&blacklistFlags=religious'
    elif flag=="political":
        url+='&blacklistFlags=political'
    elif flag=="racist":
        url+='&blacklistFlags=racist'
    elif flag=="sexist":
        url+='&blacklistFlags=sexist'
    elif flag=="explicit":
        url+='&blacklistFlags=explicit'

    #search
    if search!="":
        url+='&contains='+search
    #Guardamos la respuesta de la url en la variable joke
    joke = requests.get(url)

    #Convertimos la variable joke en un diccionario usando json()
    joke = joke.json()

    return textOutput(joke)

def translate(text):
    #Ponemos el proveedor mymemory y indicamos los idiomas
    translator = Translator(provider='mymemory', from_lang='en', to_lang='es')
    #Guardamos la traducción en translation
    return translator.translate(text)
    