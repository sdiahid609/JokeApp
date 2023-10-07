import requests

#Llamamos a la api y metemos la respuesta en data
url = 'https://v2.jokeapi.dev/joke/Any?lang=en'
data = requests.get(url)
data = data.json()
if 'joke' in data:
    print (str(data['joke']))
else:
    print (str(data['setup']))
    print (str(data['delivery']))