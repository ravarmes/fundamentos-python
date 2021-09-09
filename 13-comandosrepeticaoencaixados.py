#Demonstração do Laços Whiles Encaixados

linha = 1
coluna = 1

while (linha <= 10): 
    while (coluna <= 10):
        #Imprimi linha x coluna com tabulação no final 
        print ( linha * coluna, end="\t" ) 
        coluna = coluna + 1
    linha = linha + 1
    #Para saltar linha
    print() 
    coluna = 1

