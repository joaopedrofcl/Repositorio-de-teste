import requests
import json

api = 'https://digimon-api.vercel.app/api/digimon/name/'
nome = input('digite o nome de Digimon: ')

digimon = requests.get(f'{api}{nome}')
digimon = digimon.json()

print(digimon)

