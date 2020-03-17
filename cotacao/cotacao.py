import requests
import json


listar = open('listagem.txt')
print(listar.read())
listar.close()

pergunta = input('Digite a cotação desejada: \n')

requisao = requests.get('https://economia.awesomeapi.com.br/json/all/'+str(pergunta))

resposta = json.loads(requisao.text)
converter = dict(resposta)

for resultado in converter.values():
    print('Converter:', resultado['code'])
    print('Para: ', resultado['codein'])
    print('Valor atual: ', "R$"+resultado['bid'])
    print('Maior valor do dia até agora: ', "R$"+resultado['high'])
    print('Menor valor do dia até agora: ', "R$"+resultado['low'])
