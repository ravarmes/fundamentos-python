#Demonstração sobre Listas 
#Inicializando algumas listas
lista1 = [23, 6+9j, 'Motorola', 5.66, 'Mouse'] 
lista2 = ['GM', -3.6, 7] 

#Encontrando tamanhos das listas
t1 = len (lista1) 
t2 = len (lista2) 

#Exibindo as listas usando print e elemento por elemento usando while 
print ("\nLista 1\n", lista1) 
print ("\nLista 2\n", lista2) 

print ("\nExibindo elemento por elemento usando while") 
i = 0 
print ("\nLista 1") 
while (i < t1):
    print("Índice:", i, "Elemento:", lista1[i])
    i = i + 1 

i = 0 
print ("\nLista 2") 
while (i < t2):
    print("Índice:", i, "Elemento:", lista2[i]) 
    i = i + 1 

#Concatenando 
lista3 = lista1 + lista2 
print ("\nLista 3\n", lista3) 

#Executando várias operações de fatiamento 
print ("\nOperações de fatiamento em listas") 
print(lista3[6:])
print(lista1[:3])
print(lista3[1:5])
print(lista2[2])
print(lista3[3:6])

