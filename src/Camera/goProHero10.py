import os
import requests
import logging
import traceback

from utils.config import readConfig
from utils import logger

import utils.goProHTTPControlVars as goProHTTPControlVars
import utils.goProHTTPMediaVars as goProHTTPMediaVars
import utils.goProHTTPCapabilitiesVars as goProHTTPCapabilitiesVars
import utils.goProHTTPWebcamVars as goProHTTPWebcamVars

from utils.timeFunctions import countdown

class goProHero10:
    """
    https://gopro.github.io/OpenGoPro/http
    
    
    https://community.gopro.com/s/article/GoPro-Webcam?language=en_US
    Webcam Mode resolution limitations: "Here you can choose between [1080p] (default) or [720p]."

    Webcam Resolution
    ID 	Resolution 	Supported Cameras
    4 	480p 	Hero 10 Black, Hero 9 Black
    7 	720p 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black
    12 	1080p 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black

    Webcam Field-of-View
    ID 	FOV 	Supported Cameras
    0 	Wide 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black
    2 	Narrow 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black
    3 	Superview 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black
    4 	Linear 	Hero 12 Black, Hero 9 Black, Hero 10 Black, Hero 11 Black
    """
    
    #Control Vars:
    turboTransfer = goProHTTPControlVars.turboTransfer
    wiredCamera   = goProHTTPControlVars.wiredCamera
    keepAlive     = goProHTTPControlVars.keepAlive
    cameraControl = goProHTTPControlVars.cameraControl
    dateTime      = goProHTTPControlVars.dateTime
    digitalZoom   = goProHTTPControlVars.digitalZoom
    shutter       = goProHTTPControlVars.shutter
    
    
    #Highlight Vars:
    #Hilight a Media File - Add a hilight / tag to an existing photo or media file
    hilightMediaFile = "not implemented"
    #Hilight while recording - Add hilight at current time while recording video (This can only be used during recording.)
    hilightRecording = "not implemented"
    #Remove hilight - Remove an existing hilight from a photo or video file.
    hilightRemove = "not implemented"
    
    
    #Media Vars:
    downloadMediaFile     = goProHTTPMediaVars.downloadMediaFile
    downloadLastMediaFile = goProHTTPMediaVars.downloadLastMediaFile
    
    #Query Vars:
    #...
    
    #Capability Vars:
    #...
    
    #Webcam Vars:
    enterWebcamPreview = goProHTTPWebcamVars.enterWebcamPreview
    exitWebcamPreview  = goProHTTPWebcamVars.exitWebcamPreview
    getWebcamStatus    = goProHTTPWebcamVars.getWebcamStatus
    getWebcamVersion   = goProHTTPWebcamVars.getWebcamVersion
    startWebcam        = goProHTTPWebcamVars.startWebcam
    stopWebcam         = goProHTTPWebcamVars.stopWebcam
    
    
    
    cameraStates = {
        0 : "Off",
        1 : "Idle",
        2 : "High Power Preview",
        3 : "Low Power Preview"
    }
    
    resolutions = {
         "480p" :  4,
         "720p" :  7,
        "1080p" : 12
    }
    
    fovs = {
              "wide" : 0,
            "narrow" : 2,
         "superview" : 3,
            "linear" : 4
    }
    
    
    
    def __init__(self, goProHero10Config: str="goProHero10", cameraPort = "8080") -> None:
        #------------------------------------------------------
        #Read the Configs
        self.config = readConfig(moduleName = goProHero10Config)
        
        #------------------------------------------------------
        #Get the Serial Number and build the IP Address of the GoPro Camera
        serialX, serialY, serialZ = self.config["serialNrX"], self.config["serialNrY"], self.config["serialNrZ"]
        self.cameraPort = cameraPort
        self.cameraAddress = f"172.2{serialX}.1{serialY}{serialZ}.51"  + ":" + self.cameraPort
        self.cameraFullAddress = "http://" + self.cameraAddress
        
        #------------------------------------------------------
        #Get the Current Camera State
        self.cameraState = self.getCameraState()
        
    #end-def
    
    def showConnectionDetails(self) -> str:
        msg = f"""\rIP Address: {self.cameraAddress}\n\
                  \rPort: {self.cameraPort}\n\
                  \rCamera Full Address: {self.cameraFullAddress}
                """
        print(msg)
        return msg
    #end-def
    

    def keepAliveSignal(self) -> None:
        self.getHTTP(paramURL = self.keepAlive["url"])
        return
    #end-def
    
    def getCameraState(self) -> None:
        statusJSONdata = self.getHTTP(paramURL = self.getWebcamStatus["url"]) #json format
        statusCode = statusJSONdata.get("status") #integer
        status = self.cameraStates.get(statusCode, "") #string
        return status.lower()
    
    
    def getHTTP(self, paramURL: str="", parameters: dict={}) -> int:
        fullURL = self.cameraFullAddress + paramURL
        
        response = requests.get(fullURL, params = parameters)
        if response.status_code == 200:
            data = response.json()
            print(f"Successful HTTP POST Operation!\n{fullURL}\n>>> DATA:\n{data}\n")
            return data
        else:
            return -1
        #end-if-else
    #end-def
    
    def postHTTP(self, paramURL: str="", parameters: dict={}) -> int:
        fullURL = self.cameraFullAddress + paramURL
        
        response = requests.get(fullURL, params = parameters)
        if response.status_code == 200:
            print(f"Successful HTTP POST Operation!\n>>>{fullURL}\n>>>{parameters}\n")
            return 1
        else:
            print(f"Error in HTTP POST Operation!\n>>>{fullURL}\n>>>{parameters}\n")
            return -1
        #end-if-else
    #end-def
    
    
#end-class



if __name__ == "__main__":
    logger = logger.setupLogger()
    try:
        gopro = goProHero10()
        logging.info(gopro.showConnectionDetails())
        #gopro.keepAliveSignal()
        
        #------------------------
        #Adjust Resolution + Fov
        desiredResolution = gopro.resolutions["1080p"]
        desiredFov = gopro.fovs["wide"]
        
        gopro.startWebcam["params"]["res"] = desiredResolution
        gopro.startWebcam["params"]["fov"] = desiredFov
        
        #------------------------
        #Apply changes to Fov and Resolution (fist turn camera off and restart)
        currentStatus = gopro.getCameraState()
        print(currentStatus)
        if (currentStatus == "idle"):
            gopro.getHTTP(paramURL  = gopro.startWebcam["url"],
                          parameters= gopro.startWebcam["params"])
        else:
            print("Camera is not available for webcam mode ...")
            gopro.getHTTP(paramURL = gopro.exitWebcamPreview["url"])
            countdown(delay=5, message="Closing Webcam preview ...")
        #end-if-else
 
        
    except:
        print(traceback.format_exc())
        logging.error(traceback.format_exc())
    #end-try-except

    
    
#end-if-else
