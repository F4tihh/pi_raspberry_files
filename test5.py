from controller import *
import RPi.GPIO as GPIO

FORWARD_PIN = 18

def forward():
    GPIO.output(FORWARD_PIN, GPIO.HIGH)

def stop():
    GPIO.output(FORWARD_PIN, GPIO.LOW)

# GPIO ayarlamalar�
GPIO.setmode(GPIO.BCM)
GPIO.setup(FORWARD_PIN, GPIO.OUT)

try:
    forward()  # Robot ileri gitmeye ba�lar
    while True:
        # Robotun ileri gitmeye devam etmesini sa�lamak i�in ekstra i�lemler burada yap�labilir
        pass

except KeyboardInterrupt:
    pass
finally:
    stop()
    GPIO.cleanup()