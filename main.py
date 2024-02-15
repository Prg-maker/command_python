from src.clone_repo.clone_repo_main import CloneRepoMain

class Main:
    def start(self):
        cloneRepo = CloneRepoMain()
        texto_para_imprimir = "COOM"
        cor_do_texto = 'cyan'
        fonte_do_texto = 'isometric1'  
        cloneRepo.printColoredAscii(color=cor_do_texto, font=fonte_do_texto, text=texto_para_imprimir)

main = Main();
main.start()