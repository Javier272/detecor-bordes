import cv2
import numpy as np
from matplotlib import pyplot as plt


#carga la imagen
imagen=cv2.imread("ob9.jpg")


#convierte la imagen a escala de grises
imagen_gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)


#Aplica filtro sobel en X, Y
xsoble=cv2.Sobel(imagen_gris,cv2.CV_64F,1,0,ksize=5)
ysobel=cv2.Sobel(imagen_gris,cv2.CV_64F,0,1,ksize=5)


#Calcula gradiente
gradiente=cv2.magnitude(xsoble,ysobel)


#Normaliza el gradiente
normalizado_gradiente=np.uint8(255*(gradiente/np.max(gradiente)))