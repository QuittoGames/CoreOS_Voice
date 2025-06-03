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
    Devices: list = field(default_factory=lambda: [
        Device(name="QuittoPC", MAC_end="22:48:5c:06:0d:b1"),
        Device(name="local_machine", MAC_end=tool.get_mac()),
    ])

    commands: list = field(init=False)
    modules_local: list = field(default_factory=lambda: ["modules"])
    Debug: bool = True

    def __post_init__(self):
        self.commands = [
            DeviceCommand(
                name="QuittoPC_start",
                root_command=False,
                Device=self.Devices,
                voice_mesage=[
                    "Ligar PC", "Ligar QuittoPC", "Iniciar computador",
                    "Ligar meu computador", "Acordar PC", "Acordar QuittoPC",
                    "Ativar computador", "Despertar máquina", "Wake up PC",
                    "Start computer", "Ligar o desktop", "Ei, liga o PC",
                    "Iniciar sistema principal", "Ativar estação principal",
                    "Ligar Steup"
                ]
            ),
            DeviceCommand(
                name="QuittoPC_shutdown",
                root_command=True
            )
        ]

    def __str__(self) -> str:
        if not self.commands:
            return "Nenhum comando registrado."

        saida = "Comandos Registrados:\n"
        for i, cmd in enumerate(self.commands, 1):
            nome = getattr(cmd, "name", "Sem nome")
            desc = getattr(cmd, "descricao", "Sem descrição")
            saida += f"{i}. {nome} - {desc}\n"
        return saida
