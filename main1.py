from cardreader2 import *
from controller import *
from game import *
from config import cfg
from threading import Lock
from time import time, sleep
import time 
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
     1: Actions.ROTATE_LEFT,
     2: Actions.GO_RIGHT,
     3: Actions.GO_FORWARD,
     4: Actions.GO_BACKWARD,
     5: Actions.DANCE,
     6: Actions.FN_CALL,
     7: Actions.MUSIC,
     8: Actions.GO_FASTFORWARD,
     9: Actions.FN_TAG,
    10: Actions.FIRE,
    11: Actions.GO_BACKWARD,
    12: Actions.GO_LEFT,
    13: Actions.FN_CALL,
    14: Actions.FN_TAG,
    15: Actions.GO_RIGHT,
}

is_running = False

def process_action_queue(action_queue):
    for a in action_queue:
        if is_running:
            action_function_map[a]()
        else:
            print("Stopped. Won't do the action in the list.")
            return

def run_game():
    controller_con_test()
    try:
        if is_running:
            controller_sound(5)
            reads = read_process()
            print("Reads:", reads)
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
        print("ERR:", err.message)

if __name__ == '__main__':
    is_running = True

    try:
        while True:
            time.sleep(2)
            while not is_running:
                time.sleep(0.4)
            run_game()
            controller_sound(7)
            is_running = False
    except KeyboardInterrupt:
        exit(0)