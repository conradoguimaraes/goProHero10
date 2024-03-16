import os
import requests
from utils.config import readConfig


class goProHero10:
    #https://gopro.github.io/OpenGoPro/http
    
    #Turbo Transfer
    turboTransfer = {
                     "mode": "post",
                     "url": "/gopro/media/turbo_transfer",
                     "params": {"p": 0},
                     "params_info": {
                                     "p=0 <int>": "disable",
                                     "p=1 <int>": "enable"
                                    }
                    }
    
    #Wired Camera Control over USB
    wiredCamera = {
                   "mode": "post",
                   "url": "/gopro/camera/control/wired_usb",
                   "params": {"p": 0},
                   "params_info": {
                                   "p=0 <int>": "disable usb control",
                                   "p=1 <int>": "enable wired usb control"
                                  }
                  }
    
    #Keep Alive Signal: gopro.keepAliveSignal()
    keepAlive = {
                 "mode": "post",
                 "url": "/gopro/camera/keep_alive",
                }
    
    #Camera Control Status
    cameraControl = {
                     "mode": "post",
                     "url": "/gopro/camera/control/set_ui_controller",
                     "params": {"p": 0},
                     "params_info": {
                                     "p=0 <int>": "CAMERA_IDLE",
                                     "p=1 <int>": "CAMERA_CONTROL",
                                     "p=2 <int>": "CAMERA_EXTERNAL_CONTROL"
                                    }
                    }
    
    #Set Date/Time
    dateTime = {
                "mode": "post",
                "url": "/gopro/camera/set_date_time",
                "params": {
                           "date": "2023_12_31",
                           "time": "16_30_00"
                          },
                "params_info": {
                                "date <str>": "current date in format YYYY_MM_DD",
                                "time <str>": "current time in format HH_MM_SS in 24 hour format"
                               }
               }
    
    #Set Digital Zoom
    digitalZoom = {
                   "mode": "post",
                   "url": "/gopro/camera/digital_zoom",
                   "params": {"percent": 0},
                   "params_info": {"percent=x <int>": "Set Zoom level of X (0-100)"}
                  }
    
    
    #Start Shutter
    shutter = {
               "mode": "post",
               "url": "/gopro/camera/shutter/{mode}",
               "params": {},
               "params_info": {"mode": "must change in the URL '{mode}' to 'start' or 'stop'"}
              }

    #Hilight a Media File - Add a hilight / tag to an existing photo or media file
    hilightMediaFile = "not implemented"
    
    #Hilight while recording - Add hilight at current time while recording video (This can only be used during recording.)
    hilightRecording = "not implemented"
    
    #Remove hilight - Remove an existing hilight from a photo or video file.
    hilightRemove = "not implemented"
    
    
    #Download a Media File
    shutterStop = {
                   "mode": "post",
                   "url": "/videos/DCIM/{directory}/{filename}",
                   "params": {},
                   "params_info": {
                                   "directory": "must change in the URL '{directory}' to the desired directory",
                                   "filename":  "must change in the URL '{filename}' to the desired filename"
                                  }
                  }
    
    
    def __init__(self, goProHero10Config: str="goProHero10", cameraPort = "8080") -> None:
        config = readConfig(moduleName = goProHero10Config)
        
        serialX, serialY, serialZ = config["serialNrX"], config["serialNrY"], config["serialNrZ"]
        self.cameraPort = cameraPort
        self.cameraAddress = f"172.2{serialX}.1{serialY}{serialZ}.51"  + ":" + self.cameraPort
        self.cameraFullAddress = "http://" + self.cameraAddress
    #end-def
    
    def showConnectionDetails(self):
        print(f"IP Address: {self.cameraAddress}")
        print(f"Port: {self.cameraPort}")
        print(f"Camera Full Address: {self.cameraFullAddress}")
    #end-def
    

    def keepAliveSignal(self):
        self.postHTTP(paramURL = self.keepAlive["url"])
        return
    #end-def
    
    def getHTTP(self, paramURL: str="") -> int:
        fullURL = self.cameraFullAddress + paramURL
        
        response = requests.get(paramURL)
        if response.status_code == 200:
            data = response.json()
            print(f"Successful HTTP POST Operation!\n{fullURL}\n>>>DATA:\n{data}")
            return 1
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
    print("Ola")
    
    gopro = goProHero10()
    gopro.showConnectionDetails()
    
    
    
    
    
#end-if-else
