from time import sleep, time
import sys
from mfrc522 import MFRC522
import RPi.GPIO as GPIO

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
  readers.append(MFRC522(0, i, 100000, GPIO.BCM, pin_rst = RESET_PIN, debugLevel='INFO'))

# Its recommended to reset MFRC522 after each polling. Pulling Reset_Pin to low
# (by setting the ping to low mode in out settings) turns off the sensors until
# the pin is high again.
try:
  for reader in readers:
    print(reader)
    reader.MFRC522_Init()
    reader.Write_MFRC522(0x04, 0x00)
    reader.Write_MFRC522(0x02, 0xFF)
    reader.Write_MFRC522(0x09, 0x26)
    reader.Write_MFRC522(0x01, 0x0C)
    reader.Write_MFRC522(0x0D, 0x87)
    print(reader.Read_MFRC522(MFRC522.CommIrqReg))
  while True:
    print(readers[0].Read_MFRC522(MFRC522.CommIrqReg))

except KeyboardInterrupt:
  GPIO.output(RESET_PIN, GPIO.LOW)
  GPIO.cleanup()
  raise
