import copy
import matriz as m

def graph_search(problema):
    frontera = []
    explorado = []
    path = []
    estado = problema.inicial
    path.append(estado)
    frontera.append(path)
    estados_visitados = 0

    while True:
        if len(frontera):
            path = problema.criteria(frontera)
            estado = path[len(path)-1]
            explorado.append(estado)
            frontera.remove(path)
            m.printing(estado)
            #print(len(frontera))
            #estados_visitados += 1
            #print(estados_visitados)

            if problema.win_condition(estado):
                return path

            probabilidades = problema.actions(estado)
            for a in probabilidades:
                if a not in explorado:
                    new_path = copy.deepcopy(path)
                    new_path.append(a)
                    frontera.append(new_path)
        else:
            return False


