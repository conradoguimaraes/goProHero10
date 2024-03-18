#Anti-Flicker (134)
antiFlicker = {
                    "mode": "get",
                    "url": "/gopro/camera/setting/134/{option}",
                    "params": {},
                    "params_info": {
                                    "option": "must change in the URL '{option}' to 2 (60Hz) | 1 (50Hz)"
                                },
                    "response": {
                                    200: "Request was successfully received by the camera."
                                },
                    "response_info": {}
                }


#Aspect Ratio (108)
aspectRatio = "not supported on Hero 10 Black"


#Auto Power Down (59)
autoPowerDown = {
                    "mode": "get",
                    "url": "/gopro/camera/setting/59/{option}",
                    "params": {},
                    "params_info": {
                                    "option": "must change in the URL '{option}' to 0 (never), 1 (1min), 4 (5min), 6 (15min) or 7 (30min)"
                                },
                    "response": {
                                    200: "Request was successfully received by the camera."
                                },
                    "response_info": {}
                }


#Bit Depth (183)
bitDepth = "not supported on Hero 10 Black"

#Bit Rate (182)
bitRate = "not supported on Hero 10 Black"

#Controls (175)
controls = "not supported on Hero 10 Black"

#Duration (172)
duration = "not supported on Hero 10 Black"

#Easy Mode Speed (176)
easyModeSpeed = "not supported on Hero 10 Black"

#Enable Night Photo (177)
nightPhoto =  "not supported on Hero 10 Black"

#Frames per Second (3)
fps = {
            "mode": "get",
            "url": "/gopro/camera/setting/3/{option}",
            "params": {},
            "params_info": {
                            "option": "must change in the URL '{option}' to 0 (240fps), 1 (120fps), 2 (100fps), 5 (60fps), 6 (50fps), 8 (30fps), 9 (25fps), 10 (24fps), 13 (200fps)"
                        },
            "response": {
                            200: "Request was successfully received by the camera."
                        },
            "response_info": {}
        }

#Framing (193)
framing = "not supported on Hero 10 Black"

#GPS (83)
gps = {
            "mode": "get",
            "url": "/gopro/camera/setting/83/{option}",
            "params": {},
            "params_info": {
                            "option": "must change in the URL '{option}' to 0 (OFF) or 1 (ON)."
                        },
            "response": {
                            200: "Request was successfully received by the camera."
                        },
            "response_info": {}
        }

#Hindsight (167) - "the camera continuously records audio and video, but only saves 15 or 30 seconds to the SD card when you hit the shutter button"
hindsight = {
            "mode": "get",
            "url": "/gopro/camera/setting/167/{option}",
            "params": {},
            "params_info": {
                            "option": "must change in the URL '{option}' to 2 (15s), 3 (30s) or 4 (OFF)."
                        },
            "response": {
                            200: "Request was successfully received by the camera."
                        },
            "response_info": {}
        }


#Horizon Leveling (150)
horizonLeveling1 = "not supported on Hero 10 Black"

#Horizon Leveling (151)
horizonLeveling2 = "not supported on Hero 10 Black"

#Hypersmooth (135)
hypersmooth = {
            "mode": "get",
            "url": "/gopro/camera/setting/135/{option}",
            "params": {},
            "params_info": {
                            "option": "must change in the URL '{option}' to 0 (OFF), 2 (HIGH), 3 (BOOST) or 100 (STANDARD)."
                        },
            "response": {
                            200: "Request was successfully received by the camera."
                        },
            "response_info": {}
        }

#Interval (171)
interval = "not supported on Hero 10 Black"

#Lapse Mode (187)
lapseMode = "not supported on Hero 10 Black"

#Lens (121)
lens1 = {
            "mode": "get",
            "url": "/gopro/camera/setting/121/{option}",
            "params": {},
            "params_info": {
                            "option": "must change in the URL '{option}' to 0 (WIDE), 2 (NARROW), 3 (SUPERVIEW), 4 (LINEAR), 7 (MAX SUPERVIEW) or 8 (LINEAR+HORIZON LEVELING)."
                        },
            "response": {
                            200: "Request was successfully received by the camera."
                        },
            "response_info": {}
        }

