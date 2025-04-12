import cv2

# Load the image
image_path = 'your_image.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)

# Check if image loaded successfully
if image is None:
    print("Error: Unable to load image.")
    exit()

# Define three predefined sizes (width, height)
sizes = {
    "small": (150, 150),
    "medium": (300, 300),
    "large": (600, 600)
}

# Resize, display, and save each resized image
for label, size in sizes.items():
    resized_image = cv2.resize(image, size)
    window_name = f"Resized - {label}"
    cv2.imshow(window_name, resized_image)
    cv2.imwrite(f"resized_{label}.jpg", resized_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
