#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from os import path
from colorama import init, Fore, Style

# LIB
sys.path.append('./src/')
from rookit import check_root, main, elevar_privilegio

def editor_de_texto():
    init(autoreset=True)

    def boas_vindas():
        print(Fore.CYAN + "Bem-vindo ao Editor de Texto 📝\n")
        print(Fore.CYAN + "Criado por GPT com auxílio de Carlos Silva\n")

    def criar_arquivo(file_path):
        if path.exists(file_path):
            print(Fore.YELLOW + "\n\tArquivo já existe!")
            ans = input(Fore.YELLOW + "\nDeseja utilizar este arquivo? (s/n)\n-> ")

            if ans.lower() != 's':
                return False

        else:
            print(Fore.YELLOW + "\n\tCriando novo arquivo...\n")

        with open(file_path, "a") as file:
            pass

        return True

    def apagar_conteudo(file):
        ans = input(Fore.YELLOW + "\nDeseja apagar todo o conteúdo? (s/n)\n-> ")
        if ans.lower() == 's':
            print(Fore.YELLOW + "\n\tApagando...\n")
            file.seek(0)
            file.truncate()

    def escrever_arquivo(file_path):
        print(Fore.GREEN + "\nPressione ENTER para começar uma nova linha.")
        print(Fore.GREEN + "Pressione Ctrl + C para salvar e fechar.\n")

        line_count = 1

        try:
            while True:
                line = input(Fore.MAGENTA + "\t" + str(line_count) + " ")
                with open(file_path, "a") as file:
                    file.write(line)
                    file.write('\n')
                line_count += 1
        except KeyboardInterrupt:
            print(Fore.RED + "\n\n\tFechando...")

    def abrir_arquivo():
        file_path = input(Fore.CYAN + "\nPor favor, insira o caminho para o arquivo: ")
        if not path.exists(file_path):
            print(Fore.RED + "\n\tArquivo não encontrado!")
            return

        print(Fore.GREEN + "\nArquivo encontrado!\n")
        with open(file_path, "r") as file:
            print(file.read())

    def menu():
        print(Fore.BLUE + "\nEscolha uma opção:")
        print("1. Criar ou abrir um arquivo")
        print("2. Escrever no arquivo")
        print("3. Visualizar o arquivo")
        print("4. Sair")

        opcao = input("-> ")

        if opcao == '1':
            file_path = input(Fore.CYAN + "\nPor favor, insira o caminho para o arquivo: ")
            if criar_arquivo(file_path):
                print(Fore.GREEN + "\nArquivo criado ou aberto com sucesso!\n")
            else:
                print(Fore.RED + "\nOperação cancelada.\n")
            menu()

        elif opcao == '2':
            file_path = input(Fore.CYAN + "\nPor favor, insira o caminho para o arquivo: ")
            if path.exists(file_path):
                with open(file_path, "a") as file:
                    apagar_conteudo(file)
                    escrever_arquivo(file_path)
            else:
                print(Fore.RED + "\n\tArquivo não encontrado!\n")
            menu()

        elif opcao == '3':
            abrir_arquivo()
            menu()

        elif opcao == '4':
            print(Fore.BLUE + "\nAté logo!")
            return

        else:
            print(Fore.RED + "\nOpção inválida, por favor, escolha novamente.\n")
            menu()

    boas_vindas()
    menu()

if check_root():
    #print("Você está como root!")
    editor_de_texto()
    
else:
    print("Você não está como root. Este script requer privilégios de root para executar o notepad.")
    elevar_privilegio()
    editor_de_texto()

