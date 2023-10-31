cfg = {
        ###########  ROTATION ###########
        # Initialization configuration.
        # pitch_degree is the degree from which the pitch will be rotated down to.
        "pitch_degree": 13,
        ###########  ROTATION ###########
        # Rotations to right or left, clockwise or counter-clockwise in respectively.
        # rotate_degree controls the degree of the turn.
        # rotate_speed controls the speed in degrees of the turn.
        "rotate_degree": 90,
        "rotate_speed": 90,
        "yaw_speed": 120,

        ###########  MOVING ###########
        # Movement to forward, backward, left, right or fastforward.
        # "move_distance" in meters to control the distance.
        # "move_gain" will be added to move_distance to calculate final distance to be inputted to robot.
        # Change it to particularize for different surfaces.
        # "move_speed" controls the speed for forward, backward, left and right movements.
        # "move_fastspeed" controls the speed for fastforward.
        "move_distance": 0.75,
        "move_gain": 0.05,
        "move_speed": 1,
        "move_fastspeed": 1,

        ###########  DANCE ###########
        # Dance movement. Dance movement rotates chassis to right and left repeatedly in place.
        # The dance will start with an half of the specified degree to a side then will be followed by
        # full degree rotations back and forth. To finish at the center, a final half degree movement will
        # be made.
        # "dance_angle" specifies the full degree of the dance movement. The half degree wil be calculated not specified.
        # "dance_speed" is the speed in degrees in which all the rotation will be made.
        # "dance_iter" is the number of full degree iterations.
        "dance_angle": 90,
        "dance_speed": 120,
        "dance_iter": 4,
        }

