import os
from pathlib import Path
import time
home = str(Path.home()) + "/"

# Variables

sl = input("Type the name of your command: ")


fl = input("Type the mame of your file: ")

ph = input("Type the path of your project, like this '/home/py/cmi/cmi.py/': ")

od = input("Type the command language of the command ex, python3: ")


destFile = home + r".bashrc"

os.system(f"mkdir " + home +".cmi/")

os.system("mv  " +fl+ " " +home+".cmi/")

dr = home + f"{fl}"

a = True
# cmdi
if a:
    with open(destFile, 'a') as f:
        f.write(f"#cmi {sl}\n")
        f.write(f'alias {sl}="{od} {dr}"\n')
        f.write(f"#cmif {sl}\n")
os.system("source " + home + " .bashrc")

print(f"Your new command is '{sl}' and is located in " + home + ".cmi/" + fl + "\n\n Thanks for using cmi 'command installer'\nDev: py#6650")
