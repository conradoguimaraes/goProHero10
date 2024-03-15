import cv2 as cv
def setResolution(cap, x,y):
    cap.set(cv.CAP_PROP_FRAME_WIDTH, int(x))
    cap.set(cv.CAP_PROP_FRAME_WIDTH, int(y))
    return str(cap.get(cv.CAP_PROP_FRAME_WIDTH)),str(cap.get(cv.CAP_PROP_FRAME_WIDTH))
#end-def