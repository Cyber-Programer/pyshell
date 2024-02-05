import subprocess
import os
import shutil

def ck_lolcat_installation():
    try:
        output = subprocess.check_output(['lolcat', '--version'])
        return True
    except FileNotFoundError:
        print('[ Need to install ] Lolcat')
        return False
    except subprocess.CalledProcessError:
        return False

def install():
    print('Which is your system?\n[1] Termux\n[2] Linux')
    x = int(input('=>'))

    os.system('chmod +x pyshell.py')

    if x == 1:
        print('Setup for Termux!')
        try:
            shutil.copy('pyshell.py', '/data/data/com.termux/files/usr/bin/')
            shutil.copy('colors.py', '/data/data/com.termux/files/usr/bin/')
        except Exception as e:
            print(e)
    elif x == 2:
        print("Setup for Linux (run with sudo user)")
        print()
        try:
            shutil.copy('pyshell.py', '/usr/bin/')
            shutil.copy('colors.py', '/usr/bin/')
        except Exception as e:
            print(e)

    print('\nJust type ./pyshell.py to start your terminal\n')

if ck_lolcat_installation():
    print('[ok] lolcat')
    install()
else:
    os.system('apt-get install lolcat')
    install()
