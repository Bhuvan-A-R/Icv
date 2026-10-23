import cv2, numpy as np

img = cv2.imread('image.jpg', 0)
F = np.fft.fftshift(np.fft.fft2(img))
r, c = img.shape
y, x = np.ogrid[:r, :c]

# Circular mask of radius 30 keeps low frequencies; its inverse keeps high
low = ((y - r // 2) ** 2 + (x - c // 2) ** 2 <= 30 ** 2)
back = lambda m: np.abs(np.fft.ifft2(np.fft.ifftshift(F * m))).astype(np.uint8)

cv2.imshow('Low-pass', back(low))
cv2.imshow('High-pass', back(~low))
cv2.waitKey(0)
cv2.destroyAllWindows()
