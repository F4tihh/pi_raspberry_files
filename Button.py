import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

BUTTON = 12
#BUTTON
LED = 20
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

try:
  while True:
    GPIO.wait_for_edge(BUTTON, GPIO.RISING)
    GPIO.output(LED, GPIO.HIGH)
    sleep(2)
    GPIO.output(LED, GPIO.LOW)
except KeyboardInterrupt:
  GPIO.output(LED, GPIO.LOW)
  GPIO.cleanup()
  raise