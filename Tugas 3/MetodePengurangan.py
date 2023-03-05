import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca citra acuan dan citra uji
img1 = cv2.imread('doraemon.jpg',0)
img2 = cv2.imread('doraemon1.jpg',0)

# melakukan pengurangan citra
diff = cv2.absdiff(img1,img2)

# menampilkan citra acuan, citra uji, dan hasil pengurangan citra
plt.subplot(131),plt.imshow(img1,cmap = 'gray')
plt.title('Citra Lena'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img2,cmap = 'gray')
plt.title('Citra gambar'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(diff,cmap = 'gray')
plt.title('Hasil Pengurangan Citra'), plt.xticks([]), plt.yticks([])
plt.show()
