import os 
import subprocess

def functionComand(comando):
    return subprocess.check_output(comando , shell= True)


def creteNewProjecteReact():

    nome = input("Nome da aplicaçao: ")
    
    comando = f"npm create vite@latest {nome} -- --template react-ts"
    functionComand(comando)

    os.chdir(f"/home/daniel/projetos/command/{nome}");
    comando = "npm i "
    functionComand(comando)