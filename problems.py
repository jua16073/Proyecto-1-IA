# archivo para generar el grafo del problema.
# inicio, acciones, heuristica


def graph_search(problema):
    frontera = []
    explorado = []
    estado = problema.inicial
    frontera.append(estado)

    while True:
        if len(frontera):
            path = problema.criterio(frontera)
            frontera.remove(path)
            estado = path[len(path)-1]
            explorado.append(frontera[len(frontera)-1])

        if problema.win_condition(estado):
            return path

        probabilidades = problema.acciones(estado)
        for a in probabilidades:
            if a not in explorado:
                new_path = path
                new_path.append(a)
                frontera.append(new_path)
        else:
            return False


