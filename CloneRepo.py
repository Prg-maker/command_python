from pyfiglet import Figlet
from termcolor import colored
from cloneRepo import cloneRepo
from createNewProjectReactTs import creteNewProjecteReact

from src.clone_repo.clone_repo_main import CloneRepoMain

cloneRepo = CloneRepoMain()

texto_para_imprimir = "COOM"
cor_do_texto = 'cyan'
fonte_do_texto = 'isometric1'  

cloneRepo.printColoredAscii(color=cor_do_texto, font=fonte_do_texto, text=texto_para_imprimir)

def print_colored_ascii(text, color='white', font='slant'):
    fig = Figlet(font=font)
    colored_text = colored(fig.renderText(text), color)
    print(colored_text)

texto_para_imprimir = "COOM"
cor_do_texto = 'cyan'
fonte_do_texto = 'isometric1'  

print_colored_ascii(texto_para_imprimir, cor_do_texto, fonte_do_texto)



opt = int(input("Escolha: ")) 

    
def SwicthCase():
    if opt == 1:
        cloneRepo();
    elif opt == 2:
        creteNewProjecteReact();
    elif opt == 3:
        pass
SwicthCase()