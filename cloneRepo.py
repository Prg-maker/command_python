import os
import subprocess

def functionComand(comando):
    return subprocess.check_output(comando , shell= True)

def cloneRepo():
    repository = input("Nome do repositorio: ");

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