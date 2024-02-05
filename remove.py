import os

def remove():
    system_type = os.environ


    if 'termux' in system_type:
        os.system('rm -rf /data/data/com.termux/files/usr/bin/pyshell')
    
    else:
        if os.geteuid() != 0:
                print("Please run with sudo!")
                return
        os.system('rm -rf /bin/pyshell')
        
    os.chdir('..')
    os.system('rm -rf pyshell')

remove()
