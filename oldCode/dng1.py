#!/usr/bin/python3

# Capture a DNG and a JPEG made from the same raw data.

import time
import random
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (4056, 3040)})
picam2.configure(camera_config)
#picam2.still_configuration.size = (4056.3040)
picam2.start()
capture_config = picam2.create_still_configuration(raw={"size": (4056, 3040)})

rnum1=random.randrange(1,10000)
filen3='/media/pi/d1usb/pictures/%s.jpg' % rnum1
filen4='/media/pi/d1usb/pictures/%s.dng' % rnum1
print("test")
picam2.switch_mode_and_capture_file(capture_config, filen4, name="raw")
#picam2.switch_mode_and_capture_file(capture_config, filen3, name="main")
picam2.capture_file(filen3)
picam2.stop()