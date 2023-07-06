# Definição de função 
def calc(a, b): 
    # Calcula soma, diferença, produto e quociente
    s = a + b 
    d = a - b 
    p = a * b 
    q = a / b 
    # Retorna soma, diferença, produto e quociente 
    return s, d, p, q 

# Chamada de função 
# Os valores serão recebidos na ordem em que forem devolvidos 
som, dif, pro, quo = calc (10, 20)

