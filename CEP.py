import requests
import json

pergunta = input('Digite o seu cep sem os traços: \n')

requisao = requests.get(' https://cep.awesomeapi.com.br/json/'+str(pergunta))

endereco = json.loads(requisao.text)

print('Rua : ', endereco['address'])
print('Bairro: ', endereco['district'])
print('Cidade: ', endereco['city'])
print('Estado: ', endereco['state'])
print('CEP: ', endereco['cep'])
