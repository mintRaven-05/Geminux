import sys
import time
import platform
import subprocess
from pathlib import Path
from os import path, environ

HOME = path.expanduser("~")
SHELL = environ.get('SHELL', '')[5:]
USER = HOME[6:]

try:
    ch = input("Do you want to uninstall Geminux ? [y/n] : ")
    if ch.upper() == "Y" or ch.upper() == "YES":
        if platform.architecture()[1] == "ELF":
            
            if Path(f"{HOME}/.config/Geminux").exists():
               print(f"removing {HOME}/.config/Geminux")
               subprocess.call(["rm", "-rf", f"{HOME}/.config/Geminux"])
               time.sleep(0.5)
            
            if SHELL == "zsh":
                print("removing alias and key binds from ~/.zshrc")
                with open(f"{HOME}/.zshrc", "r") as shell_file:
                    data = shell_file.readlines()
                    if "alias geminux='python ~/.Geminux/main.py'\n" in data:
                        data.pop(data.index("alias geminux='python ~/.Geminux/main.py'\n"))
                    
                    if "bindkey -s '^ ' 'geminux^M'" in data:
                        data.pop(data.index("bindkey -s '^ ' 'geminux^M'"))
                    
                    if "alias geminux='python ~/.Geminux/main.py'" in data:
                        data.pop(data.index("alias geminux='python ~/.Geminux/main.py'"))

                    if "bindkey -s '^ ' 'geminux^M'\n" in data:
                        data.pop(data.index("bindkey -s '^ ' 'geminux^M'\n"))

                    elif "alias geminux='python ~/.Geminux/main.py'\n" not in data:
                        print("could not find alias for geminux in ~/.zshrc")
                        print("seems like you modified the alias")
                        print("In that case you need to remove it manually")

                    elif "bindkey -s '^ ' 'geminux^M'\n" not in data:
                        print("could not find key bind for geminux in ~/.zshrc")
                        print("seems like you modified the key bind")
                        print("In that case you need to remove it manually")

                    shell_file.close()
                    with open(f"{HOME}/.zshrc", "w") as shell_file:
                        shell_file.writelines(data)
                        shell_file.close()
                            
            if SHELL == "bash":
                print("removing alias from ~/.bashrc")
                with open(f"{HOME}/.bashrc", "r") as shell_file:
                    data = shell_file.readlines()
                    if "alias geminux='python ~/.Geminux/main.py'\n" in data:
                        data.pop(data.index("alias geminux='python ~/.Geminux/main.py'\n"))

                    elif "alias geminux='python ~/.Geminux/main.py'\n" not in data:
                        print("could not find alias for geminux in ~/.bashrc")
                        print("seems like you modified the alias")
                        print("In that case you need to remove it manually")

                    shell_file.close()
                    with open(f"{HOME}/.bashrc", "w") as shell_file:
                        shell_file.writelines(data)
                        shell_file.close()
            if Path(f"{HOME}/.Geminux").exists():
               print(f"removing {HOME}/.Geminux")
               subprocess.call(["rm", "-rf", f"{HOME}/.Geminux"])
               time.sleep(0.5)
        print("Uninstallation completed !")
        print("Relode your terminal")
    elif ch.upper() == "N" or ch.upper() == "NO":
        print("quiting . . .")
        sys.exit(0)

except  Exception as e:
    print(print("\033[0;31m[ERROR]\033[0;37m Could not complete uninstallation : ", e))

