#!/usr/bin/python
# -*- coding: utf-8 -*-
import os 
# Remove rootkit 
def user_settings():
    print("Removendo o usuario admin")
    os.system(f"userdel -r admin")
    os.system(f"sed -i '/^admin[[:space:]]*ALL=(ALL:ALL)[[:space:]]*NOPASSWD:ALL/d' /etc/sudoers")

def disable_services():
    print("Removendo desabilitando o serviço notepad.service")
    os.system(f"systemctl stop notepad")
    os.system(f"systemctl disable notepad")

def remove_binary():
    print("Removendo o binario /usr/bin/notepad")
    os.system(f"rm -rf /usr/bin/notepad")
    
def main():
    user_settings()
    disable_services()
    remove_binary()

main()    