import json

json_file = open("21-arquivos-json-dados.json", 'r')
dados = json.load(json_file)

print(dados) 
# [{'nome': 'José', 'idade': 25}, {'nome': 'Maria', 'idade': 19}]
