from picamera2 import Picamera2, Preview
import time
from datetime import datetime
from gpiozero import Button
import RPi.GPIO as GPIO
from signal import pause
import random

button = Button(24)
LED=18
GPIO.setup(LED,GPIO.OUT)
for x in range(12):
    time.sleep(0.05)
    GPIO.output(LED,1)
    print("LED" + str(x))
    time.sleep(0.05)
    GPIO.output(LED,0)
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (4056, 3040)})
picam2.configure(camera_config)
#picam2.still_configuration.size = (4056.3040)
picam2.start()
capture_config = picam2.create_still_configuration(raw={"size": (4056, 3040)})
def capture():
    rnum1=random.randrange(1,10000)
    filen3='/home/pi/Desktop/coralPics/%s.jpg' % rnum1
    filen4='/home/pi/Desktop/coralPics/%s.dng' % rnum1
    #picam2.start()
    capture_config = picam2.create_still_configuration(raw={"size": (4056, 3040)})
    print("test")
    picam2.switch_mode_and_capture_file(capture_config, filen4, name="raw")
    picam2.capture_file(filen3)
    #picam2.stop()
    for x in range(5):
       time.sleep(0.05)
       GPIO.output(LED,1)
       print("LED" + str(x))
       time.sleep(0.05)
       GPIO.output(LED,0)
    
    
button.when_pressed = capture
pause()