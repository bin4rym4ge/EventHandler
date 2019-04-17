

class EventHandler(object):
    def __init__(self):
        self.Flag = {
        "init": 0,
        "KEY_A": 0,
        "KEY_B": 0,
        "KEY_C": 0,
        "KEY_D": 0,
        "KEY_E": 0,
        "KEY_F": 0,
        "KEY_G": 0,
        "KEY_H": 0,
        "KEY_I": 0,
        "KEY_J": 0,
        "KEY_K": 0,
        "KEY_L": 0,
        "KEY_M": 0,
        "KEY_N": 0,
        "KEY_O": 0,
        "KEY_P": 0,
        "KEY_Q": 0,
        "KEY_R": 0,
        "KEY_S": 0,
        "KEY_T": 0,
        "KEY_U": 0,
        "KEY_V": 0,
        "KEY_W": 0,
        "KEY_X": 0,
        "KEY_Y": 0,
        "KEY_Z": 0,
        "KEY_SPACE": 0,
        "KEY_ENTER": 0
        }

        self.Flag["init"] = 1
    def keyhandle(self):
        rawinput()
