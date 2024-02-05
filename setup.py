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
    x = os.uname().sysname.lower()

    os.system('chmod +x pyshell.py')

    if x == 'termux':
        print('Setup for Termux!')
        try:
            shutil.copy('pyshell.py', '/data/data/com.termux/files/usr/bin/')
            shutil.copy('colors.py', '/data/data/com.termux/files/usr/bin/')
        except Exception as e:
            print(e)
    elif x == 'linux':
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
