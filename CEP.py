import requests
import json

pergunta = input('Digite seu cep sem os traços: \n')

requisao = requests.get(' https://cep.awesomeapi.com.br/json/'+str(pergunta))

endereco = json.loads(requisao.text)

conteudo = dict(endereco)

print('Rua: ', conteudo['address'])
print('Bairro: ', conteudo['district'])
print('Cidade: ', conteudo['city'])
print('Estado: ', conteudo['state'])
print('CEP: ', conteudo['cep'])
