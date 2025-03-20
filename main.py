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

#Detectar los bordes con canny
bordes=cv2.Canny(normalizado_gradiente,50,200)


#Detecta contornos de la imagen
contornos,jerarquia=cv2.findContours(bordes,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


#Dibujar contornos
imagen_contornos=np.zeros_like(imagen)
cv2.drawContours(imagen_contornos,contornos,-1,(0,255,0),2)


#Contador de contornos
numero_objetos=len(contornos)
print("Numero de objetos encontrados:",numero_objetos)


#Imprime las imagenes la imagen con contornos
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(imagen_gris, cmap="gray")
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(normalizado_gradiente, cmap="gray")
plt.title("Filtro Sobel")
plt.axis("off")



plt.subplot(1, 3, 3)
plt.imshow(imagen_contornos, cmap="gray")
plt.title("Contornos Detectados")
plt.axis("off")

plt.show()

