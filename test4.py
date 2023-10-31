#!/bin/python3
from cardreader import *
from controller import *
from game import *
from config import cfg
from threading import Lock

import RPi.GPIO as GPIO
from time import sleep
from time import time as gettime


BUTTON = 12

action_function_map = {
    Actions.GO_FORWARD       : controller_forward,
    Actions.GO_FASTFORWARD   : controller_fastforward,
    Actions.GO_BACKWARD      : controller_backward,
    Actions.GO_RIGHT         : controller_right,
    Actions.GO_LEFT          : controller_left,
    Actions.ROTATE_RIGHT     : controller_rotate,
    Actions.ROTATE_LEFT      : controller_crotate,
    Actions.DANCE            : controller_dance,
    Actions.MUSIC            : controller_music,
    Actions.FIRE             : controller_fire,
        }

action_card_map = {
    0x935ab71866 : Actions.ROTATE_LEFT,
    0x63fec40950 : Actions.ROTATE_RIGHT,
    0x73bf3108f5 : Actions.ROTATE_LEFT,
    0x6350750a4c : Actions.FIRE,
    0xa3a4840a89 : Actions.FN_TAG,
    0xe3773b13bc : Actions.FN_TAG,
    0x430c550a10 : Actions.ROTATE_LEFT,
    0xe347351382 : Actions.FIRE,
    0xc3766b0ad4 : Actions.DANCE,
    0xd37ce50943 : Actions.GO_BACKWARD,
    0x53aa4d0abe : Actions.GO_FORWARD,
    0xf3ee7e0a69 : Actions.GO_RIGHT,
    0x63fa4c13c6 : Actions.GO_RIGHT,
    0xf3f8e109e3 : Actions.ROTATE_RIGHT,
    0x83297f0adf : Actions.ROTATE_LEFT,
    0x137f500a36 : Actions.GO_RIGHT,
    0x938d630a77 : Actions.ROTATE_RIGHT,
    0x0382811111 : Actions.GO_FASTFORWARD,
    0x2366810ace : Actions.ROTATE_RIGHT,
    0x33006f0a56 : Actions.GO_RIGHT,
    0x13509311c1 : Actions.GO_FORWARD,
    0xd39c090a4c : Actions.GO_LEFT,
    0xe38bdb09ba : Actions.MUSIC,
    0xc3a0d409be : Actions.FN_CALL,
    0xb34a4b13a1 : Actions.FN_CALL,
    0x53e8e5114f : Actions.FN_CALL,
    0x134a820ad1 : Actions.FN_CALL,
        }

def process_action_queue(action_queue):
    for a in action_queue:
        if is_running:
          action_function_map[a]()
        else:
            print("Stopped. Won't do the action in the list.")
            return

is_running = False
last_callback : int

milliseconds = lambda: int(gettime() * 1000)

def button_callback(channel):
    global is_running, last_callback
    cur_time = milliseconds()
    if cur_time - last_callback < 1500:
        last_callback = cur_time
        return
    last_callback = cur_time
    if is_running:
        is_running = False
        print("stopped")
    else:
        is_running = True
        print("started")
    # if game_mutex.acquire(blocking=False):
    #     print("pressed and proceessed")
    #     sleep(10)
    #     game_mutex.release()
    # else:
    #     print("passed callback")
    #     return

def run_game():
    controller_con_test()
    try:
        if is_running:
            controller_sound(5)
            reads = read_process()
        else:
            print("Stopped. Won't read card action list.")
            controller_sound(15)
            return

        if is_running:
            action_list = list()
            for number, id in sorted(reads.items()):
                print("RFID NUMBER: %d KEY ID: %s " % (number, hex(id)))
                action_list.append(action_card_map[id])
            game = Game(action_list)
            print(game.get_action_queue())
        else:
            print("Stopped. Won't process card action list.")
            controller_sound(15)
            return

        if is_running:
            process_action_queue(game.get_action_queue())
        else:
            print("Stopped. Won't process game action list.")
            controller_sound(15)
            return

    except GameLogicError as err:
        print("ERR:",err.message)


if __name__ == '__main__':
    is_running = False
    last_callback = milliseconds()

    # Initializations
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON, GPIO.IN)
    GPIO.add_event_detect(BUTTON, GPIO.RISING, bouncetime=500, callback=button_callback)
    #read_init()
    #controller_init()

    # controller_test()

    #try:
     #  while True:
      #      time.sleep(2)
       #     while not is_running:
        #        time.sleep(0.4)
         #       controller_con_test()
          #  run_game()
           # controller_sound(7)
            #is_running = False
        #pass
    #finally:
     #   GPIO.cleanup()
      #  controller_close()
       # exit(0)

     game = Game(Actions.ROTATE_LEFT)
     print(game.get_action_queue())

