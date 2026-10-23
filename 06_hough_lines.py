import cv2, numpy as np

img = cv2.imread('image.jpg')
edges = cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 50, 150)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

if lines is not None:
    for rho, theta in lines[:, 0]:
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a * rho, b * rho
        cv2.line(img, (int(x0 - 1000 * b), int(y0 + 1000 * a)),
                 (int(x0 + 1000 * b), int(y0 - 1000 * a)), (0, 0, 255), 2)

cv2.imshow('Hough Lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
