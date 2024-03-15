import numpy as np
import cv2
#import time
from timeFunctions import countdown, currentTime
from utils.getCameras import get_available_cameras
import os
#import cameraFunctions as camf

#Get Camera ID:
cameras = get_available_cameras()
#list(cameras.keys())[0]

#cameraID = int(input("Desired Camera ID>"))
cameraID = 0

error = True
while error:
    try:
        #Force release
        os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = str(cameraID)
        
        #--------------
        #Open Camera and give it some time to open
        #cap = cv2.VideoCapture('http://192.168.137.190:4747/video')
        #cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap = cv2.VideoCapture(0)
        countdown(delay=5, message="Opening Camera")
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        error = False
    except:
        cap.release()
        pass
    #end-try-except
#end-while



#--------------
savePath = os.path.join(os.getcwd(), "images")
if (os.path.isdir(savePath) is not True):
    try:
        os.mkdir(savePath)
    except:
        pass
#end-if-else

newImagePrefix = "img_"
newImageExtension = ".png"
maxLeadingZeros = 4



#camf.setResolution(cap, 2704, 2028)
#width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print("width: ", width)
#print("height: ", height)

showFps = True
prev_frame_time = 0
new_frame_time = 0

sizes = {'0': ( 640,  480),
         '1': (1280,  720),
         '2': (1920, 1080)}
window_width, window_height = sizes["1"]

imgCounter = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    #gray = cv2.resize(gray, (500, 300)) 
    
    if showFps:
        new_frame_time = currentTime()
        # fps will be number of frame processed in given time frame 
        # since their will be most of time error of 0.001 second 
        # we will be subtracting it to get more accurate result 
        
        fps = 1/(new_frame_time-prev_frame_time) 
        prev_frame_time = new_frame_time
    
        # converting the fps into integer 
        fps = int(fps) 
    
        # converting the fps to string so that we can display it on frame by using putText function 
        fps = str(fps) 
        
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA) 
    #end-if-else
    
    frame = cv2.resize(frame, (window_width, window_height))
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(5) == ord('s'): # wait for 's' key to save and exit
        filename = newImagePrefix + (maxLeadingZeros - len(str(imgCounter)))*"0"+str(imgCounter) + newImageExtension
        filePath = os.path.join(savePath, filename)
        
        cv2.imwrite(filePath, frame)
        print("image saved!")
        imgCounter += 1
    #end-if-else
#end-while

cap.release()
cv2.destroyAllWindows()