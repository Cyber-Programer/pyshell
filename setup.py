import subprocess
import os

def ck_lolcat_installation():
    try:
        output = subprocess.check_output(['lolcat','--version'])
        return True
    except FileNotFoundError:
        print()
        print('[ Need to install ] Lolcat')
        print()
        return False
    except subprocess.CalledProcessError:
        return False

def install():
    os.system('chmod +x pyshell.py')  # Assuming it's pyshell.py, not pyshell.py
    os.system(' cp pyshell.py /bin/')
    os.system(' cp colors.py /bin/')
    print()
    print()
    print()
    print('Just type ./pyshell.py to start your terminal')
    print()
    print()
    

if ck_lolcat_installation():
    print('[ok] lolcat')
    install()
else:
    os.system('apt-get install lolcat')
    install()
