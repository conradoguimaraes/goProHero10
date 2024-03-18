#Turbo Transfer
turboTransfer = {
                    "mode": "get",
                    "url": "/gopro/media/turbo_transfer",
                    "params": {"p": 0},
                    "params_info": {
                                    "p": "<int> 0 (disable) or 1 (enable)"
                                },
                    "response": {
                                    200: "Successful operation."
                                },
                    "response_info": {}
                }


#Wired Camera Control over USB
wiredCamera =  {
                    "mode": "get",
                    "url": "/gopro/camera/control/wired_usb",
                    "params": {"p": 0},
                    "params_info": {
                                    "p": "<int> 0 (disable) or 1 (enable) wired usb control"
                                    },
                    "response": {
                                    200: "Successful operation."
                                },
                    "response_info": {}
                }


#Keep Alive Signal: gopro.keepAliveSignal()
keepAlive = {
                "mode": "get",
                "url": "/gopro/camera/keep_alive",
                "response": {
                                200: "Successful operation."
                            },
                "response_info": {}
            }

"""
In order to maximize battery life, GoPro cameras automatically go to sleep after some time. 
This logic is handled by a combination of the Auto Power Down setting which most (but not all) 
cameras support and a Keep Alive message that the user can regularly send to the camera.

The camera will automatically go to sleep if both timers reach zero.

The Auto Power Down timer is reset when the user taps the LCD screen, presses a button on the 
camera, programmatically (un)sets the shutter, sets a setting, or loads a Preset.

The Keep Alive timer is reset when the user sends a keep alive message.

The best practice to prevent the camera from inadvertently going to sleep is to start sending 
Keep Alive messages every 3.0 seconds after a connection is established.
"""




#Camera Control Status
cameraControl = {
                    "mode": "get",
                    "url": "/gopro/camera/control/set_ui_controller",
                    "params": {"p": 0},
                    "params_info": {
                                    "p": "<int> 0 (CAMERA_IDLE), 1 (CAMERA_CONTROL) or 2 (CAMERA_EXTERNAL_CONTROL)"
                                },
                    "response": {
                                    200: "Successful operation."
                                },
                    "response_info": {}
                }

#Set Date/Time
dateTime = {
                "mode": "get",
                "url": "/gopro/camera/set_date_time",
                "params": {
                            "date": "2023_12_31",
                            "time": "16_30_00"
                            },
                "params_info": {
                                "date <str>": "current date in format YYYY_MM_DD",
                                "time <str>": "current time in format HH_MM_SS in 24 hour format"
                                },
                "response": {
                                200: "Successful operation."
                            },
                "response_info": {}
            }

#Set Digital Zoom
digitalZoom = {
                    "mode": "get",
                    "url": "/gopro/camera/digital_zoom",
                    "params": {"percent": 0},
                    "params_info": {"percent=x <int>": "Set Zoom level of X (0-100)"},
                    "response": {
                                    200: "Successful operation."
                                },
                    "response_info": {}
              }


#Start Shutter
shutter = {
                "mode": "get",
                "url": "/gopro/camera/shutter/{mode}",
                "params": {},
                "params_info": {"mode": "must change in the URL '{mode}' to 'start' or 'stop'"},
                "response": {
                                200: "Successful operation."
                            },
                "response_info": {}
          }