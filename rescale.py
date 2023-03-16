import cv2 as cv


# rescale image or video
def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


# change resolution video

def changeRes(width,height):

    # live video
    # not work with existing video, process for live recording video
    capture.set(3,width)
    capture.set(4,height)
    

# Reading images
# img = cv.imread("Resources/Photos/cat.jpg")

# resized_image = rescaleFrame(img)

# cv.imshow("cat", img)
# cv.imshow("resized cat", resized_image)

# cv.waitKey(0)


# Reading Videos
# capture = cv.VideoCapture("Resources/Videos/dog.mp4")

# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
#     cv.imshow("video", frame)
#     cv.imshow("video rescaled", frame_resized)

#     if cv.waitKey(20) and 0xFF==ord('d'):
#         break   
# cv.waitKey(0)