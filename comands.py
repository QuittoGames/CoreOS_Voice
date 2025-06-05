from dataclasses import dataclass
from modules.DeviceCommand import DeviceCommand
from data import data

@dataclass
class Commands:
    commands: list = []


    def __post_init__(self):
        self.commands = [
            DeviceCommand(
                name="QuittoPC_start",
                root_command=False,
                Device=data.Devices,
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
                root_command=True,
            )
        ]