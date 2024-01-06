# Comand
 ### Em Progresso
![](https://media.giphy.com/media/FaAxdPWZ7HKGmlnku7/giphy.gif)

| Tarefa            | Concluída |
|-------------------|-----------|
| Clonar um repositório     | [x]       |
| Rodar o comando <code> npm i</code> | [x]       |
| Rodar o comando <code> npm i</code> | [x]       |


___


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


