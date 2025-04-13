import cv2

image = cv2.imread('Lesson 50/example.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(gray_image, (224, 224))
cv2.imshow('Processed Image', resized_image)
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('Lesson 50/newImage.jpg', resized_image)
    print("Image saved as Lesson 50/example.jpg")
else:
    print("Image not saved")

cv2.destroyAllWindows()
print(f"Processed Image Dimensions: {resized_image.shape}")
