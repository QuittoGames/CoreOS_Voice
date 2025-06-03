from dataclasses import dataclass
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))
from Comand import Comand
from Device import Device
from typing import Callable


@dataclass
class DeviceCommand(Comand):
    Device: Device
    voice_mesage: list
    event: Callable

    def start(self):
        pass

    def __init_subclass__(cls):
        return super().__init_subclass__()