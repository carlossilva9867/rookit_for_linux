
# Rootkit 
Este projeto destina-se a fins educacionais e de pesquisa em segurança cibernética, com o objetivo de aumentar a compreensão dos administradores de sistemas sobre as técnicas empregadas por rootkits e as medidas de defesa necessárias para proteger sistemas contra essas ameaças.



Cenario de um ataque

![Rootkit Logo](https://github.com/carlossilva9867/rookit_for_linux/blob/master/img/example_rootkit_attack.png?raw=true)

  

## Descrição
Rootkit é uma ferramenta utilizada por cibercriminosos para ocultar atividades maliciosas em sistemas comprometidos, dificultando sua detecção por parte dos administradores de sistemas e das soluções de segurança tradicionais.

Este projeto visa implementar a simulação dos comportamentos utilizados por rootkits em sistemas operacionais Linux, incluindo:

- **Shell reverso para controle remoto**: Implementação de um mecanismo que permite aos administradores acessar remotamente o sistema alvo, possibilitando a execução de comandos e operações de gerenciamento.

- **Elevação de privilégios**: Desenvolvimento de técnicas que permitem ao rootkit obter privilégios de administração ou acesso privilegiado ao sistema, mesmo sem as devidas credenciais.

- **Ocultação de processos no sistema**: Implementação de métodos para ocultar processos relacionados ao rootkit, tornando-os invisíveis aos comandos convencionais de listagem de processos, dificultando a detecção e remoção.

- **Comportamento persistente através do uso do cron e systemd**: Desenvolvimento de estratégias que garantem que o rootkit seja executado de forma persistente no sistema, mesmo após reinicializações, utilizando agendamento de tarefas com o cron ou integração com o sistema de inicialização systemd.



---

## Detecção

Para detectar comportamentos no sistema operacional, podemos utilizar ferramentas nativas como:

### Audit

O Auditd é um sistema de auditoria no sistema operacional Linux que permite a criação de novas regras para identificar comportamentos maliciosos ou não, gerando um log de registro quando determinada ação é realizada por um usuário ou programa.

referências: https://linux.die.net/man/8/auditd
### chkrootkit

O chkrootkit é uma ferramenta de linha de comando projetada para verificar sistemas Linux em busca de sinais de uma possível invasão por rootkits, que são programas maliciosos projetados para esconder a presença de intrusos no sistema.
referências: https://www.unix.com/man-page/linux/1/chkrootkit/

### rkhunter

O rkhunter (Rootkit Hunter) é uma ferramenta de detecção de rootkits que verifica o sistema em busca de sinais de comprometimento por malware. Ele examina arquivos, processos e configurações do sistema em busca de alterações suspeitas que possam indicar a presença de um rootkit ou outras ameaças.
referências: https://rkhunter.sourceforge.net/

  
---
### Funções do rookit
O programa foi desenvolvido em Python e compilado em formato **ELF** para permitir a execução de um único arquivo, simulando um programa legítimo como o Notepad

| Função                 | Descrição                                                                                                                                                                   |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| check_root             | Verifica se o script está sendo executado com privilégios de root.                                                                                                         |
| rootkit_main           | Função principal que invoca as funcionalidades do rootkit, incluindo escalonamento de privilégios, shell reverso e persistência.                                          |
| rootkit_init           | Inicia o rootkit em segundo plano, garantindo que as funcionalidades sejam executadas de forma discreta.                                                                   |
| elevar_privilegio      | Função que implementa o escalonamento de privilégios, permitindo que o rootkit execute determinadas operações com privilégios elevados.                                    |
| remote_shell           | Implementação de um shell reverso para controle remoto do sistema, possibilitando que um atacante assuma o controle do sistema de forma remota.                            |
| get_persistence        | Implementa mecanismos de persistência, garantindo que o rootkit seja executado automaticamente após reinicializações do sistema, aumentando a furtividade do ataque.       |
| rootkit                | Script principal do rootkit, que reúne todas as funcionalidades e as inicia em segundo plano para operação contínua.                                                       |



## Contribuindo

Contribuições são bem-vindas! 



### 
A shell reversa foi inspirada no projeto.
- https://github.com/mhaskar/Linux-Root-Kit/blob/master/R00TKIT.py
