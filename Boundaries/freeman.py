import sys
import numpy as np

nuevo_limite = 10000  # Puedes ajustar este valor según tus necesidades
sys.set_int_max_str_digits(nuevo_limite)

def next_index_in_neighbourhood(x, y, connectivity, direction):
    # Siguiente indice en la vecindad de un pixel dependiendo la conectividad
    dx, dy = dir_to_coord(direction, connectivity)
    next_x = x + dx
    next_y = y + dy
    return next_x, next_y


def dir_to_coord(direction, connectivity):
    # Marcar la direcciones a coordenadas
    if connectivity == 4:
        if direction == 0:
            dx = 0
            dy = 1
        if direction == 1:
            dx = -1
            dy = 0
        if direction == 2:
            dx = 0
            dy = -1
        if direction == 3:
            dx = 1
            dy = 0

    elif connectivity == 8:
        if direction == 0:
            dx = 0
            dy = 1
        if direction == 1:
            dx = -1
            dy = 1
        if direction == 2:
            dx = -1
            dy = 0
        if direction == 3:
            dx = -1
            dy = -1
        if direction == 4:
            dx = 0
            dy = -1
        if direction == 5:
            dx = 1
            dy = -1
        if direction == 6:
            dx = 1
            dy = 0
        if direction == 7:
            dx = 1
            dy = 1

    return dx, dy


def trace_boundary(image, connectivity=8, background=0):
    # Trazar el límite de un objeto (colección conectada de píxeles con valores desiguales al valor de fondo) en una imagen.

    # Comprobar la conectividad
    if not ((connectivity == 4) or (connectivity == 8)):
        print('Connenctivity must either be 4 or 8')
        sys.exit(1)

    M, N = image.shape
    previous_directions = []  # Lista de direcciones anteriores
    start_search_directions = []  # Lista de direcciones de partida para la búsqueda local
    boundary_positions = []  # Lista de (x,y) píxeles límite

    # Vriable que indica si (mientras buscamos en la vecindad local de un píxel) hemos encontrado un píxel objeto (un píxel con un valor diferente al del fondo).
    found_object = False

    # Buscamos el píxel superior izquierdo del objeto y lo establecemos como punto de partida.
    for x in range(M):
        for y in range(N):
            if not (image[x, y] == background):
                p0 = [x, y]
                found_object = True
                break
        if found_object:
            break

    # Inicializamos las diferentes listas
    boundary_positions.append(p0)
    if connectivity == 4:
        previous_directions.append(0)
        start_search_directions.append(np.mod((previous_directions[0] - 3), 4))
    elif connectivity == 8:
        previous_directions.append(7)
        start_search_directions.append(np.mod((previous_directions[0] - 6), 8))

    n = 0  # Contador de píxeles límite
    while True:
        # Terminamos el algoritmo cuando volvemos al punto de partida.
        if n > 2:
            if ((boundary_positions[n-1] == boundary_positions[0]) and
                    (boundary_positions[n] == boundary_positions[1])):
                break

      