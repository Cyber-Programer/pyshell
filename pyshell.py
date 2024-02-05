#!/usr/bin/env python3


# Shell Code

import sys
import os
from colors import color
import subprocess

# pwd = os.getcwd()

system_username = subprocess.getoutput(['whoami'])
host_name = subprocess.getoutput(['hostname'])

def mainShell():
    while True:
        usr = input(f'{color.red}┌─[{color.reset}{color.yellow}{system_username}{color.reset}@{color.cyan}{host_name}{color.reset}{color.red}]─[{color.reset}{color.green}{os.getcwd()}{color.reset}{color.red}]{color.reset}{color.reset}\n{color.red}└──╼ {color.reset}$ ')
        if any(keyword in usr.lower() for keyword in ['exit','close']):
            break
    
         
        if usr.startswith('cd'):
            new_directory = usr[3:].strip()
            # print(new_directory)
            
            try:
                os.chdir(new_directory)
                # print(f"Changed directory to: {os.getcwd()}")
            except FileNotFoundError:
                print(color.red+f"Directory not found: {new_directory}"+color.reset)
        else:
            os.system(usr)
            print() 

if __name__ == '__main__':
    mainShell()
