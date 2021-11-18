import os

uin = input('have you already set up the .bash_aliases script under .bashrc? (y/n) ')
if uin == 'n':
    file = open('test.txt','a')
    file.write('\nif [ -e ~/.bash_aliases ]')
    file.write('\nthen')
    file.write('\n. ~/.bash_aliases')
    file.write('\nfi')

input('Are you sure you would like to install this command? press any key to continue, otherwise press ctrl+c')
print('running "sudo mkdir /usr/bin/warp-start"')
os.system('sudo mkdir /usr/bin/warp-start')
print('running "sudo mv warp-start.py /usr/bin/warp-start/warp-start.py"')
os.system('sudo mv warp-start.py /usr/bin/warp-start/warp-start.py')
print('running "chmod +x /usr/bin/warp-start/warp-start.py"')
os.system('chmod +x /usr/bin/warp-start/warp-start.py')
print('''running "echo "alias warp-start='/usr/bin/warp-start/warp-start.py'" >> ~/.bash_aliases"''')
os.system('''echo "alias warp-start='/usr/bin/warp-start/warp-start.py'" >> ~/.bash_aliases''')
print('Finished, use the command by typing "warp-start".')
exit()
