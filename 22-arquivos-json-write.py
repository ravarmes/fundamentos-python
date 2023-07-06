import json

# Formando uma lista de dicionários de pessoas
dados = [
            {
                'nome': 'Jonas',
                'idade': 10
            },
            {
                'nome': 'Bernardo',
                'idade': 20
            }
        ]

# Abrindo um arquivo JSON para escrita (apagando o conteúdo antigo)
json_file = open('22-arquivos-json-dados.json', 'w')

# Escrevendo o conteúdo da variável 'dados' no arquivo json_file
json.dump(dados, json_file, indent=True)

