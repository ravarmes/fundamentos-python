file = open('22-arquivos-texto-dados.txt', 'w+')
print('Escrevendo no arquivo txt...')
file.write('Linha 1\n')
file.write('Linha 2\n')

lista = list()
lista.append("Linha 3 \n")
lista.append("Linha 4 \n")
file.writelines(lista)

file.close()