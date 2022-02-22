file = open('21-arquivos-texto-dados.txt', 'r')
print('Lendo linha por linha do arquivo txt:')
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

file.seek(0, 0)

print(file.readlines())

file.close()