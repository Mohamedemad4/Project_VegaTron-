# Project_VegaTron- For Taqadam Make it Happen 2020
detect Drowsiness in car and truck Drivers Via computer vision and a raspberryPi

### The algorithm 

This is based on landmark detection using DLIB library. And then computing the EAR via [this formula](https://miro.medium.com/max/1544/1*6Ix1R90EmXixWYd5MGSJdQ.png);
and if the EAR has been lower than the ```ear_thresh``` for more than ```seconds_with_sub_ear``` it sounds the alarm 
also alerts the user if it can't detect their eyes.

## For Developers  
#### scripts dir. has all the Juice:
- Drowsiness_Detection.py is the main file that does the EAR calculations 
- blink.py has all the pin def. and access functions for the LEDs and Buzzers
- live_stream.py debug script that live streams the camera to port :5000
all the authors this work was based on are credited in their respective files
