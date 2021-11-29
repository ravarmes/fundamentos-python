#Demonstração sobre operações com Strings
#Inicializa duas Strings
exemplo_str = "Este é um exemplo de string"
saudacao_str = "Olá!"

#Mostrando as Strings e seus comprimentos
print("String 1:", exemplo_str, "; Tamanho da String 1:", len(exemplo_str))
print("String 2:", saudacao_str, "; Tamanho da String 2:", len(saudacao_str))

#Concatenação 
s = saudacao_str + " " + exemplo_str
print("\nString 1 e 2 concatenadas: ", s, "; Tamanho da String s:", len(s)) 

#Mostrando resultados de diferentes operações com substrings 
print("\nDiferentes operações com substrings:") 
print(exemplo_str[5:], "\n", saudacao_str[:3], "\n", s[12:25], "\n", saudacao_str[3])

#Mostrando strings em maiúsculas e minúsculas 
print("\nMaiúsculas: ", exemplo_str.upper(), "\nMinúsculas: ", s.lower()) 

