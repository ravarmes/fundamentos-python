#Positivo, negativo, zero 
#Comando para entrada de dados do usuário
x_str = input ('Digite um número: ') 
#Converte a entrada para int
num = int (x_str) 
#Checa se num é positivo, negativo ou zero
#Checa se num é maior que 0
if (num > 0): 
    #Instruções executadas se num é maior que 0
    print ("O número: ", num, " é positivo.\n") 
#Checa se num é menor que 0 
elif (num < 0): 
    #Instruções executadas se num é menor que 0 
    print ("O número: ", num, " é negativo.\n")
#Se num não for positivo nem negativo, é 0 
else: 
    #Instruções executadas se num é igual a 0
    print ("O número: ", num, " é zero.\n")

