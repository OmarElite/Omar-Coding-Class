import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Set paths
input_path = "original_images/example.jpg"  # Change to your actual image name
output_dir = "output_images"

# Load the image
image = cv2.imread(input_path)

# 1. Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(os.path.join(output_dir, "grayscale.jpg"), gray_image)

# Display Grayscale Image
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

# 2. Crop the image (adjust values if needed)
cropped_image = image[100:300, 200:400]
cv2.imwrite(os.path.join(output_dir, "cropped.jpg"), cropped_image)

# 3. Rotate the image by 45 degrees
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))
cv2.imwrite(os.path.join(output_dir, "rotated.jpg"), rotated_image)

# 4. Adjust Brightness (+50 to all pixel values)
bright_image = cv2.add(image, (50, 50, 50, 0))  # Handles overflow internally
cv2.imwrite(os.path.join(output_dir, "brightened.jpg"), bright_image)

print("All image transformations are completed and saved.")
