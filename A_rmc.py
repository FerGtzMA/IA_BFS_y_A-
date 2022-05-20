from collections import deque
import time
import matplotlib.pyplot as plt

class Graph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    # función para obtener los vecinos
    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # función heurística con valores iguales para todos los nodos
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1,
            'G': 1,
            'H': 1,
            'I': 1,
            'J': 1,
            'K': 1
        }

        return H[n]

    def A_estrella(self, start_node, stop_node):
        # open_list es una lista de los nodos que han sido visitados pero no tienen vecinos.
        # No se han inspeccionado todos y va a comenzar con el nodo inicio.
        open_list = set([start_node])

        # closed_list es una lista de nodos que han sido visitados.
        # Pero sus vecino sí han sido inspeccionados.
        closed_list = set([])

        # g contiene las distancias actuales desde el nodo inicial hacia los demás nodos
        # el valor definido (si no se encuentra en la grafica) será infinito positivo.
        g = {}

        g[start_node] = 0

        # Los padres contendran, aparte, un mada de adyacencia de todos los nodos
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # encuentra un nodo con el valor más bajo, con la uncion de evalucion
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('La ruta no existe!!')
                return None

            # si el nodo actual es una hoja entonces empezamos a recontruir la
            # ruta desde ahí hasta el nodo inicial
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('La mejor ruta: {}'.format(reconst_path))
                return reconst_path

            # for para todos los vecinos del nodo actual
            for (m, weight) in self.get_neighbors(n):
                # Si el nodo actual no está ni en la open_list ni en closed_list, 
                # lo agregamos a open_list y anotar n como su padre
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # Si no, verfificamos qué es más rápido ¿visitar primero n luego m?
                # Si es así, actualizamos los datos principales y los datos de la lista de distancias.
                # Y otro caso es que si el nodo estaba en la closed_lis, lo movemos a la open_list.
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # Eliminamos n de la open_list y lo agregamos a la closed_list
            # esto lo hacemos proque ya todos sus vecinos fueron inspeccionados
            open_list.remove(n)
            closed_list.add(n)

        print('La ruta no existe!!')
        return None

#------------------------------PRUEBAS----------------------------------
segundos = []
nombres = []

adjacency_list = {
    'A': [('B', 3), ('C', 2), ('D', 2)],
    'B': [('E', 5)],
    'C': [('B', 1), ('E', 2), ('F', 2), ('G', 7), ('D', 4)],
    'D': [('G', 1)],
    'E': [('F', 3), ('I', 4), ('H', 3)],
    'F': [('I', 5)],
    'G': [('F', 4), ('I', 1), ('J', 8)],
    'H': [('K', 1)],
    'I': [('J', 2), ('K', 8), ('H', 2)],
    'J': [('K', 3)]
}
prueba = Graph(adjacency_list)

for i in range(10):
    inicio = time.time()
    prueba.A_estrella('A', 'K')
    print("Timepo de ejecición de A a K: ",time.time()-inicio,"\n")

    segundos.append(time.time()-inicio)
    nombres.append(i+1)

fig, Tiem = plt.subplots()
Tiem.plot(nombres, segundos)
fig.suptitle('Tiempos')