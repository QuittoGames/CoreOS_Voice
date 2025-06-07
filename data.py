from dataclasses import dataclass, field
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))
from modules.Comand import Comand
from modules.DeviceCommand import DeviceCommand
from modules.Device import Device
from tool import tool

@dataclass
class data:
    modules_local: list = field(default_factory=lambda: ["modules"])
    Debug: bool = True

    Devices: list = field(default_factory=lambda: [
        Device(id = 1 , name="QuittoPC", MAC_end="22:48:5c:06:0d:b1"),
        Device(id = 0, name="local_machine", MAC_end=tool.get_mac()),
    ])

    def getDevice(id: int):
        devices = sorted(data.Device, key=lambda d: d.id)
        low = 0
        high = len(devices) - 1

        while low <= high:
            mid = (low + high) // 2
            device = devices[mid]

            if device.id == id:
                return device
            elif device.id < id:
                low = mid + 1
            else:
                high = mid - 1

        return None

    
    def __str__(self) -> str:
        if not self.commands:
            return "Nenhum comando registrado."

        saida = "Comandos Registrados:\n"
        for i, cmd in enumerate(self.commands, 1):
            nome = getattr(cmd, "name", "Sem nome")
            desc = getattr(cmd, "descricao", "Sem descrição")
            saida += f"{i}. {nome} - {desc}\n"
        return saida
