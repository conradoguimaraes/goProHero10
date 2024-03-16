#Turbo Transfer
turboTransfer = {
                    "mode": "post",
                    "url": "/gopro/media/turbo_transfer",
                    "params": {"p": 0},
                    "params_info": {
                                    "p=0 <int>": "disable",
                                    "p=1 <int>": "enable"
                                },
                    "response": {
                                    200: "Successful operation."
                                },
                    "response_info": {}
                }


#Wired Camera Control over USB
wiredCamera =  {
                    "mode": "post",
                    "url": "/gopro/camera/control/wired_usb",
                    "params": {"p": 0},
                    "params_info": {
                                    "p=0 <int>": "disable usb control",
                                    "p=1 <int>": "enable wired usb control"
                                    },
                    "response": {
                                    200: "Successful operation."
                                },
                    "response_info": {}
                }


#Keep Alive Signal: gopro.keepAliveSignal()
keepAlive = {
                "mode": "post",
                "url": "/gopro/camera/keep_alive",
                "response": {
                                200: "Successful operation."
                            },
                "response_info": {}
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
                                },
                    "response": {
                                    200: "Successful operation."
                                },
                    "response_info": {}
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
                                },
                "response": {
                                200: "Successful operation."
                            },
                "response_info": {}
            }

#Set Digital Zoom
digitalZoom = {
                    "mode": "post",
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
                "mode": "post",
                "url": "/gopro/camera/shutter/{mode}",
                "params": {},
                "params_info": {"mode": "must change in the URL '{mode}' to 'start' or 'stop'"},
                "response": {
                                200: "Successful operation."
                            },
                "response_info": {}
          }