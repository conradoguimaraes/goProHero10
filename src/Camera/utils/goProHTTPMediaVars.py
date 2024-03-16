#Download a Media File
downloadMediaFile = {
                        "mode": "get",
                        "url": "/videos/DCIM/{directory}/{filename}",
                        "params": {},
                        "params_info": {
                                        "directory": "must change in the URL '{directory}' to the desired directory",
                                        "filename":  "must change in the URL '{filename}' to the desired filename"
                                    },
                        "response": {
                                        200: "Successful operation."
                                    },
                        "response_info": {}
                    }

#Get Last Captured Media
downloadLastMediaFile = {
                        "mode": "get",
                        "url": "/gopro/media/last_captured",
                        "params": {},
                        "params_info": {
                                        "directory": "must change in the URL '{directory}' to the desired directory",
                                        "filename":  "must change in the URL '{filename}' to the desired filename"
                                    },
                        "response": {
                                        200: "Successful last captured media.",
                                        204: "There is no last media for the camera to report."
                                    },
                        "response_info": {
                                            200: {
                                                    "file": "Filename of the media",
                                                    "folder": "Directory in which the media is contained in"
                                                 }
                                         }
                        }


#Get Media File GPMF
mediaFileGPMF = "not implemented"

#Get Media File INFO
getMediaFileInfo = {
                        "mode": "get",
                        "url": "/gopro/media/info",
                        "params": {"path": "100GOPRO/GOPR0002.JPG"},
                        "params_info": {
                                        "path": "filepath: directory plus filename (video/photo) with extension"
                                    },
                        "response": {
                                        200: "Successfully retrieved file (video/photo) metadata."
                                    },
                        "response_info": {
                                            200: {
                                                    "VideoMetadata": "check official docs for full description of return parameters / json",
                                                    "PhotoMetadata": "check official docs for full description of return parameters / json"
                                                 }
                                         }
                    }

#Get Media File Screennail
getMediaFileScreennail = {
                            "mode": "get",
                            "url": "/gopro/media/screennail",
                            "params": {"path": "100GOPRO/GOPR0002.JPG"},
                            "params_info": {
                                            "path": "filepath: directory plus filename with extension"
                                        },
                            "response": {
                                            200: "Successfully retrieved file preview image (screennail)."
                                        },
                            "response_info": {}
                        }

#Get Media File Telemetry
getMediaFileTelemetry = {
                            "mode": "get",
                            "url": "/gopro/media/telemetry",
                            "params": {"path": "100GOPRO/GOPR0002.JPG"},
                            "params_info": {
                                            "path": "filepath: directory plus filename with extension"
                                        },
                            "response": {
                                            200: "Successfully retrieved file binary telemetry data."
                                        },
                            "response_info": {}
                        }

#Get Media File Thumbnail
getMediaFileThumbnail = {
                            "mode": "get",
                            "url": "/gopro/media/thumbnail",
                            "params": {"path": "100GOPRO/GOPR0002.JPG"},
                            "params_info": {
                                            "path": "filepath: directory plus filename with extension"
                                        },
                            "response": {
                                            200: "Successfully retrieved file preview image (thumbnail)."
                                        },
                            "response_info": {}
                        }

#Get Media List
getMediaFileThumbnail = {
                            "mode": "get",
                            "url": "/gopro/media/list",
                            "params": {},
                            "params_info": {},
                            "response": {
                                            200: "Successfully retrieved media list."
                                        },
                            "response_info": {
                                                200: {
                                                           "id": "check official docs for full description of return parameters / json",
                                                        "media": "check official docs for full description of return parameters / json"
                                                    }
                                             }
                        }