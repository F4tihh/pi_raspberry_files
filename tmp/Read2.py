from time import sleep, time
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

poll_duration_in_s = 3
rfid_count = 18
readers = []
reads = dict()

poll_list = list()
for i in range(0, rfid_count):
  poll_list.append(i)
curr_poll_list = poll_list.copy()

GPIO.setmode(GPIO.BCM)
RESET_PIN = 21 # In BCM pin number. See: https://pinout.xyz

for i in range(0, rfid_count):
# Parameters are bus and device number respectively. Device number is allias to
# Chip Select (Slave Select) in SPI Protocol.
# /dev/spidev<bus>.<device>
# Pin association to the device numbers configured by device tree object.
# See: /home/alarm/spi-cs-extend.dts
# See: https://gist.github.com/mcbridejc/d060602e892f6879e7bc8b93aa3f85be
  readers.append(SimpleMFRC522(0, i, 800000))

# Its recommended to reset MFRC522 after each polling. Pulling Reset_Pin to low
# (by setting the ping to low mode in out settings) turns off the sensors until
# the pin is high again.
GPIO.setup(RESET_PIN, GPIO.OUT)

GPIO.output(RESET_PIN, GPIO.LOW)
sleep(0.01)

GPIO.output(RESET_PIN, GPIO.HIGH)
sleep(0.01)

try:
# One-shot reads might miss. So its better to poll multiple times.
  old_time = 0
  total_read = 0;
  while True:
    if time() - old_time < poll_duration_in_s:
      for i , v in enumerate(curr_poll_list):
        readers[v].READER.MFRC522_Init();
        # print(v)
        id = readers[v].read_id()
        if id:
          reads[v + 1] = id
          curr_poll_list.remove(v)
        #print("%d ID: %s" % (i, id))
      total_read += 1
      # print(curr_poll_list)
    else:
      for number, id in sorted(reads.items()):
        print("RFID NUMBER: %d KEY ID: %d" % (number, id))

      reads.clear()
      print("Total Read = %d.\tReading the devices..." % (total_read))
      total_read = 0
      old_time = time()
      curr_poll_list = poll_list.copy()
      GPIO.output(RESET_PIN, GPIO.LOW)
      sleep(0.05)

      GPIO.output(RESET_PIN, GPIO.HIGH)
      sleep(0.05)


except KeyboardInterrupt:
    GPIO.cleanup()
    raise
