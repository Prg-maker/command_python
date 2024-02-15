from  ..utils.comand import Comand
import os

class CreateNewProjectReact():
    def create(self):

        functionComand = Comand()
        os.chdir("/home/daniel/projetos/daniel");
        nome = input("Nome da aplicaçao: ")
        
        functionComand.comandInTerminal(f"npm create vite@latest {nome} -- --template react-ts")

        os.chdir(f"/home/daniel/projetos/daniel/{nome}");
        functionComand.comandInTerminal("npm i ")

        
        functionComand.comandInTerminal("git init")
        functionComand.comandInTerminal("git add .")
        functionComand.comandInTerminal("git commit -m 'fist commit' ")
        functionComand.comandInTerminal("code .")
        print(f"[bold green]Projeto criado: {nome}.[/bold green]")