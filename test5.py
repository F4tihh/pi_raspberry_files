from controller import *
import RPi.GPIO as GPIO

FORWARD_PIN = 18

def forward():
    GPIO.output(FORWARD_PIN, GPIO.HIGH)

def stop():
    GPIO.output(FORWARD_PIN, GPIO.LOW)

# GPIO ayarlamalarý
GPIO.setmode(GPIO.BCM)
GPIO.setup(FORWARD_PIN, GPIO.OUT)

try:
    forward()  # Robot ileri gitmeye baþlar
    while True:
        # Robotun ileri gitmeye devam etmesini saðlamak için ekstra iþlemler burada yapýlabilir
        pass

except KeyboardInterrupt:
    pass
finally:
    stop()
    GPIO.cleanup()