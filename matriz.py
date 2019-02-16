# Funcion para pasar de un vector a una matriz
def a_matriz(inicial):
    x = 0
    filas = []
    completo = []
    for i in inicial:
        filas.append(i)
        x += 1
        if x % 4 == 0:
            completo.append(filas)
            filas = []
    return completo


# Funcion para imprimir la matriz como un sudoku
def printing(matriz):
    print("")
    for x in range(16):
        if (x % 4 == 0 and x != 0):
            print("\n___________________\n", end="")
        print(matriz[int(x / 4)][x % 4] + "  | ", end='')
    print("")