import json
import requests


class Ingestiones():
    def __init__(self):
        self.ruta_static="src/pad/static/"
        
    def leer_api(self, url):
        response = requests.get(url)
        return response.json()
    
ingestion = Ingestiones() 
datos_json = ingestion.leer_api("https://api.github.com/users/octocat")
clima = ingestion.leer_api("https://api.github.com/users/octocat")
print(ingestion.ruta_static)
print(datos_json)
print("Ruta del clima:",clima)