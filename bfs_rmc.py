import heapq
import math
import time
import matplotlib.pyplot as plt

segundos = []
nombres = []

# Usamos un Diccionario que las llaves tienen como valor otro diccionario para la concatenación 
# de los valores, vertices y distancias
graph={
    "a":{"b":3,"c":2,"d":2},
    "b":{"a":3,"c":1,"e":5},
    "c":{"a":2,"b":1,"d":4,"e":2,"f":2,"g":7},
    "d":{"a":2,"c":4,"g":1},
    "e":{"b":5,"c":2,"f":3,"h":3,"i":4},
    "f":{"c":2,"e":3,"g":4,"i":5},
    "g":{"c":7,"d":1,"f":4,"i":1,"j":8},
    "h":{"e":3,"i":2,"k":1},
    "i":{"e":4,"f":5,"g":1,"h":2,"j":2,"k":8},
    "j":{"g":8,"i":2,"k":3},
    "k":{"h":1,"i":8,"j":3}
}

#Inicializamos el valor distancia desde el punto de inicio a cero hasta el 
#infinito a otros nodos
def init_distance(graph,s): # Imagen entrante y punto de partida
    distance={s:0}
    for vertex in graph:
        if vertex !=s:
            distance[vertex]=math.inf  # Excepto a sí mismo son infinitos
    return distance

def bfs(graph,s):
    #Creamos una cola
    pqueue=[]
    
    # Primero agregue un punto de partida a la cola y la clasificación la agremaos después.
    
    # El siguiente método organiza los elementos de acuerdo a la prioridad en la cola.
    heapq.heappush(pqueue,(0,s))
    
    #Guardamos los vertivces que han sido visitados
    visitado=set()
    
    # Marcar el nodo padre de cada nodo; Como este nodo es el nodo inicio NO tiene padre 
    padre={s:None}
    distance=init_distance(graph,s)

    while (len(pqueue)>0):
        
        # heapop devuelve la prioridad más alta, en este caso queremos la distancia más corta.
        pair=heapq.heappop(pqueue)  #Devuelve una tupla con el valor más pequeño
        distancia=pair[0]  #Extraemos la distancia
        vertex=pair[1] #Extraemos el nodo
        visitado.add(vertex) #Marcamos el nodo extraido como visitado
        nodes=graph[vertex].keys() ##Extraemos los nodos conectados al nodo actual

        # Algoritmo de núcleo
        for n in nodes:
            if n not in visitado:
                 #inicioNodoTime = time.time()
                 if distancia+graph[vertex][n] < distance[n]:

                     #Añadir la ruta mas corta a la cola y ordenar
                     heapq.heappush(pqueue,(distancia+graph[vertex][n],n))
                     padre[n]=vertex  #Registrar nodo principal
                    
                    # Actualizar la distancia desde el punto de inicio al nodo n
                     distance[n]=distancia+graph[vertex][n]
    return padre,distance

#Una función para conocer el camino de la ruta más corta del camino dado
def camino(graph,s,end):
    padre, distance = bfs(graph, s)
    preCamino=[end]  
    while padre[end] !=None:
        preCamino.append(padre[end])
        end=padre[end]
    preCamino.reverse()  
    return preCamino

#Corriendo el algoritmo
# inicia el tiempo
start, end = input("Introduzca los nodos inicial y final separados por espacios:").split()
tiempoTotal = 0
for i in range(10):
    inicio = time.time()
    padre,distance=bfs(graph,start)
    final = time.time()-inicio
    segundos.append(final)
    timepoTotal = tiempoTotal + final
    nombres.append(i+1)

print("El tiempo total de la misma instancia recorrida 10 veces es: ",timepoTotal)
# termina el tiempo y muestra cuánto tiempo tardó
#print("\nTiempo de ejecución: ", time.time()-inicio)

ruta=camino(graph,start,end)
print("La ruta de {} a {}:".format(start, end), ruta)
print("La distancia de {} a {}:".format(start,end),distance[end])

fig, Tiem = plt.subplots()
Tiem.plot(nombres, segundos)
fig.suptitle('Tiempos')