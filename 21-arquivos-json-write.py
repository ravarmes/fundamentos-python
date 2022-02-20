import json

dic1 = {
    'Pessoa 1':{
        'nome': 'Alberto',
        'idade': 10
    },
    'Pessoa 2':{
        'nome': 'Bernardo',
        'idade': 20
    }
}

dic1_json = json.dumps(dic1, indent=True)
print(dic1_json)

file = open('teste.json', 'w+')
file.write(dic1_json)
