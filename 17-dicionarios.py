#Demonstração sobre Dicionários
#Inicializando alguns dicionários
dados_empregado = {'id': 1023, 'nome': 'Maria', 'idade': 29} 
exemplo_dic = {'xyz': 534, 2 + 3j: 'aaa', 5.4: 425, (1, 2, 3): [4, 5, 6]} 
print ( "\ndados_empregado:", dados_empregado, 
        "\nchaves:", dados_empregado.keys (), 
        "\nvalores:", dados_empregado.values ( ), 
        "\n\nexemplo_dic:", exemplo_dic, 
        "\nchaves:", exemplo_dic.keys (), 
        "\nvalores:", exemplo_dic.values ()) 

#Alter nome de dados_empregado
dados_empregado ['nome'] = 'José' 

#Excluir chave de idade 
del dados_empregado ['idade'] 

#Adicionar chave de país e valores 
dados_empregado ['país'] = "Brasil" 

#Print usando loop
print ("\ndados_empregado atualizado:") 
for key_var in dados_empregado: 
    print (" Chave: ", key_var," \tValor: ", dados_empregado [key_var])

