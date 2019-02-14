#Proyecto 1 de IA
#Parte de Sudoku
#Rodrigo Juárez 16073

#Libreria para tomar argumentos de consola
import sys
import problems as p

#inicio del programa
def sudoku(argv):
  if (len(argv[1]) != 16):
    print("No es un sudoku de 4x4")
    return (0)
  mat = a_Matriz(argv[1])
  print(mat)
  printing(mat)
  #p.problema(mat)
  print(win_Condition(mat))
  actions(mat)


## Funcion para pasar de un vector a una matriz
def a_Matriz(inicial):
  x = 0
  y = 0
  filas = []
  completo = []
  for i in inicial:
    filas.append(i)
    x += 1
    if ( x % 4 ==0 ):
      completo.append(filas)
      filas = []
  return completo


##Funcion para imprimir la matriz como un sudoku
def printing(matriz):
  print("")
  for x in range(16):
    if (x % 4 == 0 and x != 0):
      print("\n___________________\n", end= "")
    print(matriz[int(x/4)][x % 4] + "  | ", end='')
  print("")

## Funcion para designar a cual paso darle prioridad
def heuristica1(matriz):
  points = 0
  for x in range(4):
    nums = 0
    for y in range(4):
      if (matriz[x][y] != "."):
        nums +=1
    points += nums * nums

  for x in range(4):
    nums = 0
    for y in range(4):
      if (matriz[y][x] != "."):
        nums +=1
    points += nums * nums
  return points

  
def actions(matriz):
  espacios = 0
  posiciones = []
  posibilidades = []
  # Encontrar cuantos espacios vacios hay
  for x in range(4):
    for y in range(4):
      if (matriz[x][y] == "."):
        posiciones.append(tuple([x,y]))
        espacios +=1
  print(posiciones)
  
  #Sacar cada una de las posibilidades
  cont = 0
  while(cont<espacios):
    nums = ["1","2","3","4"]
    for x in range(4):
      if (matriz[posiciones[cont][0]][x] != "."):
        nums.remove(matriz[posiciones[cont][0]][x])

    for x in range(4):
      if (matriz[x][posiciones[cont][1]] != "." and (matriz[x][posiciones[cont][1]] in nums) ):
        nums.remove(matriz[x][posiciones[cont][1]])
    posibilidades.append(nums)
    print(nums)
    cont += 1

def win_Condition(matriz):
  # Comprobar si estan todos en las filas
  for x in range(4):
    nums = ["1", "2", "3", "4"]
    for y in range(4):
      if (matriz[x][y] in nums):
        nums.remove(matriz[x][y])
    if (len(nums) != 0):
      return False

  #Comprobar si estan todos en las columnas
  for x in range(4):
    nums = ["1", "2", "3", "4"]
    for y in range(4):
      if (matriz[y][x] in nums):
        nums.remove(matriz[y][x])
    if (len(nums) != 0):
      return False

  #Comprobar si estan todos en los cuadros 
  h = 0
  k = 0
  i = 0
  while (i < 4):
    if (i == 1):
      k = 2
    if (i == 2):
      k = 0
      h = 2
    if (i == 3):
      k = 2
      h = 2
    for x in range(2):
      for y in range(2):
        if( matriz[x+h][y+k] in nums ):
          nums.remove(matriz[x+h][y+k])
    if (len(nums) != 0):
        return False
    i +=1 

  return True
    
  
  


##Para empezar 
if __name__ == "__main__":
  sudoku(sys.argv)
  pass