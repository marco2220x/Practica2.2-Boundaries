import numpy as np
import matplotlib.pyplot as plt
import cv2
from Boundaries import freeman as cc
from Boundaries import moore as mr

if __name__ == "__main__":

    #Leer la imagen
    image_path = 'utilidades/ishihara-18.png' #Ingrese la la direccion de la imagen
    original_image = cv2.imread(image_path, 1)
    image = cv2.imread(image_path, 0)

    '''
    #Suavizado para la imagen de formas (la iamgen de circulos no lo necesita)
    image = cv2.blur(image, (9, 9))
    '''

    ''' Rotar imagen '''
    #Sola descomenta esto para rotar la imagen
    '''
    original_image = cv2.rotate(original_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    '''
    
    connectivity = 8 #Escoge la conectividad 4 o 8
    background = 50

    if len(np.unique(image)) == 2:
        bg, fg = np.unique(image)
        image[image == bg] = background
        image[image == fg] = 255

    chain_code, boundary_pixels = cc.trace_boundary(image, connectivity, background)

    image_with_boundary = np.copy(image)
    for x, y in boundary_pixels:
        image_with_boundary[x, y] = 150
        
    print('Cadena de Freeman de la imagen original (escala de grises)')
    print('Codigo de cadena:')
    print(chain_code)
    
    
    # Binarizado de la imagen del circulo
    _, binary_image = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)
    
    '''
    # Binarizado de la imagen de formas
    _, binary_image = cv2.threshold(image, 89, 255, cv2.THRESH_BINARY)
    '''

    #Algoritmo de Moore
    image_moore= mr.moore_boundary(binary_image)

    if len(np.unique(image_moore)) == 2:
        bg, fg = np.unique(image_moore)
        image_moore[image_moore == bg] = background
        image_moore[image_moore == fg] = 255

    chain_code1, boundary_pixels1 = cc.trace_boundary(image_moore, connectivity, background)

    image_with_boundary1 = np.copy(image_moore)
    for x, y in boundary_pixels1:
        image_with_boundary1[x, y] = 150

    #Códigos de Freeman
    
    print('Cadenas de Freeman con la imagen original segmentada ocupando la máscara de Moore')
    print('Codigo de cadena:')
    print(chain_code1)
    print('Normalizacion del punto de inicio con la magnitud minima:')
    mcs_chain_code = cc.minimum_magnitude(chain_code1)
    print(mcs_chain_code)
    print('Normalizacion de la primera diferencia:')
    fdt_chain_code = cc.first_difference(chain_code1, connectivity)
    print(fdt_chain_code)
    print('Normalizacion al punto de inicio con magnitud minima de la primera diferencia:')
    rs_chain_code = cc.minimum_magnitude(fdt_chain_code)
    print(rs_chain_code)
    

    #Para la imagen rotada descomenta esta seccion y comenta la seccion anterior
    '''
    #Códigos de Freeman para la imagen rotada
    print('Algoritmo de Freeman con la imagen original segmentada ocupando la máscara de Moore')
    print('Codigo de cadena:')
    print(chain_code1)
    print('Normalizacion del punto de inicio con la magnitud minima:')
    mcs_chain_code = cc.minimum_magnitude(chain_code1)
    print(mcs_chain_code)
    print('Normalizacion de la primera diferencia del punto de inicio con la magnitud minima:')
    fdt_chain_code = cc.first_difference(mcs_chain_code, connectivity)
    print(fdt_chain_code)
    print('Normalizacion al punto de inicio con magnitud minima de la primera diferencia del punto de inicio con la magnitud minima:')
    rs_chain_code = cc.minimum_magnitude(fdt_chain_code)
    print(rs_chain_code)
    '''

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 3, 1)
    ax1.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    ax1.set_title('Imagen Original')
    ax1 = fig.add_subplot(2, 3, 2)
    ax1.imshow(binary_image, cmap='gray')
    ax1.set_title('Imagen Binarizada')
    ax1 = fig.add_subplot(2, 3, 3)
    ax1.imshow(image_moore, cmap='gray')
    ax1.set_title('Imagen algoritmo de Moore')
    ax1 = fig.add_subplot(2, 3, 4)
    ax1.imshow(image_with_boundary, cmap='gray', interpolation='none', vmin=0, vmax=255)
    ax1.set_title('Imagen con algoritmo de Freeman')
    ax1 = fig.add_subplot(2, 3, (5, 6))
    ax1.imshow(image_with_boundary1, cmap='gray', interpolation='none', vmin=0, vmax=255)
    ax1.set_title('Cadena de Freeman con imagen segmentada ocupando la máscara de Moore')
    plt.show()


    


