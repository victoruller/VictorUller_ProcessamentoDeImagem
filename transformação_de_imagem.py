
'''
cv2.imshow('in', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
#abrir a imagem

def mostraImagemNoColab(imagemLink, querVerOShape=0):
  from google.colab.patches import cv2_imshow #X
  img = cv2.imread(imagemLink, 3)
  if(querVerOShape):
    print(img.shape)
  cv2_imshow(img)
 


def mostrarImagem(imagemLink, querVerOShape=0):
  img = cv2.imread(imagemLink,3)
  if(querVerOShape):
    print(img.shape)
  cv2.imshow('in', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


  
def transformaEmEscalaDeCinzas(img):
  B, G, R = cv2.split(img)
  img_grayscale_cv2 = R * 0.299 + G * 0.587 + B * 0.114
  return img_grayscale_cv2
  

def mostraHistogramaDeImagemGrayscale(img):
  histogram = np.zeros(256)
  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      histogram[int(img[i,j])] += 1
      x = np.linspace(0, 255, 256)

  plt.bar(x, histogram)
  plt.xlabel('intensidade');
  plt.ylabel('frequência');
  plt.show()


def transformaEmNegativaComNumpy(img):
  img_negative_np = 255-img
  return img_negative_np
  
def transformaColoridaEmNegativaPontoAPonto(img):
  img_out = [img.shape[0], img.shape[1], img.shape[2]]
  img_out = np.zeros(img_out, np.uint8)
  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      for k in range(img.shape[2]):
          img_out[i, j, k] = 255 - img[i, j, k]
  return img_out


def transformaEmLogaritmica(img):
  img_in = img
  
  c = 35
  img_out = img_in.copy()
  
  img_out = c*np.log(1+img_in)
  return img_out



#POTÊNCIA (GAMMA)
def transformaGamma(img, gamma=1, c=1):
#para desvendar imagens escuras, gamma <1 (0.4 até 0.7 normalmente), para claras, gamma>1 (1.5 até 3 normalmente)
    
  img_in = img
  img_out = c * np.power(img_in,  gamma) 
  return img_out
