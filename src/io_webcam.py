import cv2 as cv

# Read the webcam
# Specify the number the webcam to access.
webcam = cv.VideoCapture(0)

# Visualize video

ret = True
while ret:
    # Ret is a boolean variable containing the status of the frame.
    ret, frame = webcam.read()


    cv.imshow(
        winname="A webcam",
        mat=frame
    )

    # Reading frames in webcam is slightly slower than video
    if cv.waitKey(40) & 0xFF == ord("q"):
        break

webcam.release()
cv.destroyAllWindows()