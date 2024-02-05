import subprocess
import os
import shutil
from pathlib import Path



def install():
    x = os.uname().sysname.lower()

    os.rename('pyshell.py', 'pyshell')  # Use os.rename for renaming files
    os.system('chmod +x pyshell')

    if x == 'termux':
        print('Setup for Termux!')
        try:
            os.system(f'export PATH="$PATH:{str(Path.home())}/cyberprogramer"')
            shutil.copy('pyshell', f'{str(Path.home())}/cyberprogramer')
        except Exception as e:
            print(e)
    elif x == 'linux':
        print("Setup for Linux (run with sudo user)")
        if os.geteuid() != 0:
            print("Please run with sudo!")
            return

        try:
            os.system(f'export PATH="$PATH:{str(Path.home())}/cyberprogramer"')
            shutil.copy('pyshell', f'{str(Path.home())}/cyberprogramer')
        except Exception as e:
            print(e)

    print('\nJust type pyshell to start your terminal\n')

if __name__ == '__main__':
    install()