from  ..utils.comand import Comand
import os
class CloneRepo:
    def __init__(self, repo:str):
        self.repo = repo
    
    def clone(self):

        functionComand = Comand()

        os.chdir(f"/home/daniel/projetos/daniel");

        repository = input("Nome do repositorio: ");

        functionComand.comandInTerminal(f'git clone {repository} '  )

        nome = repository.split("/")
        nome  = nome[-1].split(".")

        os.chdir(f"/home/daniel/projetos/daniel/{nome[0]}");


        arquivos=[]

        for nome_arquivos in os.listdir(f"/home/daniel/projetos/daniel/{nome[0]}"):
            if(nome_arquivos.endswith("js")):
                arquivos.append(nome_arquivos)    

        if(len(arquivos) != 0):
            functionComand.comandInTerminal("npm i ")        
        

        functionComand.comandInTerminal("code .")
        