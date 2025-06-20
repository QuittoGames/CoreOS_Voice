import os
import platform
from dataclasses import dataclass
import subprocess
import sys
from data import data
import uuid

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    async def verify_modules():
        try:
            # #Uso Do modules por txt
            req_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "requirements", "requirements.txt"))
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_path], check=True)
        except Exception as E:
            print(f"Erro Na Verificaçao De Modulos, Erro: {E}")
            return
        
    async def add_path_modules(data_local:data):
        if data.modules_local == None:return
        try:
            for i in data.modules_local:
                sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), i)))
                if data_local.Debug:print(f"Module_local: {i}")
            return
        except Exception as E:
            print(f"Erro Al Adicionar Os Caminhos Brutos, Erro: {E}")
            return
    
    def get_mac() -> str:
        mac_num = uuid.getnode()
        mac = ':'.join(f'{(mac_num >> ele) & 0xff:02x}' for ele in range(40, -1, -8))
        return mac
    
    def byteMAC(MAC:str):
        return bytes.fromhex(MAC.replace(":", ""))
    
    def wake_on_lan(MAC_adress:str):
        pass