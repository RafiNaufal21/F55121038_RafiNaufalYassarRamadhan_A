import cv2
import numpy as np

def resize(image,w,h):
    image=cv2.resize(image,(w,h))
    return image
def gausblur(image,blur,m):
    image = cv2.GaussianBlur(image,(m,m),blur)
    return image
def medblur(image,shift):
    image=cv2.medianBlur(image,shift)
    return image
def avgblur(image,shift):
    image=cv2.blur(image,(shift,shift))
    return image

gambar = cv2.imread('lena.jpg')
x = medblur(gambar,7)
cv2.imshow("lenaRGB",gambar)
cv2.imshow("hasil",x)

cv2.waitKey(0)
cv2.destroyAllWindows()