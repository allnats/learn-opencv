import cv2 as cv
from os import path

image_path = path.join (".", "data", "cat.jpg")
image = cv.imread(image_path)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

# Resizing the image
resized_image = cv.resize(image, (width // 8, height // 8))

cv.imshow("Original Image", image)
cv.imshow("Resized Image", resized_image)
cv.waitKey(0)