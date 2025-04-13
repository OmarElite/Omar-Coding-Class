import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load image
image_path = 'Lesson 51/example2.jpg'
image = cv2.imread(image_path)

# Convert from BGR to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 1. Rotate the image (e.g., 90 degrees clockwise)
rotated = cv2.rotate(image_rgb, cv2.ROTATE_90_CLOCKWISE)

# 2. Brighten the image
brightened = cv2.convertScaleAbs(rotated, alpha=1.2, beta=30)  # increase contrast and brightness

# 3. Crop the image (center crop)
h, w, _ = brightened.shape
crop_size = 300
start_y = h//2 - crop_size//2
start_x = w//2 - crop_size//2
cropped = brightened[start_y:start_y+crop_size, start_x:start_x+crop_size]

# Display all steps
titles = ['Original', 'Rotated', 'Brightened', 'Cropped']
images = [image_rgb, rotated, brightened, cropped]

plt.figure(figsize=(12, 6))
for i in range(4):
    plt.subplot(1, 4, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
