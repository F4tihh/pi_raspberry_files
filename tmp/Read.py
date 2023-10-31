from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
reader = SimpleMFRC522(0,3)
reader2= SimpleMFRC522(0,4)
reader3= SimpleMFRC522(0,5)
reader4= SimpleMFRC522(0,2)
GPIO.setup(37, GPIO.OUT)

#reader3= SimpleMFRC522(0,2)
#reader4= SimpleMFRC522(0,1)
try:
    while True:
        print("Hold a tag near the reader")
        GPIO.output(37, GPIO.HIGH)
        sleep(0.1)
        reader.READER.MFRC522_Init();
        reader2.READER.MFRC522_Init();
        reader3.READER.MFRC522_Init();
        reader4.READER.MFRC522_Init();

        id = reader.read_id()
        if id:
            print("READ:1 ID: %s\n" % (id))
        id2 = reader2.read_id()
        if id2:
            print("READ:2 ID: %s\n" % (id2))
        id3 = reader3.read_id()
        if id3:
            print("READ:3 ID: %s\n" % (id3))
        id4 = reader4.read_id()
        if id4:
            print("READ:4 ID: %s\n" % (id4))
        GPIO.output(37, GPIO.LOW)
        sleep(0.1)
# id4, text4 = reader4.read()
# print("ID: %s\nText: %s" % (id4,text4))
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
