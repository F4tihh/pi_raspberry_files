import time
import curses
from robomaster import robot,config,chassis,gimbal,blaster,led
from game import *
from config import cfg
import pygame

ep_robot = robot.Robot()
ep_chassis : chassis.Chassis
ep_gimbal  : gimbal.Gimbal
ep_blaster  : blaster.Blaster
ep_led      : led.Led



pitch_degree = cfg["pitch_degree"]
def controller_con_test():
    if ep_robot.get_version() is None:
        exit(1)

def controller_init():
    global ep_chassis
    global ep_gimbal
    global ep_blaster
    global ep_led
    if not ep_robot.initialize(conn_type="sta", proto_type='udp'):
        print("Robot initialization failed")
        exit(1)
    #ep_robot.initialize(conn_type="sta", proto_type='udp')
    ep_chassis = ep_robot.chassis
    ep_gimbal = ep_robot.gimbal
    ep_blaster = ep_robot.blaster
    ep_led = ep_robot.led
    ep_led.set_led(r=0,g=0,b=255)
    # move pitch to the max
    # ep_gimbal.move(pitch=120, pitch_speed=90).wait_for_completed()
    # get it down to a certain degree
    ep_gimbal.moveto(yaw=0, pitch=pitch_degree, pitch_speed=90, yaw_speed=90).wait_for_completed()
    controller_sound(2)
    ep_led.set_led(r=255,g=255,b=0)

    #Upload sound files
    # upload_file = "/python/sdk_audio_9.wav"
    # ep_robot._ftp.upload("gameover.wav", upload_file)
    # ep_robot.play_sound(0xE0 + 9, times=1).wait_for_completed()

    # ep_robot._audio_id = (ep_robot._audio_id + 1) % 10
    # upload_file = "/python/sdk_audio_{0}.wav".format(ep_robot._audio_id)
    # ep_robot._ftp.upload(filename, upload_file)
    # logger.info("upload file {0} to target {1}".format(filename, upload_file))
    # sound_id = 0xE0 + (ep_robot._audio_id % 10)


### Actions ###

def controller_test():
    for i in range(25):
        print(i)
        time.sleep(1)
        controller_sound(i)
  # controller_fire()
    pass
  # controller_dance()
  # controller_crotate()
  # controller_sound()
  # controller_crotate()
  # controller_sound()
  # controller_powerforward()
  # controller_fire()
  # pass

def controller_close():
  ep_robot.close()

def _controller_brake():
  ep_chassis.drive_wheels(w1=0, w2=0, w3=0, w4=0)

rotate_degree = cfg["rotate_degree"]
rotate_speed = cfg["rotate_speed"]
yaw_speed = cfg["yaw_speed"]

# clockwise rotate
def controller_rotate():
  ep_chassis.move(z=-rotate_degree,z_speed=rotate_speed).wait_for_completed()
  ep_gimbal.move(yaw=rotate_degree,yaw_speed=yaw_speed).wait_for_completed()

# counter-clockwise rotate
def controller_crotate():
  ep_chassis.move(z=rotate_degree,z_speed=rotate_speed).wait_for_completed()
  ep_gimbal.move(yaw=-rotate_degree,yaw_speed=yaw_speed).wait_for_completed()

move_distance = cfg["move_distance"] + cfg["move_gain"]
move_speed = cfg["move_speed"]
move_fastspeed = cfg["move_fastspeed"]

def controller_forward():
  ep_chassis.move(x=move_distance,xy_speed=move_speed).wait_for_completed()
  _controller_brake()

def controller_backward():
  ep_chassis.move(x=-move_distance,xy_speed=move_speed).wait_for_completed()
  _controller_brake()

def controller_left():
  ep_chassis.move(y=-move_distance,xy_speed=move_speed).wait_for_completed()
  _controller_brake()

def controller_right():
  ep_chassis.move(y=move_distance,xy_speed=move_speed).wait_for_completed()
  _controller_brake()

def controller_fastforward():
  ep_chassis.move(x=move_distance,xy_speed=move_fastspeed).wait_for_completed()
  _controller_brake()

dance_angle = cfg["dance_angle"]
dance_half_angle = dance_angle / 2
dance_speed = cfg["dance_speed"]
dance_iter = cfg["dance_iter"]

def controller_dance():
    # ep_chassis.move(z=-90,z_speed=120)
    # ep_gimbal.move(yaw=-90,yaw_speed=120)
    ep_robot.play_audio("destiny.wav")
    #
    pygame.mixer.init()
    pygame.mixer.music.load("destiny.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    #
    ep_led.set_led(r=255,g=0,b=255,effect="flash")
    ep_chassis.move(z=dance_half_angle,z_speed=dance_speed).wait_for_completed()
    for _ in range(dance_iter):
        ep_chassis.move(z=-dance_angle,z_speed=dance_speed).wait_for_completed()
        ep_chassis.move(z=dance_angle,z_speed=dance_speed).wait_for_completed()
    ep_chassis.move(z=-dance_half_angle,z_speed=dance_speed).wait_for_completed()
    time.sleep(2)
    ep_led.set_led(r=255,g=255,b=0)

    # ep_gimbal.move(yaw=45,yaw_speed=120).wait_for_completed()
    # for _ in range(3):
    #     ep_gimbal.move(yaw=-90,yaw_speed=120).wait_for_completed()
    #     ep_gimbal.move(yaw=90,yaw_speed=120).wait_for_completed()
    # ep_gimbal.move(yaw=-45,yaw_speed=120).wait_for_completed()

    # ep_gimbal.move(yaw=, yaw_speed=120)
    # robot_ctrl.set_mode(rm_define.robot_mode_free)
    # chassis_ctrl.set_rotate_speed(120)
    # gimbal_ctrl.set_rotate_speed(120)
    # gun_ctrl.fire_continuous()
    # # while True:

    # gimbal_ctrl.rotate(rm_define.gimbal_right)
    # chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 0.2)
    # gimbal_ctrl.rotate(rm_define.gimbal_left)
    # chassis_ctrl.rotate_with_time(rm_define.clockwise, 0.4)
    # gimbal_ctrl.rotate(rm_define.gimbal_right)
    # chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 0.2)
    pass

def controller_music():
    ep_robot.play_audio("shark.wav").wait_for_completed()
    pass

def controller_sound(sound_id):
    ep_robot.play_sound(sound_id, times=1).wait_for_completed()

def controller_fire():
    ep_led.set_led(r=255,g=0,b=0)
    for i in [8, 15, 25]:
        for j in [-20, 0, 20]:
            ep_gimbal.moveto(yaw=j, pitch=i, pitch_speed=90, yaw_speed=90).wait_for_completed()
            ep_blaster.fire()
    ep_gimbal.moveto(yaw=0, pitch=pitch_degree, pitch_speed=90, yaw_speed=90).wait_for_completed()
    ep_led.set_led(r=255,g=255,b=0)

