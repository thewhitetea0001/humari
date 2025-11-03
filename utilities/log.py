import colorama
import datetime
from datetime import datetime
from colorama import Fore, Style, init

init()

class Log:
    @staticmethod
    def log(file_name, text):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} LOG   | [{file_name}] {text}")

    @staticmethod
    def info(task, name, text):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} {Fore.GREEN}INFO{Style.RESET_ALL}  | [{task.upper()}:{name}] {text}") # command or event, name, text

    @staticmethod
    def warn(task, name, text):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} {Fore.YELLOW}WARN{Style.RESET_ALL}  | [{task.upper()}:{name}] {text}")
    
    @staticmethod
    def error(task, name, text):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} {Fore.RED}ERROR{Style.RESET_ALL} | [{task.upper()}:{name}] {text}")