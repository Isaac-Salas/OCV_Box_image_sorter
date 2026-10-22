import cv2
import matplotlib.pyplot as plt



# Load images as grayscale
base = cv2.imread("base.jpeg", 0)
current = cv2.imread("images/image (4).jpeg", 0)

# Ensure images are the same size
current = cv2.resize(current, (base.shape[1], base.shape[0]))

# Calculate absolute difference
diff = cv2.absdiff(base, current)

# Threshold to remove noise (e.g., compression artifacts)
# Pixels with difference > 25 become white (255), others black (0)
_, mask = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)




# Calculate percentage of changed pixels
total_pixels = base.size  # width * height
changed_pixels = cv2.countNonZero(mask)
percentage_change = (changed_pixels / total_pixels) * 100

if percentage_change > 30:
    print('Not a single box!')
elif percentage_change < 15:
    print ('Single box!')
else:
    print('Oddity!')
    

plt.imshow(base + diff)
print(f"Percentage of image changed: {percentage_change:.2f}%")