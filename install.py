import os
import time as t
from time import sleep as s
from pathlib import Path

home = str(Path.home()) + "/"

def c():
    os.system("clear")

c()

print("Wealcome to the CMI 'Command Installer' setup.")

t.sleep(2)

print('\nSettings up everything for you...')

t.sleep(2)

print("\nInstalling dependencies...")

print("""\n\n
         ----  Avaible Distros ----

       1 =  Arch Linux 

       2 = Debian & Debian Based

       3 = Other Distro YOU NEED TO HAVE BASH INSTALLED

       4 = Termux

       5 = Exit Installer

       """)

so = (int(input("Select your Linux distro\n> ")))

if so == 1:
    os.system("sudo pacman -Syu bash")
if so == 2:
    os.system("sudo apt-get install bash")
if so == 3:
    pass
if so == 4:
    os.system("pkg install bash")
if so == 5:
    print("Exiting CMI Setup...")
    time.sleep(2)
    exit()
if not (so == 1 or so == 2 or so == 3 or so == 4 or so == 5):
    print("-- ERROR: You need to chose a number, only 1 - 5")
    exit()

e = True

destFile = home + r".bashrc"

fil = home + ".cmi/.cmi.py"
exi = os.path.isdir(home + '.cmi')
if exi == False:
    os.system("mkdir " + home + ".cmi")

if e:
    os.system(f"mv .cmi.py {home}.cmi/")
    with open(destFile, 'a') as f:
        f.write("#cmis\n")
        f.write(f'alias cmi="python3 {fil}"\n')
        f.write('#cmif\n')

os.system("source $HOME/.bashrc")

print("Cmi Got installed, only type cmi to create a new command")
