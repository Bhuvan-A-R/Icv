import cv2, numpy as np

img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# CMYK has no built-in OpenCV code, so compute it from RGB
b, g, r = cv2.split(img / 255.0)
k = 1 - np.maximum(np.maximum(r, g), b)
c, m, y = [(1 - x - k) / (1 - k + 1e-8) for x in (r, g, b)]

for name, im in [('Gray', gray), ('HSV', hsv), ('C', c), ('M', m), ('Y', y), ('K', k)]:
    cv2.imshow(name, im)
cv2.waitKey(0)
cv2.destroyAllWindows()
