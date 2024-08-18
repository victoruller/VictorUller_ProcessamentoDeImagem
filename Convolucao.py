#Esse código foi feito para ser executado no Google Colab
#Para usar em outras IDEs, basta temover o comando marcado com "X" e substituir os "cv2_imshow()" por:
'''
cv2.imshow('in', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

import numpy as np
import cv2
from google.colab.patches import cv2_imshow #X

img_in = cv2.imread('imagemVivaPinhata.webp')
print(img_in.shape)
img_out = np.zeros(img_in.shape, dtype=np.uint8)

kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
divisor = 0
for aux in range(3):
  for aux2 in range(3):
    divisor += kernel[aux, aux2]


for k in range(img_out.shape[2]):
  for i in range(img_out.shape[1]):
    for j in range(img_out.shape[0]):
      auxx = 0
      for I in np.array([-1, 0, 1]):
        for J in np.array([-1, 0, 1]):
          if(i+I < 0 or i+I >= img_in.shape[1] or j+J < 0 or j+J >= img_in.shape[0]):
            if(j+J >= 0 and j+J < img_in.shape[0]):
              auxx += (img_in[j+J, i, k] * kernel[I+1, J+1])
              continue
            elif(i+I >= 0 and i+I < img_in.shape[1]):
              auxx += (img_in[j, i+I, k] * kernel[I+1, J+1])
              continue
            else:
              auxx += (img_in[j, i, k] * kernel[I+1, J+1])
              continue
          else:
            auxx += (img_in[j+J, i+I, k] * kernel[I+1, J+1])
            continue

      #print(img_out[i, j, k], end=' -> ')
      img_out[j, i, k] =  int((auxx / divisor))
      #print(img_out[i, j, k])

cv2_imshow(img_out)
        
          


