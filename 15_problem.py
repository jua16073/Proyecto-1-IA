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
    # mat = f_mat.a_matriz("123456789ABCDFE.")
    # mat = f_mat.a_matriz("B1E5C73F294D.A68")
    if es_posible(argv[1]):
        print("Es resoluble")
        mat = f_mat.a_matriz(argv[1])
        f_mat.printing(mat)
        problema = Problem15()
        problema.inicial = mat
        respuesta = p.graph_search(problema)
        print("Termino")
        for x in respuesta:
            f_mat.printing(x)
    else:
        print("No se puede resolver")


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
                if puntos == 2 and estado[2][0] == "9" and estado[3][0] =="D":
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


def es_posible(inicial):
    paridad = 0
    ancho = math.sqrt(len(inicial))
    fila = 0
    fila_vacio = 0
    print(len(inicial))

    for i in range(len(inicial)):
        if i % ancho == 0:
            fila += 1
        if inicial[i] == ".":
            fila_vacio = copy.deepcopy(fila)
        for j in range(i+1, len(inicial)):
            if inicial[i] > inicial[j] and (inicial[j] != "."):
                paridad += 1
    print(paridad)
    if ancho % 2 == 0:
        if fila_vacio % 2 == 0:
            return paridad % 2 == 0
        else:
            return paridad % 2 != 0
    else:
        return paridad % 2 == 0


# Para empezar
if __name__ == "__main__":
    inicio(sys.argv)
    pass
# A59427.8F16CD3BE
# F21C856B49A73ED.
# B1E5C73F294D.A68 Exito en 5-6 mins aprox
# 98B2AC3.4ED75F61 Exito en 1:32 mins aprox
# D356E27BAFC481.9 Exito en 5 mins aprox
# 2F.D4BACE8913765 Exito en 2:17 mins aprox
# Unsolvable 123456789ABCDFE.

