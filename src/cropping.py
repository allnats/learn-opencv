import cv2 as cv
from os import path

image_path = path.join(".", "data", "bird.png")
image = cv.imread(image_path)

print(image.shape)
# Note: Image is a numpy array.
print(type(image))
print(type(image.shape))

# Note: The first element is height then width.
cropped_image = image[9:232, 197:481] # We are doing an numpy array slicing.

cv.imshow("Original Image", image)
cv.imshow("Cropped Image", cropped_image)
cv.waitKey(0)