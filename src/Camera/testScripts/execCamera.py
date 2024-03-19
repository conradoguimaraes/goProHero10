import cv2
from camera import camera

goProCamera = camera()
while(goProCamera.cap.isOpened()):
    goProCamera.display()
    key = cv2.waitKey(1)
    if key == 27: #ESC Key to exit
        break
goProCamera.cap.release()
#cv2.destroyAllWindows()