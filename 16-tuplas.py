#Demonstração sobre Tuplas
#Inicializando algumas tuplas
tupla1 = (23, 6+9j, 'Motorola', 5.66, 'Mouse')
tupla2 = ('GM', -3.6, 7)

#Encontrando tamanhos das tuplas
t1 = len (tupla1) 
t2 = len (tupla2) 

#Exibindo as tuplas usando print e elemento por elemento usando while 
print ("\nTupla 1\n", tupla1) 
print ("\nTupla 2\n", tupla2) 

print ("\nExibindo elemento por elemento usando while") 
i = 0 
print ("\nTupla 1") 
while (i < t1):
    print("Índice:", i, "Elemento:", tupla1[i])
    i = i + 1 

i = 0 
print ("\nTupla 2") 
while (i < t2):
    print("Índice:", i, "Elemento:", tupla2[i])
    i = i + 1 

#Concatenando 
tupla3 = tupla1 + tupla2
print ("\nTupla 3\n", tupla3) 

#Executando várias operações de fatiamento 
print ("\nOperações de fatiamento em tuplas") 
print(tupla3[6:])
print(tupla1[:3])
print(tupla3[1:5])
print(tupla2[2])
print(tupla3[3:6])

