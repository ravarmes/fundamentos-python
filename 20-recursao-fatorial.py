def fat(n):
    if (n == 0):
        return 1
    else:
        return n*fat(n-1)


resultado = fat(40)
print("Fatorial: ", resultado)