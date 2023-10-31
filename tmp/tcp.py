# -*-coding:utf-8-*-
# Copyright (c) 2020 DJI.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time
import curses
from robomaster import robot,config,chassis

rpm_speed = 50
rpm_timeout = 2.7

rpm_backwhe_error = 5

def forward():
  # ep_chassis.drive_speed(x=1, timeout=0.75)
  ep_chassis.drive_wheels(w1=rpm_speed, w2=rpm_speed, w3=rpm_speed, w4=rpm_speed, timeout=rpm_timeout)
  time.sleep(3)
def backward():
  # ep_chassis.drive_speed(x=-1, timeout=0.75)
  ep_chassis.drive_wheels(w1=-rpm_speed, w2=-rpm_speed, w3=-rpm_speed, w4=-rpm_speed, timeout=rpm_timeout)
  time.sleep(3)
def left():
  # ep_chassis.drive_wheels(w1=-rpm_speed, w2=rpm_speed, w3=rpm_speed, w4=-(rpm_speed-10), timeout=rpm_timeout)
  ep_chassis.drive_wheels(w1=-rpm_speed, w2=rpm_speed, w3=(rpm_speed-rpm_backwhe_error), w4=-(rpm_speed-rpm_backwhe_error), timeout=rpm_timeout)
  # ep_chassis.drive_speed(y=-1, timeout=0.5)
  # ep_chassis.move(y=0.50,xy_speed=0.2).wait_for_completed()
  # ep_chassis.move(y=0.0,xy_speed=0.0)
  time.sleep(3)
def right():
  ep_chassis.drive_wheels(w1=rpm_speed, w2=-rpm_speed, w3=-(rpm_speed-rpm_backwhe_error), w4=(rpm_speed-rpm_backwhe_error), timeout=rpm_timeout)
  # ep_chassis.drive_wheels(w1=0, w2=0, w3=-rpm_speed, w4=(rpm_speed-10), timeout=rpm_timeout)
  time.sleep(3)

rotate_rpm = 30
rotate_timeout = 2.3

def rotate():
  # ep_chassis.drive_wheels(w1=rpm_speed, w2=-rpm_speed, w3=rpm_speed, w4=-rpm_speed, timeout=1.48)
  ep_chassis.drive_wheels(w1=-rotate_rpm, w2=rotate_rpm, w3=0, w4=0, timeout=rotate_timeout)
  # ep_chassis.drive_speed(y=-1, timeout=0.5)
  time.sleep(3)
def counter_rotate():
  # ep_chassis.drive_wheels(w1=-rpm_speed, w2=rpm_speed, w3=-rpm_speed, w4=rpm_speed, timeout=1.48)
  ep_chassis.drive_wheels(w1=rotate_rpm, w2=-rotate_rpm, w3=0, w4=0, timeout=rotate_timeout)
  time.sleep(3)


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="sta", proto_type='udp')

    ep_chassis = ep_robot.chassis
    pos = ep_chassis.sub_position()
    print("->",type(ep_robot.dds))

    x_val = 0.2
    y_val = 0.2
    z_val = 30

    while True:
        # get keyboard input, returns -1 if none available
        c = input()
        if c == 'w':
            forward()
        elif c == 's':
            backward()
        elif c == 'a':
            left()
        elif c == 'd':
            right()
        elif c == 'q':
            rotate()
        elif c == 'e':
            counter_rotate()
        elif c == 'j':
            print("ffs")
            quit()


    # 前进 0.5米
    ep_chassis.drive_wheels(w1=40, w2=-40, w3=40, w4=-40, timeout=10)
    #
    time.sleep(12)
    ep_robot.close()
