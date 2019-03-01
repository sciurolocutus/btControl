from enum import Enum


class ControlAction(Enum):
    RECONNECT = 'reconnect'
    START = 'start'
    STOP = 'stop'