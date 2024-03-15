import os
import requests
from utils.config import readConfig


class goProHero10:
    # Enable TurboTransfer: gopro.turboTransfer["params"]["p"] = 1
    #Disable TurboTransfer: gopro.turboTransfer["params"]["p"] = 0
    turboTransfer = {"mode": "post",
                     "url": "/gopro/media/turbo_transfer",
                     "params": {"p": 0}
                    }
    
    # Enable wiredCamera: gopro.wiredCamera["params"]["p"] = 1
    #Disable wiredCamera: gopro.wiredCamera["params"]["p"] = 0
    wiredCamera = {"mode": "post",
                   "url": "/gopro/camera/control/wired_usb",
                   "params": {"p": 0}
                  }
    
    #Keep Alive Signal: gopro.keepAliveSignal()
    keepAlive = {"mode": "post",
                 "url": "/gopro/camera/control/keep_alive",
                }
    
    def __init__(self, goProHero10Config: str="goProHero10", cameraPort = "8080") -> None:
        config = readConfig(moduleName = goProHero10Config)
        
        serialX = config["serialNrX"]
        serialY = config["serialNrY"]
        serialZ = config["serialNrZ"]
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
