import json

file = open('teste.json', 'r')
dic1_json = file.read()
dic1_json = json.loads(dic1_json)

print(dic1_json)

for chave, valor in dic1_json.items():
    print(chave, ' = ', valor)
