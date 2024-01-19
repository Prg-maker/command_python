import os 
import subprocess

def functionComand(comando):
    return subprocess.check_output(comando , shell= True)


def creteNewProjecteReact():
   
    os.chdir("/home/daniel/projetos/daniel");
    nome = input("Nome da aplicaçao: ")
    
    comando = f"npm create vite@latest {nome} -- --template react-ts"
    functionComand(comando)

    os.chdir(f"/home/daniel/projetos/daniel/{nome}");
    comando = "npm i "
    functionComand(comando)

    functionComand("code .")
    print(f"Projeto criado {nome}.")
   

