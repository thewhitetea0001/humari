import colorama
import datetime
from datetime import datetime
from colorama import Fore, Style, init

init()

class Log:
    @staticmethod
    def info(text):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} {Fore.GREEN}info{Style.RESET_ALL} | {text}")

    @staticmethod
    def warn(text):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} {Fore.YELLOW}warn{Style.RESET_ALL} | {text}")
    
    @staticmethod
    def error(text, e = None):
        if e != None:
            text = f"{text}: {e}"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} {Fore.RED}erro{Style.RESET_ALL} | {text}")
