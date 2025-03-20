  Programa de detección de objetos

La función de este programa es la detección de la cantidad de objetos en una foto a base de filtrado y conteo de contornos


  ¿Cómo funciona?

Cuenta con tres procesos de filtrado que son los siguientes:

Escala gris: Convierte a escala de grises para quitar ruido y facilitar el procesamiento.

Sobel: Detecta el contorno de los objetos. Calcula  las derivadas en la dirección X,Y

Canny: Refina los contornos, optimiza los umbrales y elimina el ruido


  Librerías utilizadas

OpenCV
NumPy
MatPlotlib

Como resultado da el conteo de los objetos en base a los contornos contados y 3 imágenes mostrando la foto con los 3 filtros

