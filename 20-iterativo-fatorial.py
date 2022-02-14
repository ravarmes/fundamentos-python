def fat(n):
    resp = 1
    while (n != 0):
        resp = resp * n
        n = n - 1
    return resp


resultado = fat(40)
print("Fatorial: ", resultado)