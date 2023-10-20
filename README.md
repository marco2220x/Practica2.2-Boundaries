# Seguimiento de límites en Python 📸

En este trabajo, se han desarrollado dos algoritmos que implementan técnicas y  enfoques distintos para el seguimiento de límites de un objeto de interés en una imagen.

## Técnicas de Segmentación Implementadas
Técnicas de seguimiento de límites (Boundaries):

1. **Algoritmo de seguimiento de límites (Moore Boundary Tracing):** El algoritmo de Moore es una técnica que se basa en el principio de seguimiento de límites en imágenes binarias. El objetivo del algoritmo de Moore es identificar y seguir la secuencia de píxeles que forman el límite de un objeto en una imagen. 

2. **Segmentación por cluster por el método de k-medias:** Los códigos de cadenas de Freeman, son una técnica para representar la forma o el contorno de objetos en imágenes digitales.
Estos códigos se utilizan para describir la dirección de un borde o contorno en una imagen binaria.

## Visualización de Resultados
Para que puedas evaluar fácilmente los resultados de cada técnica, hemos utilizado la biblioteca Matplotlib para mostrarlos en una sola imagen. Cada resultado se presenta en un subplot separado, lo que facilita la comparación y evaluación de las diferentes técnicas utilizadas.


#### Resultados obtenidos a partir de implementar el seguimiento de contornos por el algoritmo de Moore

<table>
  <tr>
    <td align="center">
      <img src="/imagenesREADME/Imagen1.png" alt="Resultado 1" width="400"/>
    </td>
  </tr>
</table>


#### Resultados obtenidos de los códigos de cadenas de Freeman:
<table>
  <tr>
    <td align="center">
      <img src="/imagenesREADME/Imagen2.jpg" alt="Resultado 1" width="400"/>
    </td>
  </tr>
</table>

#### Resultados obtenidos al aplicar la mormalización a la rotacción (First difference):
<table>
  <tr>
    <td align="center">
      <img src="/imagenesREADME/Imagen2.jpg" alt="Resultado 1" width="400"/>
    </td>
  </tr>
</table>

#### Resultados obtenidos de la normalización del punto inicial con la magnitud miníma:
<table>
  <tr>
    <td align="center">
      <img src="/imagenesREADME/Imagen2.jpg" alt="Resultado 1" width="400"/>
    </td>
  </tr>
</table>

## Cómo Usar el Programa
Aquí te proporcionamos instrucciones sobre cómo utilizar nuestro programa:
1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python y las bibliotecas necesarias instaladas.
3. Ejecuta el programa y proporciona una imagen en escala de grises como entrada.
4. El programa aplicará las técnicas de segmentación y mostrará los resultados utilizando Matplotlib.

## Autores
Este proyecto fue realizado por un equipo de estudiantes:
| [<img src="https://avatars.githubusercontent.com/u/113084234?v=4" width=115><br><sub>Aranza Michelle Gutierrez Jimenez</sub>](https://github.com/AranzaMich) |  [<img src="https://avatars.githubusercontent.com/u/113297618?v=4" width=115><br><sub>Evelyn Solano Portillo</sub>](https://github.com/Eveeelyyyn) |  [<img src="https://avatars.githubusercontent.com/u/112792541?v=4" width=115><br><sub>Marco Castelan Rosete</sub>](https://github.com/marco2220x) | [<img src="https://avatars.githubusercontent.com/u/113079687?v=4" width=115><br><sub>Daniel Vega Rodríguez</sub>](https://github.com/DanVer2002) |
| :---: | :---: | :---: | :---: |

