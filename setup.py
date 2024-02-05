import subprocess
import os
import shutil
from pathlib import Path

# system_username = subprocess.getoutput(['whoami'])

def install():
    x = os.uname().sysname.lower()

    os.system('mv pyshell.py pyshell')  # Use os.rename for renaming files
    os.system('chmod +x pyshell')
    
    if x == 'linux':
        print('Setup for Linux!')
        try:
            if os.geteuid() != 0:
                print("Please run with sudo!")
                return
            os.system('cp pyshell /bin')  # Move to /bin with sudo
        
        except Exception as e:
            print(e)
            
    elif x == 'termux':
        print("Setup for Termux")
        
        # if os.geteuid() != 0:
        #     print("Please run with sudo!")
        #     return

        try:
            shutil.copy('pyshell', '/data/data/com.termux/files/usr/bin')  # Move to Termux bin directory
        except Exception as e:
            print(e)

    print('\nJust type pyshell to start your terminal\n')

if __name__ == '__main__':
    install()
