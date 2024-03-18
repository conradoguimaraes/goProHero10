import os
import numpy as np
import cv2

from utils.config import readConfig

import time
from utils.timeFunctions import countdown, currentTime
from utils.getCameras import get_available_cameras

#pip install pygrabber==0.1
from pygrabber.dshow_graph import FilterGraph

class camera:
    def __init__(self, cameraConfig: str="camera", cameraName: str="GoPro Webcam", windowName: str="Frame") -> None:
        #------------------------------------------------------
        #Read the Configs
        self.config = readConfig(moduleName = cameraConfig)
        
        self.enableDirectShow = self.config["enableDirectShow"]
        self.showFPS          = self.config["showFPS"]
        self.imageSubfolder   = self.config["imageSubfolder"]
        self.frameWidth       = self.config["frameWidth"]
        self.frameHeight      = self.config["frameHeight"]
        #------------------------------------------------------
        #Create the Images Subfolder:
        self.savePath = os.path.join(os.getcwd(), "images")
        if (os.path.isdir(self.savePath) is not True):
            try:
                os.mkdir(self.savePath)
            except:
                pass
        #end-if-else
        #------------------------------------------------------
        #Get the Camera ID
        self.cameraID = self.getCameraID(goProName = cameraName)
        if self.cameraID == -1: raise Exception("'GoPro Webcam' was not found in the available cameras list.")
        
        #------------------------------------------------------
        #Start the Camera with/without Direct Shows
        #self.cap = cv2.VideoCapture(self.cameraID, cv2.CAP_DSHOW)
        if (self.enableDirectShow):
            self.cap = cv2.VideoCapture(self.cameraID, cv2.CAP_DSHOW)
        else:
            self.cap = cv2.VideoCapture(self.cameraID)

        #end-if-else
        #Add some delay to give time for the camera setup
        countdown(delay = 3, message="Opening Camera")
        #------------------------------------------------------
        if (self.showFPS):
            self.prev_frame_time = 0
            self.new_frame_time = 0
            self.fps = 0
        #end-if-else
        #------------------------------------------------------
        self.windowName = windowName
        
        
    #end-def
    
    
    def display(self):
        ret, frame = self.cap.read()
        
        if self.showFPS:
            self.new_frame_time = currentTime()
            # fps will be number of frame processed in given time frame 
            # since their will be most of time error of 0.001 second 
            # we will be subtracting it to get more accurate result 
            
            fps = 1/(self.new_frame_time - self.prev_frame_time) 
            self.prev_frame_time = self.new_frame_time

            self.fps = int(fps)
            # converting the fps to string so that we can display it on frame by using putText function 
            fps = str(self.fps)
            
            font = cv2.FONT_HERSHEY_SIMPLEX 
            cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA) 
        #end-if-else
        
        
        cv2.imshow(self.windowName, frame)
        key = cv2.waitKey(1)
        if key == 27: #ESC Key to exit
            pass
        
    #end-def
    
    
    def changeFrameSize(self) -> None:
        cv2.resizeWindow(self.windowName, 
                         self.frameWidth,
                         self.frameHeight) 
        return
    #end-def
    
    def getCameraID(self, goProName: str="") -> int:
        cameras = self.get_available_cameras()
        for cameraID, cameraName in cameras.items():
            if (cameraName.lower() == goProName.lower()):
                return cameraID
            else:
                pass
            #end-if-else
        #end-for
        return -1
    #end-def
    
    def get_available_cameras(self) -> dict:
        #https://stackoverflow.com/questions/70886225/get-camera-device-name-and-port-for-opencv-videostream-python
        devices = FilterGraph().get_input_devices()

        available_cameras = {}

        for device_index, device_name in enumerate(devices):
            available_cameras[device_index] = device_name
        #end-for
        
        print(available_cameras)
        return available_cameras
    #end-def
    
#end-class

if __name__ == "__main__":
    pass
#end-if-else