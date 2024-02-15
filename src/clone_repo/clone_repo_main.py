from pyfiglet import Figlet
from termcolor import colored


class CloneRepoMain:
    def printColoredAscii(self, color , text , font):
        fig = Figlet(font=font)
        colored_text = colored(fig.renderText(text), color)
        print(colored_text)


