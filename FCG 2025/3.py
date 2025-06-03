import cv2

# 1. Load & binarize (invert so dots are white on black)
img   = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
_, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# 2. Dilate to fill the dots into squares
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
dilated = cv2.dilate(bw, kernel, iterations=1)

# 3. Save and scan with any QR reader
cv2.imwrite('qr.png', dilated)