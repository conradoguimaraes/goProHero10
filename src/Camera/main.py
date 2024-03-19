import os
import sys
import logging
import threading
import traceback


from camera import camera
from goProHero10 import goProHero10

from utils import logger
from utils.config import readConfig
from utils.timeFunctions import countdown

import cv2


#----------------------------------------------------------------
config = readConfig(moduleName=__name__)

#----------------------------------------------------------------
#Initialize the Logger
logger = logger.setupLogger()

#----------------------------------------------------------------
#Initialize the API Handler
logging.info("Initializing the goProHero10 [API] ...")
gopro = goProHero10()
logging.info(gopro.showConnectionDetails())

#----------------------------------------------------------------
#Adjust Resolution + Fov
desiredResolutionName = "1080p"
desiredFovName = "wide"

desiredResolution = gopro.resolutions[desiredResolutionName] #1080p,720p,420p
desiredFov = gopro.fovs[desiredFovName] #Wide, Narrow, Superview, Linear

gopro.startWebcam["params"]["res"] = desiredResolution
gopro.startWebcam["params"]["fov"] = desiredFov


# frameSizes = {'480p': ( 640,  480),
#               '720p': (1280,  720),
#               '1080p': (1920, 1080)}
frameSizes = {'480p': ( 640,  480),
              '720p': (1280,  720),
              '1080p': (1280, 720)} #reduce 1080p window size

#----------------------------------------------------------------
#Check if camera is in "Idle" Mode
#When the camera is in this mode, start the webcam with the
#desired RESOLUTION and FOV
currentStatus = ""
while (currentStatus != "idle"):
    currentStatus = gopro.getCameraState()
    logging.info(f"Current Camera Status: {currentStatus}.")
    if (currentStatus == "idle"):
        logging.info(f'Starting webcam with:\nurl: {gopro.startWebcam["url"]}\nparams: {gopro.startWebcam["params"]}')
        logging.info(f'Resolution: {desiredResolution}\nFOV:{desiredFov}\n')
        gopro.getHTTP(paramURL  = gopro.startWebcam["url"],
                      parameters= gopro.startWebcam["params"])
    else:
        logging.info("Camera is not available for webcam mode ...")
        
        logging.info('Forcing Webcam exit ({gopro.exitWebcamPreview["url"]}) ...')
        gopro.getHTTP(paramURL = gopro.exitWebcamPreview["url"])
        countdown(delay=3, message="Closing Webcam preview ...")
        
        logging.info("Sending Keep Alive signal ...")
        gopro.keepAliveSignal()
    #end-if-else
#end-while

newCurrentStatus = gopro.getCameraState()
logging.info(f"Current Camera Status: {currentStatus}.")
print(f"Current Camera Status: {currentStatus}.")

#----------------------------------------------------------------


def keyPressHandler():
    #not used
    while True:
        try:
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                del goProCamera
            elif (cv2.waitKey(1) & 0xFF == ord('1')):
                gopro.startWebcam["params"]["res"] = gopro.resolutions["1080p"]
            elif (cv2.waitKey(1) & 0xFF == ord('1')):
                gopro.startWebcam["params"]["res"] = gopro.resolutions["720p"]
            elif (cv2.waitKey(1) & 0xFF == ord('3')):
                gopro.startWebcam["params"]["res"] = gopro.resolutions["480p"]
            else:
                pass
            #end-if-else
        except:
            pass
        #end-try-except
#end-def

#threadKeyPress = threading.Thread(target = keyPressHandler, args=[])
#threadKeyPress.start()


#----------------------------------------------------------------
#Path to save the output images (when the user presses key 'p')
savePath = os.path.join(os.getcwd(), "images")
if (os.path.isdir(savePath) is not True):
    try:
        os.mkdir(savePath)
    except:
        pass
#end-if-else

newImagePrefix = "img_"
newImageExtension = ".png"
maxLeadingZeros = 4 #example: img_0000.png, img_0001.png, ...
imgCounter = 0

