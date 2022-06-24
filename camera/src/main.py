from cv2 import VideoCapture, imwrite, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT

cam = VideoCapture(0)
cam.set(CAP_PROP_FRAME_WIDTH, 1920)
cam.set(CAP_PROP_FRAME_HEIGHT, 1080)

result, image = cam.read()
  
if result:
    imwrite("out/test.png", image)
else:
    print("No image detected. Please! try again")
