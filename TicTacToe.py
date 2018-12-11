import cv2 as cv
from AppManager import TicTacToeApp
from imutils.video import VideoStream


webcam = cv.VideoCapture(0)
# webcam = VideoStream(0)
app = TicTacToeApp(webcam, 640, 360, debug=False)
app.set_red_calibration(200, 250)
app.root.mainloop()

