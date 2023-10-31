from enum import Enum, auto

class Actions(Enum):
    GO_FORWARD      = auto()
    GO_FASTFORWARD  = auto()
    GO_BACKWARD     = auto()
    GO_RIGHT        = auto()
    GO_LEFT         = auto()
    ROTATE_RIGHT    = auto()
    ROTATE_LEFT     = auto()
    DANCE           = auto()
    MUSIC           = auto()
    FIRE            = auto()

    FN_TAG          = auto()
    FN_CALL         = auto()

    REPEAT_TWO      = auto()
    REPEAT_THREE    = auto()


class Game():
    ## A function is a set of actions
    game_function = list()

    def __init__(self, action_list):
        self.action_list = action_list

    def __process_function_def(self):
        ### Get the function definition and remove the block from the list
        if Actions.FN_TAG not in self.action_list:
            return self.action_list
        elif self.action_list.count(Actions.FN_TAG) == 2:
            fn_tags = [i for i, n in enumerate(self.action_list) if n == Actions.FN_TAG]
            self.game_function = self.action_list[fn_tags[0]+1:fn_tags[1]]
        else:
                raise GameLogicError("Function tags don't match!")

        action_list_after_fn = self.action_list.copy()
        for i in range(fn_tags[0],fn_tags[1]+1):
            action_list_after_fn[i] = None
        return action_list_after_fn

    def __process_repeat_actions(self, sub_action_list):
        action_list_after_reps = list()
        for i, a in enumerate(sub_action_list):
            if a is not None and a is not Actions.REPEAT_TWO and a is not Actions.REPEAT_THREE:
                action_list_after_reps.append(a)
            elif a is Actions.REPEAT_TWO or a is Actions.REPEAT_THREE:
                if i != len(sub_action_list)-1:
                    if sub_action_list[i+1] is not Actions.REPEAT_TWO and sub_action_list[i+1] is not Actions.REPEAT_THREE:
                        # Add the extras because the actions will be added once anyway
                        if a is Actions.REPEAT_TWO:
                            for _ in range(1):
                                action_list_after_reps.append(sub_action_list[i+1])
                        elif a is Actions.REPEAT_THREE:
                            for _ in range(2):
                                action_list_after_reps.append(sub_action_list[i+1])
                else:
                    raise GameLogicError("X2 and X3 should be followed by another card.")
        # print(action_list_after_reps)
        return action_list_after_reps

    def __process_function_calls(self, sub_action_list):
        action_list_after_fcall = list()
        for i, a in enumerate(sub_action_list):
            if a is not None and a is not Actions.FN_CALL:
                action_list_after_fcall.append(a)
            elif a is Actions.FN_CALL:
                if self.game_function:
                    action_list_after_fcall.extend(self.game_function)
                else:
                    raise GameLogicError("Function call without definition.")
        return action_list_after_fcall

    def get_action_queue(self):
        """ Process the actions and form an action queue

        Returns the calculated action queue
        """

        try:
            action_list_after_fn = self.__process_function_def()

            ### Resolve the X2's and X3's before function substitution
            action_list_after_reps = self.__process_repeat_actions(action_list_after_fn)

            ### Resolve function calls
            action_list_after_fcall = self.__process_function_calls(action_list_after_reps)

            ### Resolve the X2's and X3's after function substitution
            action_list_after_reps = self.__process_repeat_actions(action_list_after_fcall)
            return action_list_after_reps
        except GameLogicError as err:
            raise err



class GameLogicError(Exception):
    def __init__(self, message="Logic error in the game."):
        self.message = message
