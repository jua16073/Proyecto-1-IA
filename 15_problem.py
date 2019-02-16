# Rodrigo Juarez
# 15 Problem
# 15-2-2018
import matriz as f_mat
import sys
import copy
import math
import problems as p


def inicio(argv):
    if len(argv[1]) != 16:
        return "No es un input valido"
    mat = f_mat.a_matriz(argv[1])
    f_mat.printing(mat)
    problema = Problem15()
    problema.inicial = mat
    respuesta = p.graph_search(problema)
    print("Termino")
    for x in respuesta:
        f_mat.printing(x)


class Problem15:
    inicial = "Estado inicial"

    def actions(self, matriz):
        matrices = []
        for x in range(4):
            for y in range(4):
                if matriz[x][y] == ".":
                    posicion = tuple((x, y))
        if posicion[0] - 1 >= 0:
            nueva_matriz = copy.deepcopy(matriz)
            nueva_matriz[posicion[0]][posicion[1]] = nueva_matriz[posicion[0]-1][posicion[1]]
            nueva_matriz[posicion[0]-1][posicion[1]] = "."
            matrices.append(nueva_matriz)
        if posicion[0] + 1 <= 3:
            nueva_matriz = copy.deepcopy(matriz)
            nueva_matriz[posicion[0]][posicion[1]] = nueva_matriz[posicion[0] + 1][posicion[1]]
            nueva_matriz[posicion[0] + 1][posicion[1]] = "."
            matrices.append(nueva_matriz)

        if posicion[1] - 1 >= 0:
            nueva_matriz = copy.deepcopy(matriz)
            nueva_matriz[posicion[0]][posicion[1]] = nueva_matriz[posicion[0]][posicion[1] - 1]
            nueva_matriz[posicion[0]][posicion[1] - 1] = "."
            matrices.append(nueva_matriz)
        if posicion[1] + 1 <= 3:
            nueva_matriz = copy.deepcopy(matriz)
            nueva_matriz[posicion[0]][posicion[1]] = nueva_matriz[posicion[0]][posicion[1] + 1]
            nueva_matriz[posicion[0]][posicion[1] + 1] = "."
            matrices.append(nueva_matriz)

        return matrices

    def win_condition(self, matriz):
        numero = 1
        for x in range(4):
            for y in range(4):
                if numero != 16:
                    if matriz[x][y].lower() != str(hex(numero).split('x')[-1]):
                        return False
                numero += 1
        return True

    def criteria(self, paths):
        path_seleccionado = None
        distancia_minima = None
        for path in paths:
            estado = path[len(path)-1]
            distancia = 0
            contador = 0
            bonus = .5
            while contador < 15:
                x = int(contador/4)
                y = int(contador - (x*4))
                for h in range(4):
                    for k in range(4):
                        if estado[h][k].lower() == str(hex(contador+1).split('x')[-1]):
                            this = (math.sqrt(math.pow((h-x), 2) + math.pow((k-y), 2)))
                            distancia += this
                contador += 1
            if distancia_minima is None:
                distancia_minima = distancia
                path_seleccionado = path
            elif distancia < distancia_minima:
                distancia_minima = distancia
                path_seleccionado = path
        print(distancia_minima)
        return path_seleccionado


# Para empezar
if __name__ == "__main__":
    inicio(sys.argv)
    pass
