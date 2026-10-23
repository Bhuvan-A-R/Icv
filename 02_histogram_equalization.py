import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)
eq = cv2.equalizeHist(img)

plt.hist(img.ravel(), 256, (0, 256)); plt.title('Original'); plt.figure()
plt.hist(eq.ravel(), 256, (0, 256)); plt.title('Equalized'); plt.show()
