import os, time

while True:
    os.system("fswebcam -r 1920x1080 --no-banner -d /dev/video0 out/camera0.png")
    time.sleep(.5)
