from pirc522 import RFID
import signal
import time

poll_duration_in_s = 4
rfid_count = 6
readers = []
reads = dict()

GPIO.setmode(GPIO.BCM)
RESET_PIN = 2 # In BCM pin number. See: https://pinout.xyz

for i in range(0, rfid_count):
# Parameters are bus and device number respectively. Device number is allias to
# Chip Select (Slave Select) in SPI Protocol.
# /dev/spidev<bus>.<device>
# Pin association to the device numbers configured by device tree object.
# See: /home/alarm/spi-cs-extend.dts
# See: https://gist.github.com/mcbridejc/d060602e892f6879e7bc8b93aa3f85be
  readers.append(RFID(0, i, 10000000, RESET_PIN, ))

while True:

  rdr.wait_for_tag()

  (error, tag_type) = rdr.request()

  if not error:
    print("Tag detected")
    (error, uid) = rdr.anticoll()
    if not error:
      print("UID: " + str(uid))
