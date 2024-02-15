from pyfiglet import Figlet
from termcolor import colored
from ..create_projects.craete_new_project_reactJS_for_Ts import CreateNewProjectReact

class CloneRepoMain:
    def printColoredAscii(self, color , text , font):
        fig = Figlet(font=font)
        colored_text = colored(fig.renderText(text), color)
        print(colored_text)

        print("(1) Clonar um repo")
        print("(2) Criar um projeto em ReactJs com Typescript")

        option = int(input())
        react = CreateNewProjectReact()

        if option == 1:
            pass
        elif option == 2:
            react.create();


    


