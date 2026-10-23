import cv2

img = cv2.imread('image.jpg', 0)
img = cv2.GaussianBlur(img, (3, 3), 0)  # reduce noise; Laplacian amplifies it
lap = cv2.convertScaleAbs(cv2.Laplacian(img, cv2.CV_64F))

cv2.imshow('Laplacian', lap)
cv2.waitKey(0)
cv2.destroyAllWindows()
