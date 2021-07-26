import os
import subprocess
from colorama import init,Fore,Back

#color and banner
init()
red = Fore.RED
black = Back.BLACK
cyan = Fore.CYAN
green = Fore.GREEN
reset = Back.RESET

def banner():
    print(f'{red}')
    banner = os.system("figlet -f slant 'PanDar Py'")    
    print(banner)
#command function
def cm(command):
    cm = os.system(command)

def start():
    try:
        banner()
        print("Starting Process")
        cm('sleep 5')
        cm('cd .server')
        cm('unzip python')
        print(f'{cyan}='*10+ "unzipping ")
        print("starting server ")
        print(f"{red}=="*20)
        print("Link >> localhost:8080/www.pythonforbeginners.com/index.html")
        print("Enter the link in your browser !")
        print(f'{red}=='*20)
        cm('php -S localhost:8080')
    except Exception as e:
        print(f'{black}{red}=='*20+ '+')
        print("something is wrong !")
start()
