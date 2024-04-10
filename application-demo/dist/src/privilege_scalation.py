#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess

def elevar_privilegio():
    if os.name != 'posix':
        print("Este recurso é suportado apenas em sistemas Unix.")
        return

    try:
        # Eleva os privilégios executando o comando 'sudo true' em um subprocesso
        subprocess.check_call(['sudo', 'true'])
        print("INFO - ELEVANDO PRIVILEGIOS")
        print("Privilégios elevados com sucesso!")
    except subprocess.CalledProcessError:
        print("Não foi possível elevar os privilégios.")
