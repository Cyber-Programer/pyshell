import os

def remove():
    system_type = os.uname().sysname.lower()

    if system_type == 'linux':
        if os.geteuid() != 0:
                print("Please run with sudo!")
                return
        os.system('rm -rf /bin/pyshell')

    elif system_type == 'termux':
        os.system('rm -rf /data/data/com.termux/files/usr/bin/pyshell')
    else:
        print(f"Unsupported system: {system_type}")
        return

    os.chdir('..')
    os.system('rm -rf pyshell')

remove()
