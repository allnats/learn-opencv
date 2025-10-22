import cv2 as cv
from os import path

image_path = path.join(".", "data", "bird.png")
image = cv.imread(image_path)

image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

cv.imshow("Original Image", image)
cv.imshow("RGB Image", image_rgb)
cv.imshow("Gray Image", image_gray)
cv.imshow("HSV Image", image_hsv)
cv.waitKey(0)