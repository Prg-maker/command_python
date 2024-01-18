import subprocess
import os
from pyfiglet import Figlet
from termcolor import colored

def print_colored_ascii(text, color='white', font='slant'):
    fig = Figlet(font=font)
    colored_text = colored(fig.renderText(text), color)
    print(colored_text)

texto_para_imprimir = "COOM"
cor_do_texto = 'cyan'
fonte_do_texto = 'isometric1'  

print_colored_ascii(texto_para_imprimir, cor_do_texto, fonte_do_texto)

print("(1) Clonar um repo")
print("(2) Criar um projeto em ReactJs")
print("(3) Criar um projeto em NextJs")
opt = int(input("Escolha: ")) 



def functionComand(comando):
    return subprocess.check_output(comando , shell= True)

def cloneRepo():
    print("Nome do repositorio: ");
    repository = input();

    comando = f'git clone {repository} '
    saida = functionComand(comando)

    nome = repository.split("/")


    nome  = nome[-1].split(".")

    os.chdir(f"/home/daniel/projetos/command/{nome[0]}");


    arquivos=[]

    for nome_arquivos in os.listdir(f"/home/daniel/projetos/command/{nome[0]}"):
        if(nome_arquivos.endswith("js")):
            arquivos.append(nome_arquivos)    

    if(len(arquivos) != 0):
        comando = "npm i "
        saida = functionComand(comando)

