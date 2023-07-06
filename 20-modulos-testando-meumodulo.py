#Demonstração do módulo definido pelo usuário
#Importando meumodulo.py
import meumodulo

x = 5
y = 7
z = -3

#Chamando as funções do meumodulo
meumodulo.mostrar_soma(x, y, z) 
dif = meumodulo.calcular_diferenca(x, y) 
prod = meumodulo.calcular_produto(x, y, z) 
quo = meumodulo.calcular_quociente(x, y) 

#Mostrando os resultados 
print ("\nDentro de 19-modulos-testando-meumodulo.py\n",
       "\nDiferença = ", dif, 
       "\nProduto = ", prod, 
       "\nQuociente = ", quo)

