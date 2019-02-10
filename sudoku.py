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
  p.problema(mat)



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

def printing(matriz):
  print("")
  for x in range(16):
    if (x % 4 == 0 and x != 0):
      print("\n___________________\n", end= "")
    print(matriz[int(x/4)][x % 4] + "  | ", end='')
  print("")

def heuristica(matriz):
  for x in range(4):
    
  
def actions(matriz):




if __name__ == "__main__":
  sudoku(sys.argv)
  pass