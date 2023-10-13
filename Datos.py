import requests
from translate import Translator

#Los chistes pueden tener preguntas y respuestas o solo una 
#frase, por lo que hay que tener en cuenta los diferentes campos
def textOutput(joke):
    if 'joke' in joke:
        return str(joke['joke'])
    else:
        return str(joke['setup']) + ' ' + str(joke['delivery'])

def printJoke(self, category, search):
    #URL https://v2.jokeapi.dev/joke/Programming?lang=es&blacklistFlags=religious
    #Categoría
    esp = self.esp
    url='https://v2.jokeapi.dev/joke/'
    if category=="Programación":
        url+='Programming?'
    elif category=="Misc":
        url+='Misc?'
    elif category=="Oscuro":
        url+='Dark?'
    elif category=="Escalofriante":
        url+='Spooky?'
    elif category=="Navidad":
        url+='Christmas?'
    else:
        url+='Any?'
    #Idioma
    if esp:
        url += 'lang=es'
    #Si no pones lang, el idioma por defecto es EN

    #search
    if search!="":
        url+='&contains='+search
    #Guardamos la respuesta de la url en la variable joke
    joke = requests.get(url)
    #Comprobamos si la api devuelve datos
    if joke.status_code == 200:
        #Convertimos la variable joke en un diccionario usando json()
        joke = joke.json()

        return textOutput(joke)
    else:
        return textOutput("No hemos podido encontrar ningún chiste con las características requeridas o no ha habido respuesta, lo sentimos.")

def translate(text):
    #Ponemos el proveedor mymemory y indicamos los idiomas
    translator = Translator(provider='mymemory', from_lang='en', to_lang='es')
    #Guardamos la traducción en translation
    return translator.translate(text)
