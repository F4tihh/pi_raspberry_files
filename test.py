# -*- coding: utf-8 -*-
from controller import *
from time import sleep, time

def read_process():
    # Read the image identification numbers from the `resim_id_listesi` list and return them as a dictionary.

    resim_id_listesi = [1, 2, 3, 4, 5]

    # The `resim_id_listesi` list contains the image identification numbers.

    operations = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
    }

    # The `operations` dictionary contains the functions that will be executed for each image identification number.

    try:
        reads = dict()
        for i in range(5):
            resim_id = resim_id_listesi[i]
            reads[i] = resim_id

            # Wait for the function to complete.
            if resim_id in operations:
                sleep(int(operations[resim_id]))
            else:   
                print("Geersiz resim_id:", resim_id) 

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
            if reads[i] == "1":
                controller_forward()
            elif reads[i] == "2":
                controller_right()
            elif reads[i] == "3":
                controller_backward()
            elif reads[i] == "4":
                controller_left()
            elif reads[i] == "5":
                # Print the reads dictionary.
                print("reads:", reads)
            elif reads[i] == "6":
                # Close the controller.
                controller_close()
                exit(0)
            else:
                # Print an error message.
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
