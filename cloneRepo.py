import os
import subprocess

def functionComand(comando):
    return subprocess.check_output(comando , shell= True)

def cloneRepo():
    os.chdir(f"/home/daniel/projetos/daniel");

    repository = input("Nome do repositorio: ");

    comando = f'git clone {repository} '
    functionComand(comando)

    nome = repository.split("/")
    nome  = nome[-1].split(".")

    os.chdir(f"/home/daniel/projetos/daniel/{nome[0]}");


    arquivos=[]

    for nome_arquivos in os.listdir(f"/home/daniel/projetos/daniel/{nome[0]}"):
        if(nome_arquivos.endswith("js")):
            arquivos.append(nome_arquivos)    

    if(len(arquivos) != 0):
        comando = "npm i "
        functionComand(comando)
    
    

    functionComand("code .")
    
