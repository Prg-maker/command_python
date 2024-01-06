# Comand

- [ x ] 

```py
import subprocess
import os


def functionComand(comando):
    return subprocess.check_output(comando , shell= True)


print("Nome do repositorio: ");
repository = input();

comando = f'git clone {repository} '
saida = functionComand(comando)

nome = repository.split("/")


os.chdir(f"/home/daniel/projetos/command/{nome[-1]}");

comando = "npm i"

saida = functionComand(comando)

```