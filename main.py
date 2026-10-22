import cv2
import numpy as np

# Load images and convert to grayscale
base = cv2.imread("base.jpg", cv2.IMREAD_GRAYSCALE)
current = cv2.imread("current.jpg", cv2.IMREAD_GRAYSCALE)

# Ensure images are the same size
current = cv2.resize(current, (base.shape[1], base.shape[0]))

# Calculate absolute difference
diff = cv2.absdiff(base, current)

# Threshold to get binary mask of differences
_, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours and draw bounding boxes
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt) > 500:  # Filter small noise
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(current, (x, y), (x + w, y + h), (0, 255, 0), 2)   