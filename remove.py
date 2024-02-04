import os
def remove():
    os.system('rm -rf /bin/pyshell.py')
    os.system('rm -rf /bin/colors.py')
    os.chdir('cd ..')
    os.system('rm -rf pyshell')
remove()