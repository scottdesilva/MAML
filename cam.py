# Cam

import cv2
import numpy as np

def main():

    cap = cv2.VideoCapture(0)

    if cap.isOpened() == False:
        print "error: can't find webcam"
        return

    while cv2.waitKey(1) != 27 and cap.isOpened():
        img = cap.read()

        if not img is None:
            print "error: frame not read"
            break

        imgGrayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.namedWindow("IMAGE", cv2.WINDOW_NORMAL)
        cv2.imshow("IMAGE", img)

    cv2.destroyAllWindows()

    return
