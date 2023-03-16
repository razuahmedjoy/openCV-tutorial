import cv2 as cv

# Reading images
# img = cv.imread("Resources/Photos/cat_large.jpg")

# cv.imshow("Cat",img)

# cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture("Resources/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("video", frame)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break
    

capture.release()

cv.destroyAllWindows()
