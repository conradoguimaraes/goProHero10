from goprocam import GoProCamera, constants

import sys

gopro = GoProCamera.GoPro(webcam_device="usb0")

gopro.take_photo()

input(">>>")