import os 
import subprocess
from rich import  print
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
    print(f"[bold green]Projeto criado: {nome}.[/bold green]")
   

