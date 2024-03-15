# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:24:27 2024

@author: Admin
"""

#%%
from pygrabber.dshow_graph import FilterGraph


def get_available_cameras() :
    #https://stackoverflow.com/questions/70886225/get-camera-device-name-and-port-for-opencv-videostream-python
    devices = FilterGraph().get_input_devices()

    available_cameras = {}

    for device_index, device_name in enumerate(devices):
        available_cameras[device_index] = device_name
    
    
    print(available_cameras)
    return available_cameras

