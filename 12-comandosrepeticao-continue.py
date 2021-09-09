#Demonstração do continue
#Inicializa cont com 0 
cont = 0 
#Laço de 0 até 9
while (cont < 10): 
    #Incrementa cont
    cont = cont + 1 
    #Checa se cont x 5 é múltiplo de 2
    if ((cont * 5) % 2 == 0): 
        #Pule esta iteração se cont x 5 for um múltiplo de 2 
        continue
    #Imprime cont x 5 ​
    print (cont * 5)
