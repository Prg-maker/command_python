from pyfiglet import Figlet
from termcolor import colored
from cloneRepo import cloneRepo
from createNewProjectReactTs import creteNewProjecteReact

def print_colored_ascii(text, color='white', font='slant'):
    fig = Figlet(font=font)
    colored_text = colored(fig.renderText(text), color)
    print(colored_text)

texto_para_imprimir = "COOM"
cor_do_texto = 'cyan'
fonte_do_texto = 'isometric1'  

print_colored_ascii(texto_para_imprimir, cor_do_texto, fonte_do_texto)

print("(1) Clonar um repo")
print("(2) Criar um projeto em ReactJs")


opt = int(input("Escolha: ")) 

    
def SwicthCase():
    if opt == 1:
        cloneRepo();
    elif opt == 2:
        creteNewProjecteReact();
    elif opt == 3:
        pass
SwicthCase()