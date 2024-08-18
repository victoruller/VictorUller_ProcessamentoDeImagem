#Esse código foi feito para ser executado no Google Colab
#Para usar em outras IDEs, basta temover o comando marcado com "X" e substituir os "cv2_imshow()" por:
'''
cv2.imshow('in', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow #X
#abria a imagem
img = cv2.imread('imagemVivaPinhata.webp',3)
print(img.shape)
cv2_imshow(img)
#ESCALA DE CINZAS
B, G, R = cv2.split(img)
img_grayscale_cv2 = R * 0.299 + G * 0.587 + B * 0.114
cv2_imshow(img_grayscale_cv2)
#HISTOGRAMA
histogram = np.zeros(256)
for i in range(img_grayscale_cv2.shape[0]):
  for j in range(img_grayscale_cv2.shape[1]):
    histogram[int(img_grayscale_cv2[i,j])] += 1
    x = np.linspace(0, 255, 256)

plt.bar(x, histogram)
plt.xlabel('intensidade');
plt.ylabel('frequência');
plt.show()


#NEGATIVA
cv2_imshow(img)
img_negative_np = 255-img

#cv2_imshow(img_negative_np)


img_in = img
img_out = [img_in.shape[0], img_in.shape[1], img_in.shape[2]]
img_out = np.zeros(img_out, np.uint8)
for i in range(img_in.shape[0]):
  for j in range(img_in.shape[1]):
    for k in range(img_in.shape[2]):
        img_out[i, j, k] = 255 - img_in[i, j, k]

cv2_imshow(img_out)


#LOGARITMICA
img_in = img

c = 35
img_out = img_in.copy()


img_out = c*np.log(1+img_in)
cv2_imshow(img_out)

print(img_out.max())
#logaritmica em grayscale
img_in = img_grayscale_cv2

c = 35
img_out = img_in.copy()


img_out = c*np.log(1+img_in) #necessario fazer um cast para exibir
cv2_imshow(img_out)
