from os import path
import cv2 as cv

# Read the image.
image_path = path.join('.', 'data', 'bird.png')
image = cv.imread(image_path)

# Write the image.
image_path_out = path.join('.', 'data', 'bird_out.png')
cv.imwrite(image_path_out, image)

# Visualize Image

cv.imshow(
    winname="Cool Bird",
    mat=image
)
cv.waitKey(0)