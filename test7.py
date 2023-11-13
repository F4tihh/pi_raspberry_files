# -*- coding: utf-8 -*-
from controller import *
from time import sleep, time

def read_process():
    # Read the image identification numbers from the `resim_id_listesi` list and return them as a dictionary.

    resim_id_listesi = [12, 11, 1, 2, 3, 4, 5, 10, 6]

    # The `resim_id_listesi` list contains the image identification numbers.

    operations = {
        1: controller_forward,
        2: controller_right,
        3: controller_backward,
        4: controller_left,
        5: controller_dance,
        6: controller_close,
        7: controller_crotate,
        8: controller_rotate,
        9: controller_fastforward,
        10: controller_music,
        11: controller_fire,
        12: controller_music1,
    }

    # The `operations` dictionary contains the functions that will be executed for each image identification number.

    try:
        reads = dict()
        for i in range(9):
            resim_id = resim_id_listesi[i]
            reads[i] = resim_id

            # Execute the corresponding function.
            if resim_id in operations:
                operations[resim_id]()
                sleep(1)  # Bu iniz gibi ayarlayabilirsiniz.
            else:
                print("Gersiz resim_id:", resim_id)

        return reads

    except KeyboardInterrupt:
        raise

def main():
    # Initialize the controller.
    controller_init()

    # Enter an infinite loop.
    while True:

        # Get the image identification numbers.
        reads = read_process()

        # Iterate over the image identification numbers.
        for i in reads:

            # Execute the corresponding function.
            if reads[i] == 6:  # 6 numaral
                controller_close()
                exit(0)
            elif reads[i] > 0 and reads[i] <= 10:
                print(f"lem {reads[i]} al.")
            else:
                print(f"Geenek ({reads[i]}) girdiniz. Ler girin.")

if __name__ == "__main__":
    main()
