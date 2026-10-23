import cv2, numpy as np

img = cv2.imread('image.jpg', 0)
_, b = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
k = np.ones((5, 5), np.uint8)

cv2.imshow('Dilation', cv2.dilate(b, k))
cv2.imshow('Erosion', cv2.erode(b, k))
cv2.imshow('Opening', cv2.morphologyEx(b, cv2.MORPH_OPEN, k))
cv2.imshow('Closing', cv2.morphologyEx(b, cv2.MORPH_CLOSE, k))
cv2.waitKey(0)
cv2.destroyAllWindows()
