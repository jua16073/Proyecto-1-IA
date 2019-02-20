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
    mat2 = f_mat.a_matriz("123456789ABCDE.F")
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
            nueva_matriz[posicion[0]][posicion[1]] = copy.deepcopy(nueva_matriz[posicion[0]-1][posicion[1]])
            nueva_matriz[posicion[0]-1][posicion[1]] = "."
            matrices.append(nueva_matriz)
        if posicion[0] + 1 <= 3:
            nueva_matriz = copy.deepcopy(matriz)
            nueva_matriz[posicion[0]][posicion[1]] = copy.deepcopy(nueva_matriz[posicion[0] + 1][posicion[1]])
            nueva_matriz[posicion[0] + 1][posicion[1]] = "."
            matrices.append(nueva_matriz)

        if posicion[1] - 1 >= 0:
            nueva_matriz = copy.deepcopy(matriz)
            nueva_matriz[posicion[0]][posicion[1]] = copy.deepcopy(nueva_matriz[posicion[0]][posicion[1] - 1])
            nueva_matriz[posicion[0]][posicion[1] - 1] = "."
            matrices.append(nueva_matriz)
        if posicion[1] + 1 <= 3:
            nueva_matriz = copy.deepcopy(matriz)
            nueva_matriz[posicion[0]][posicion[1]] = copy.deepcopy(nueva_matriz[posicion[0]][posicion[1] + 1])
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
        puntos_ganador = 0
        dist_restante = 1000
        for path in paths:
            estado = path[len(path)-1]
            contador = 0
            distancia = 0
            puntos = 0
            while contador < 15:
                distancia += self.revisar(estado, contador)
                if contador == 3 and distancia == 0:
                    puntos += 1
                if contador == 7 and distancia == 0:
                    puntos += 1
                contador += 1
            if puntos > puntos_ganador:
                puntos_ganador = puntos
                dist_restante = distancia
                path_seleccionado = path
            elif puntos == puntos_ganador and distancia < dist_restante:
                dist_restante = distancia
                path_seleccionado = path
        print(puntos_ganador)
        print(dist_restante)
        return path_seleccionado

    def revisar(self, matriz, num):
        x = int(num / 4)
        y = int(num - (x * 4))
        distancia = None
        for h in range(4):
            for k in range(4):
                if matriz[h][k].lower() == str(hex(num + 1).split('x')[-1]):
                    distancia = (math.sqrt(math.pow((h - x), 2) + math.pow((k - y), 2)))
        return distancia


# Para empezar
if __name__ == "__main__":
    inicio(sys.argv)
    pass
# A59427.8F16CD3BE
# F21C856B49A73ED.
