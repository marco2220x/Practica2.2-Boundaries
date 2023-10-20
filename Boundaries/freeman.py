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

    # Variable que indica si (mientras buscamos en la vecindad local de un píxel) hemos encontrado un píxel objeto (un píxel con un valor diferente al del fondo).
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

        # Esta variable indica si se debe seguir buscando en la vecindad local un píxel objeto
        search_neighbourhood = True
        # Esta variable lleva la cuenta de cuántos hemos buscado.
        loc_counter = 0
        # Obtenemos las coordenadas (x,y) de nuestra actual en la frontera.
        x, y = boundary_positions[n]

        # Buscamos un píxel del objeto en la vecindad de (x,y).
        while search_neighbourhood:

            # Buscar el siguiente píxel en la vecindad de (x,y) para comprobar (buscamos en el sentido de las agujas del reloj también en la vecindad local).
            direction = np.mod(
                start_search_directions[n] - loc_counter, connectivity)
            next_x, next_y = next_index_in_neighbourhood(
                x, y, connectivity, direction)

            # Si vamos más allá del fotograma de la imagen, lo saltamos, y continuamos la búsqueda a partir del siguiente píxel de la vecindad.
            if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                search_neighbourhood = True
                loc_counter += 1
                continue

            # Comprueba si hemos encontrado un objeto píxel
            if not (image[next_x, next_y] == background):
                # Encontrado uno: terminar la búsqueda en este barrio
                search_neighbourhood = False
            else:
                # No ha encontrado ninguno: continúe la búsqueda en este barrio
                loc_counter += 1

        # Añadimos la dirección que utilizamos para encontrar el píxel del objeto a la cadena y también actualizamos la lista de posiciones límite
        previous_directions.append(direction)
        boundary_positions.append([next_x, next_y])

        # A partir de esta dirección, podemos decidir dónde empezar la búsqueda en la siguiente iteración.
        if connectivity == 4:
            start_search_directions.append(np.mod(direction - 3, 4))
        if connectivity == 8:
            if np.mod(direction, 2):
                # la dirección es impar
                start_search_directions.append(np.mod(direction - 6, 8))
            else:
                # dirección es uniforme
                start_search_directions.append(np.mod(direction - 7, 8))

        n += 1

    chain_code = previous_directions[1:-1]

    return chain_code, boundary_positions


def minimum_magnitude(chain_code):
    # minma magnitud
    N = len(chain_code)
    norm_chain_code = np.copy(chain_code)
    circ_chain_code = np.copy(chain_code)
    minimum_int = int(''.join([str(c) for c in chain_code]))
    for _ in range(N):
        first_element = circ_chain_code[0]
        circ_chain_code[:-1] = circ_chain_code[1:]
        circ_chain_code[-1] = first_element
        test_int = int(''.join([str(c) for c in circ_chain_code]))
        if minimum_int > test_int:
            minimum_int = test_int
            norm_chain_code = np.copy(circ_chain_code)
    return list(norm_chain_code)


def first_difference(chain_code, connectivity):
    # Primera diferencia
    fdt_chain_code = []
    N = len(chain_code)
    for i in range(N-1):
        fdt_chain_code.append(
            np.mod(chain_code[i+1] - chain_code[i], connectivity))
    fdt_chain_code.append(np.mod(chain_code[0] - chain_code[-1], connectivity))
    return fdt_chain_code

      