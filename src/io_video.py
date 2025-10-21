from os import path
import cv2 as cv

# Read the video
video_path = path.join('.', 'data', 'monkey.mp4')
video = cv.VideoCapture(video_path)

# Visualize video

ret = True
while ret:
    # Ret is a boolean variable containing the status of the frame.
    ret, frame = video.read()

    if ret:
        cv.imshow(
            winname="A video",
            mat=frame
        )

        cv.waitKey(40)

video.release()
cv.destroyAllWindows()