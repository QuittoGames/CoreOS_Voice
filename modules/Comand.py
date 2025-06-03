from dataclasses import dataclass

@dataclass
class Comand:
    name: str
    root_command:bool
    
    def __str__(self) -> str:
        return f"Name: {self.name} \n root_command: {self.root_command}"