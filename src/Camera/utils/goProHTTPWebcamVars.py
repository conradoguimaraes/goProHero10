"""
Webcam

The webcam feature enables developers who are interested in writing custom drivers to broadcast the camera's 
video preview with a limited set of resolution, field of view, port, and protocol options.

While active, the webcam feature sends raw data to the connected client using a supported protocol. To enable 
multi-cam support, some cameras support running on a user-specified port. Protocol and port details are 
provided in a table below.

To test basic functionality, start the webcam, and use an application such as VLC to open a network stream:
Protocol 	Port
TS 	        udp://@:{PORT}
RTSP 	    rtsp://{CAMERA_IP}:554/live

For USB connections, prior to issuing webcam commands, Wired USB Control should be disabled.


Webcam Stabilization

Should the client require stabilization, the Hypersmooth setting can be used while in the state: READY (Status: OFF).
This setting can only be set while webcam is disabled, which requires either sending the Webcam Exit command or 
reseating the USB-C connection to the camera.

Note! The Low Hypersmooth option provides lower/lighter stabilization when used in Webcam mode vs other camera modes.

"""


#Enter Webcam Preview
enterWebcamPreview = {
                    "mode": "get",
                    "url": "/gopro/webcam/preview",
                    "params": {},
                    "params_info": {},
                    "response": {
                                    200: "Request was successfully received by the camera."
                                },
                    "response_info": {}
                }

#Exit Webcam Preview
exitWebcamPreview = {
                        "mode": "get",
                        "url": "/gopro/webcam/exit",
                        "params": {},
                        "params_info": {},
                        "response": {
                                        200: "Request was successfully received by the camera."
                                    },
                        "response_info": {
                            
                        }
                    }


#Get Webcam Status
getWebcamStatus = {
                        "mode": "get",
                        "url": "/gopro/webcam/status",
                        "params": {},
                        "params_info": {},
                        "response": {
                                        200: "Request was successfully received by the camera."
                                    },
                        "response_info": {
                                            200: {
                                                    "error": "Current webcam error (if status was not successful)\
                                                            0 (None), \
                                                            1 (Set Preset), \
                                                            2 (Set Window Size), \
                                                            3 (Exec Stream), \
                                                            4 (Shutter), \
                                                            5 (Com timeout), \
                                                            6 (Invalid param), \
                                                            7 (Unavailable), \
                                                            8 (Exit)",
                                                    "status": "Current webcam status\
                                                            0 (Off), 1 (Idle), 2 (High Power Preview), 3 (Low Power Preview)"
                                                }
                                            }
                    }

#Get Webcam Version
getWebcamVersion = {
                        "mode": "get",
                        "url": "/gopro/webcam/version",
                        "params": {},
                        "params_info": {},
                        "response": {
                                        200: "Request was successfully received by the camera."
                                    },
                        "response_info": {
                                            200: {
                                                    "max_lens_support": "<bool> Does the webcam support Max Lens Mod? True/False",
                                                    "usb_3_1_compatible": "<bool> Is the webcam USB 3.1 compatible? True/False",
                                                    "version": "<int> Current webcam version"
                                                }
                                            }
                    }

#Start Webcam
startWebcam = {
                    "mode": "get",
                    "url": "/gopro/webcam/start",
                    "params": {
                                "res": 12, 
                                "fov": 0
                               },
                    "params_info": {
                                    "res": "Resolution ID: 4 (480p), 7 (720p), 12 (1080p)",
                                    "fov": "FOV ID: 0 (Wide), 2 (Narrow), 3 (Superview), 4 (Linear)"
                                    },
                    "response": {
                                    200: "Successful operation."
                                },
                    "response_info": {}
                }

#Stop Webcam
stopWebcam = {
                    "mode": "get",
                    "url": "/gopro/webcam/stop",
                    "params": {},
                    "params_info": {},
                    "response": {
                                    200: "Successful operation."
                                },
                    "response_info": {}
                }




