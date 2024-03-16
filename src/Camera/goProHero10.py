import os
import requests
from utils.config import readConfig
import utils.goProHTTPControlVars as goProHTTPControlVars
import utils.goProHTTPMediaVars as goProHTTPMediaVars
class goProHero10:
    #https://gopro.github.io/OpenGoPro/http
    
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
