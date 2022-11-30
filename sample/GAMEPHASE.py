from enum import Enum


class GAMEPHASE(Enum):
    Invocation = 1
    Pay = 2
    Pause = 3
    Attack = 4
    Choosing = 5
    FaceOff = 6