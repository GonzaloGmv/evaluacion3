def determinante_recursivo(matriz, i, solucion):
    if i == 0:
        determinante_recursivo(matriz, i+1, matriz[0][0] * matriz[1][1] * matriz[2][2] + solucion)
    elif i == 1:
        determinante_recursivo(matriz, i+1, matriz[0][1] * matriz[1][2] * matriz[2][0] + solucion)
    elif i == 2:
        determinante_recursivo(matriz, i+1, matriz[1][0] * matriz[2][1] * matriz[0][2] + solucion)
    elif i == 3:
        determinante_recursivo(matriz, i+1, solucion - matriz[0][2] * matriz[1][1] * matriz[2][0])
    elif i == 4:
        determinante_recursivo(matriz, i+1, solucion - matriz[0][1] * matriz[1][0] * matriz[2][2])
    elif i == 5:
        solucion = solucion - matriz[0][0] * matriz[2][1] * matriz[1][2]
        print(solucion)

def determinante_iterativo(matriz):
    solucion = 0
    for i in range(6):
        if i == 0:
            solucion = matriz[0][0] * matriz[1][1] * matriz[2][2] + solucion
        elif i == 1:
            solucion = matriz[0][1] * matriz[1][2] * matriz[2][0] + solucion
        elif i == 2:
            solucion = matriz[1][0] * matriz[2][1] * matriz[0][2] + solucion
        elif i == 3:
            solucion = solucion - matriz[0][2] * matriz[1][1] * matriz[2][0]
        elif i == 4:
            solucion = solucion - matriz[0][1] * matriz[1][0] * matriz[2][2]
        elif i == 5:
            solucion = solucion - matriz[0][0] * matriz[2][1] * matriz[1][2]
            return solucion
