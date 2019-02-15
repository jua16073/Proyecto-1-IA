# Proyecto 1 de IA
# Parte de Sudoku
# Rodrigo Juárez 16073

# Libreria para tomar argumentos de consola
import sys
import problems as p
import copy

# inicio del programa


def sudoku(argv):
    if len(argv[1]) != 16:
        print("No es un sudoku de 4x4")
        return 0
    mat = a_matriz(argv[1])
    problem = sudoku_problem()
    problem.inicial = mat

    respuesta = p.graph_search(problem)
    if not respuesta:
        print(respuesta)
    else:
        for x in respuesta:
            printing(x)

class sudoku_problem:
    inicial = "Colocar estado inicial"

    def actions(self,matriz):
        espacios = 0
        posiciones = []
        posibilidades = []
        matrices = []
        # Encontrar cuantos espacios vacios hay
        for x in range(4):
            for y in range(4):
                if matriz[x][y] == ".":
                    posiciones.append(tuple([x, y]))
                    espacios += 1

        # Sacar cada una de las posibilidades
        cont = 0
        while cont < espacios:
            nums = ["1", "2", "3", "4"]
            for x in range(4):
                if matriz[posiciones[cont][0]][x] != ".":
                    nums.remove(matriz[posiciones[cont][0]][x])

            for x in range(4):
                if matriz[x][posiciones[cont][1]] != "." and (matriz[x][posiciones[cont][1]] in nums):
                    nums.remove(matriz[x][posiciones[cont][1]])
            posibilidades.append(nums)
            cont += 1

        cont = 0
        while cont < espacios:
            for x in posibilidades[cont]:
                nueva_matriz = copy.deepcopy(matriz)
                nueva_matriz[posiciones[cont][0]][posiciones[cont][1]] = x
                matrices.append(nueva_matriz)
            cont += 1
        return matrices

    def win_condition(self, matriz):
        # Comprobar si estan todos en las filas
        for x in range(4):
            nums = ["1", "2", "3", "4"]
            for y in range(4):
                if matriz[x][y] in nums:
                    nums.remove(matriz[x][y])
            if len(nums) != 0:
                return False

        # Comprobar si estan todos en las columnas
        for x in range(4):
            nums = ["1", "2", "3", "4"]
            for y in range(4):
                if matriz[y][x] in nums:
                    nums.remove(matriz[y][x])
            if len(nums) != 0:
                return False

        # Comprobar si estan todos en los cuadros
        h = 0
        k = 0
        i = 0
        while i < 4:
            if i == 1:
                k = 2
            if i == 2:
                k = 0
                h = 2
            if i == 3:
                k = 2
                h = 2
            for x in range(2):
                for y in range(2):
                    if matriz[x + h][y + k] in nums:
                        nums.remove(matriz[x + h][y + k])
            if len(nums) != 0:
                return False
            i += 1

        return True

    def criteria(self,paths):
        path_seleccionado = None;
        points_winner = 0
        for x in paths:
            estado = x[len(x) - 1]
            points = 0

            for h in range(4):
                nums = 0
                for y in range(4):
                    if estado[h][y] != ".":
                        nums += 1
                points += nums * nums

            for h in range(4):
                nums = 0
                for y in range(4):
                    if estado[y][h] != ".":
                        nums += 1
                points += nums * nums
            if points > points_winner:
                path_seleccionado = x
                points_winner = points
        return path_seleccionado


# Funcion para pasar de un vector a una matriz
def a_matriz(inicial):
    x = 0
    y = 0
    filas = []
    completo = []
    for i in inicial:
        filas.append(i)
        x += 1
        if (x % 4 == 0):
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


# Para empezar
if __name__ == "__main__":
    sudoku(sys.argv)
    pass
