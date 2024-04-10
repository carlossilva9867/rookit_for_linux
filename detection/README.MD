# Regras de Auditoria

Este arquivo contém regras de auditoria para monitorar atividades específicas.

## Configurações Gerais

- Limpar regras anteriores.
- Definir buffer de auditoria.
- Definir o modo de registro.

## Monitoramento de Usuários

- Monitorar criação de usuários em `/etc/passwd`.

## Monitoramento de Sudoers

- Monitorar alterações no arquivo `/etc/sudoers`.

## Monitoramento de Chaves SSH

- Monitorar manipulação de chaves SSH em diferentes diretórios de usuários.

## Monitoramento de Serviços Cron

- Monitorar criação de serviços cron nos diretórios relacionados ao cron.

## Monitoramento de Serviços Systemd

- Monitorar criação de serviços systemd no diretório `/etc/systemd/system/`.

## Monitoramento de Configurações de Rede

- Monitorar configurações de rede, incluindo mudanças no hostname, domainname e arquivos relacionados.

## Monitoramento de Módulos do Linux

- Monitorar módulos do Linux, como inserção e remoção de módulos.