#----------------------------------------------------------------


#Initialize the Camera/Preview/Player Handler
logging.info("Initializing the Camera [openCV] ...")
goProCamera = camera()

#Set the Frame (width, height) according to the resolution
goProCamera.frameWidth, goProCamera.frameHeight = frameSizes[desiredResolutionName]
#Set the Window Name:
goProCamera.windowName = desiredResolutionName + " | " + desiredFovName 



changeParamsFlag = False


if (goProCamera.cap.isOpened() is False):
    logging.error("Unable to open the camera ...")
    raise Exception("Unable to open the camera ...")
else:
    logging.info("Camera was opened successfully.")
    
    while(goProCamera.cap.isOpened()):
        #Update the image on the frame:
        goProCamera.display()
        
        
        #Check the Key presses:
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
        elif (cv2.waitKey(1) & 0xFF == ord('a')):
            desiredResolutionName = "1080p"
            changeParamsFlag = True
        elif (cv2.waitKey(1) & 0xFF == ord('s')):
            desiredResolutionName = "720p"
            changeParamsFlag = True
        elif (cv2.waitKey(1) & 0xFF == ord('d')):
            desiredResolutionName = "480p"
            changeParamsFlag = True
        elif (cv2.waitKey(1) & 0xFF == ord('z')):
            desiredFovName = "wide"
            changeParamsFlag = True
        elif (cv2.waitKey(1) & 0xFF == ord('x')):
            desiredFovName = "narrow"
            changeParamsFlag = True
        elif (cv2.waitKey(1) & 0xFF == ord('c')):
            desiredFovName = "superview"
            changeParamsFlag = True
        elif (cv2.waitKey(1) & 0xFF == ord('v')):
            desiredFovName = "linear"
            changeParamsFlag = True
            
        elif cv2.waitKey(5) == ord('p'):
            filename = newImagePrefix + (maxLeadingZeros - len(str(imgCounter)))*"0"+str(imgCounter) + newImageExtension
            filePath = os.path.join(savePath, filename)
            cv2.imwrite(filePath, goProCamera.frame)
            logging.info(f"Image {filename} saved!")
            imgCounter += 1
        else:
            pass
        #end-if-else
        
        #Update/Change the Resolution/FOV upon user's request
        if (changeParamsFlag):
            msg = f"Received user request to change the resolution to {desiredResolutionName}."
            logging.info(msg)
            print(msg)
            
            desiredResolution = gopro.resolutions[desiredResolutionName]
            desiredFov = gopro.fovs[desiredFovName]
            
            gopro.startWebcam["params"]["res"] = desiredResolution
            gopro.startWebcam["params"]["fov"] = desiredFov
            
            logging.info(f'Starting webcam with:\nurl: {gopro.startWebcam["url"]}\nparams: {gopro.startWebcam["params"]}')
            logging.info(f'Resolution: {desiredResolution}\nFOV:{desiredFov}\n')
            #gopro.getHTTP(paramURL = gopro.exitWebcamPreview["url"])
            gopro.getHTTP(paramURL = gopro.stopWebcam["url"])
            #countdown(delay=1, message="Closing Webcam preview and restarting...")
            gopro.getHTTP(paramURL  = gopro.startWebcam["url"],
                          parameters= gopro.startWebcam["params"])
            
            #Adjust the frame size according to the resolution
            goProCamera.frameWidth, goProCamera.frameHeight = frameSizes[desiredResolutionName]
            
            
            #Adjust the Window Name:
            previousWindowName = goProCamera.windowName
            goProCamera.windowName = desiredResolutionName + " | " + desiredFovName 
            
            cv2.destroyWindow(previousWindowName)
            
            changeParamsFlag = False
        #end-if-else
        
    #end-while
#end-if-else


goProCamera.cap.release()

#----------------------------------------------------------------


#threadKeyPress.stop()

logging.info("End of program.")