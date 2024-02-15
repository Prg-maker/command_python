import subprocess

class Comand():
    def comandInTerminal(self, comand):
        return subprocess.check_output(comand, shell=True)