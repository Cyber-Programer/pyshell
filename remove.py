import os

def remove():
    system_type = os.uname().sysname.lower()

    if system_type == 'linux':
        os.system('rm -rf /usr/bin/pyshell.py')
        os.system('rm -rf /usr/bin/colors.py')
    elif system_type == 'termux':
        os.system('rm -rf /data/data/com.termux/files/usr/bin/pyshell.py')
        os.system('rm -rf /data/data/com.termux/files/usr/bin/colors.py')
    else:
        print(f"Unsupported system: {system_type}")
        return

    os.chdir('..')
    os.system('rm -rf pyshell')

remove()
