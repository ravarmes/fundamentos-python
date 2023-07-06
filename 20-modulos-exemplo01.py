#Demonstração sobre Módulos
#Importando os and math 
import os 
import math 

#Executando funções matemáticas 
fat = math.factorial(5) 
sen = math.sin(2 * math.pi / 3) 

#Encontrando o diretório de trabalho atual usando o módulo os 
cwd = os.getcwd() 

#Exibindo os resultados 
print("\nDiretório de trabalho: ", cwd, 
      "\nFatorial (5): ", fat, 
      "\nSeno (2 x (pi / 3)): ", sen)

