import json

json_file = open("22-arquivos-json-dados.json", 'r', encoding='utf-8')
dados = json.load(json_file)


# para cada item do arquivo json
for i in dados:

    # imprimindo nome e idade formatados
    print(i['nome'], 'tem', i['idade'], 'anos.')

