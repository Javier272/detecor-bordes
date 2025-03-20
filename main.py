import cv2
import numpy as np
from matplotlib import pyplot as plt


#carga la imagen
imagen=cv2.imread("ob9.jpg")


#convierte la imagen a escala de grises
imagen_gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)