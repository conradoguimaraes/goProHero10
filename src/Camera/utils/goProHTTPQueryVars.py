#Get Camera State and Settings
getCameraState = {
                    "mode": "get",
                    "url": "/gopro/camera/state",
                    "params": {},
                    "params_info": {},
                    "response": {
                                    200: "Successfully retrieved settings and status."
                                },
                    "response_info": {
                                        200: {
                                                "settings": "check official docs for full description of return parameters / json",
                                                "status": "check official docs for full description of return parameters / json"
                                            }
                                        }
                }


#Get Date and Time
getDateTime = {
                    "mode": "get",
                    "url": "/gopro/camera/get_date_time",
                    "params": {},
                    "params_info": {},
                    "response": {
                                    200: "Successfully retrieved current date and time."
                                },
                    "response_info": {
                                        200: {
                                                "date": "<str> current date in format YYYY_MM_DD",
                                                "dst": " <int> Is daylight savings time active? [0 or 1]",
                                                "time": "<str> current time in format HH_MM_SS",
                                                "tzone": "<int> Timezone offset in minutes"
                                            }
                                        }
                }

#Get Hardware Info
getHardwareInfo = {
                    "mode": "get",
                    "url": "/gopro/camera/info",
                    "params": {},
                    "params_info": {},
                    "response": {
                                    200: "Successfully retrieved hardware info."
                                },
                    "response_info": {
                                        200: {
                                                "info": "check official docs for full description of return parameters / json"
                                            }
                                        }
                }

"""
#Hardware Info JSON:
{
    "info": 
    {
        "ap_mac_addr": "065747046ceb",
        "ap_ssid": "GP24645504",
        "firmware_version": "H23.01.01.10.00",
        "model_name": "Hero12 Black",
        "model_number": "62",
        "serial_number": "C3501324645504"
    } 
}
"""



#Get Last captured media - already implemented in goProHTTPMediaVars.py


