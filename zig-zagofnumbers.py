def imprimir_zigzag(L, C):
    matriz = [[0] * C for _ in range(L)]
    numero = 1
    for i in range(L):
        if i % 2 == 0:
            for j in range(C):
                matriz[i][j] = numero
                numero += 1
        else:
            for j in range(C - 1, -1, -1):
                matriz[i][j] = numero
                numero += 1
    for i in range(L):
        print(' '.join(str(x) for x in matriz[i]))
L = int(input())
C = int(input())
imprimir_zigzag(L, C)