#Lens (122)
lens2 = {
            "mode": "get",
            "url": "/gopro/camera/setting/122/{option}",
            "params": {},
            "params_info": {
                            "option": "must change in the URL '{option}' to  19 (NARROW), 100 (MAX SUPERVIEW), 101 (WIDE), 102 (LINEAR)."
                        },
            "response": {
                            200: "Request was successfully received by the camera."
                        },
            "response_info": {}
        }


#Max Lens (162)
maxLens = {
            "mode": "get",
            "url": "/gopro/camera/setting/162/{option}",
            "params": {},
            "params_info": {
                            "option": "must change in the URL '{option}' to  0 (OFF) or 1 (ON)."
                        },
            "response": {
                            200: "Request was successfully received by the camera."
                        },
            "response_info": {}
        }

#Max Lens Mod (189)
maxLensMod = "not supported on Hero 10 Black"

#Max Lens Mod Enable (190)
maxLensModEnable = "not supported on Hero 10 Black"

#Media Format (128)
mediaFormat = {
            "mode": "get",
            "url": "/gopro/camera/setting/128/{option}",
            "params": {},
            "params_info": {
                            "option": "must change in the URL '{option}' to  13 (Time Lapse Video), 20 (Time Lapse Photo), 21 (Night Lapse Photo) or 26 (Night Lapse Video)."
                        },
            "response": {
                            200: "Request was successfully received by the camera."
                        },
            "response_info": {}
        }

#Photo Mode (191)
photoMode = "not supported on Hero 10 Black"

#Profiles (184)
profiles = "not supported on Hero 10 Black"

#Resolutions (2)
resolutions = {
                    "mode": "get",
                    "url": "/gopro/camera/setting/2/{option}",
                    "params": {},
                    "params_info": {
                                    "option": "must change in the URL '{option}' to  1 (4K), 4 (2.7K), 6 (2.7K4:3), 9 (1080), 18 (4K4:3), 25 (5K4:3) or 100 (5:3K)."
                                },
                    "response": {
                                    200: "Request was successfully received by the camera."
                                },
                    "response_info": {}
                }

#Time Lapse Digital Lenses (123)
timeLapseDigitalLens = {
                    "mode": "get",
                    "url": "/gopro/camera/setting/123/{option}",
                    "params": {},
                    "params_info": {
                                    "option": "must change in the URL '{option}' to  19 (NARROW), 100 (MAX SUPERVIEW), 101 (WIDE), 102 (LINEAR)."
                                },
                    "response": {
                                    200: "Request was successfully received by the camera."
                                },
                    "response_info": {}
                }

#Trail Length (179)
trailLength = "not supported on Hero 10 Black"

#Video Mode (180)
videoMode1 = "not supported on Hero 10 Black"

#Video Mode (186)
videoMode2 = "not supported on Hero 10 Black"

#Video Performance Mode (173)
videoPerformanceMode = {
                    "mode": "get",
                    "url": "/gopro/camera/setting/173/{option}",
                    "params": {},
                    "params_info": {
                                    "option": "must change in the URL '{option}' to  0 (MAXIMUM), 1 (EXTENDED BATTERY) or 2 (TRIPOD/STATIONARY VIDEO)."
                                },
                    "response": {
                                    200: "Request was successfully received by the camera."
                                },
                    "response_info": {}
                }

#Webcam Digital Lenses (43)
webcamLens = {
                "mode": "get",
                "url": "/gopro/camera/setting/43/{option}",
                "params": {},
                "params_info": {
                                "option": "must change in the URL '{option}' to 0 (WIDE), 2 (NARROW), 3 (SUPERVIEW) or  4 (LINEAR)."
                            },
                "response": {
                                200: "Request was successfully received by the camera."
                            },
                "response_info": {}
            }

#Wireless Band (178)
wirelessBand = "not supported on Hero 10 Black"

