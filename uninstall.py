#MIT License

#Copyright (c) 2024 Debjeet Banerjee

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
#--------------------------------------------------------------------------------------------------------------------------------------
import sys
import time
import shutil
import platform
import subprocess
from pathlib import Path
from os import path, environ
#--------------------------------------------------------------------------------------------------------------------------------------
ansi = {
    "White" : "\033[0;37m",
    "Green" : "\033[0;32m",
    "Yellow" : "\033[0;33m",
    "Red" : "\033[1;31m",
    "Bold Green" : "\033[1;32m"
}
#--------------------------------------------------------------------------------------------------------------------------------------
HOME = path.expanduser("~")
SHELL = environ.get('SHELL', '')[5:]
USER = HOME[6:]
#--------------------------------------------------------------------------------------------------------------------------------------
try:
    #----------------------------------------------------------------------------------------------------------------------------------
    ch = input("Do you want to uninstall Geminux ? [y/n] : ")
    #----------------------------------------------------------------------------------------------------------------------------------
    if ch.upper() == "Y" or ch.upper() == "YES":
        #------------------------------------------------------------------------------------------------------------------------------
        if platform.architecture()[1] == "ELF":
            #--------------------------------------------------------------------------------------------------------------------------
            if Path(f"{HOME}/.config/Geminux").exists():
               print(f"{ansi["Bold Green"]}removing {HOME}/.config/Geminux{ansi["White"]}")
               subprocess.call(["rm", "-rf", f"{HOME}/.config/Geminux"])
               time.sleep(0.5)
            #--------------------------------------------------------------------------------------------------------------------------
            if "zsh" in SHELL:
                #----------------------------------------------------------------------------------------------------------------------
                print(f"{ansi["Bold Green"]}removing alias and key binds from ~/.zshrc{ansi["White"]}")
                #----------------------------------------------------------------------------------------------------------------------
                with open(f"{HOME}/.zshrc", "r") as shell_file:
                    data = shell_file.readlines()
                #----------------------------------------------------------------------------------------------------------------------
                    if "alias geminux='python ~/.Geminux/main.py'\n" in data:
                        data.pop(data.index("alias geminux='python ~/.Geminux/main.py'\n"))
                    #------------------------------------------------------------------------------------------------------------------
                    if "bindkey -s '^ ' 'geminux^M'" in data:
                        data.pop(data.index("bindkey -s '^ ' 'geminux^M'"))
                    #------------------------------------------------------------------------------------------------------------------
                    if "alias geminux='python ~/.Geminux/main.py'" in data:
                        data.pop(data.index("alias geminux='python ~/.Geminux/main.py'"))
                    #------------------------------------------------------------------------------------------------------------------
                    if "bindkey -s '^ ' 'geminux^M'\n" in data:
                        data.pop(data.index("bindkey -s '^ ' 'geminux^M'\n"))
                    #------------------------------------------------------------------------------------------------------------------
                    elif "alias geminux='python ~/.Geminux/main.py'\n" not in data:
                        print(f"{ansi["Yellow"]}could not find alias for geminux in ~/.zshrc")
                        print("seems like you modified the alias")
                        print(f"In that case you need to remove it manually{ansi["Yellow"]}")
                    #------------------------------------------------------------------------------------------------------------------
                    elif "bindkey -s '^ ' 'geminux^M'\n" not in data:
                        print(f"{ansi["Yellow"]}could not find key bind for geminux in ~/.zshrc")
                        print("seems like you modified the key bind")
                        print(f"In that case you need to remove it manually{ansi["White"]}")
                    #------------------------------------------------------------------------------------------------------------------
                    shell_file.close()
                    #------------------------------------------------------------------------------------------------------------------
                    with open(f"{HOME}/.zshrc", "w") as shell_file:
                        shell_file.writelines(data)
                        shell_file.close()
                    #------------------------------------------------------------------------------------------------------------------
            if "bash" in SHELL:
                #----------------------------------------------------------------------------------------------------------------------
                print(f"{ansi["Bold Green"]}removing alias from ~/.bashrc{ansi["White"]}")
                #----------------------------------------------------------------------------------------------------------------------
                with open(f"{HOME}/.bashrc", "r") as shell_file:
                    data = shell_file.readlines()
                    if "alias geminux='python ~/.Geminux/main.py'\n" in data:
                        data.pop(data.index("alias geminux='python ~/.Geminux/main.py'\n"))
                #----------------------------------------------------------------------------------------------------------------------
                    elif "alias geminux='python ~/.Geminux/main.py'\n" not in data:
                        print(f"{ansi["Yellow"]}could not find alias for geminux in ~/.bashrc")
                        print("seems like you modified the alias")
                        print(f"In that case you need to remove it manually{ansi["White"]}")
                #----------------------------------------------------------------------------------------------------------------------
                    shell_file.close()
                #----------------------------------------------------------------------------------------------------------------------
                    with open(f"{HOME}/.bashrc", "w") as shell_file:
                        shell_file.writelines(data)
                        shell_file.close()
                #----------------------------------------------------------------------------------------------------------------------
            #--------------------------------------------------------------------------------------------------------------------------
            if Path(f"{HOME}/.Geminux").exists():
               print(f"{ansi["Bold Green"]}removing {HOME}/.Geminux")
               subprocess.call(["rm", "-rf", f"{HOME}/.Geminux"])
               time.sleep(0.5)
               #----------------------------------------------------------------------------------------------------------------------
               print("Uninstallation completed !")
               print("Relode your terminal")
               print("Thank you for trying Geminux")
               print(f"visit www.github.com/mintRaven-05 for more projects{ansi["White"]}")
               #----------------------------------------------------------------------------------------------------------------------
        elif platform.architecture()[1] == "WindowsPE":
            if Path(f"{HOME}\\.config\\Geminux").exists():
               print(f"{ansi["Bold Green"]}removing {HOME}\\.config")
               shutil.rmtree(f"{HOME}\\.config")
               time.sleep(0.5)
            #------------------------------------------------------------------------------------------------------------------------
            if Path(f"{HOME}\\.Geminux").exists():
                print(f"removing {HOME}\\.Geminux")
                shutil.rmtree(f"{HOME}\\.Geminux")
                time.sleep(0.5)
            #------------------------------------------------------------------------------------------------------------------------
            time.sleep(1)
            #------------------------------------------------------------------------------------------------------------------------
            print("uninstallation completed")
            print("Thank you for trying Geminux")
            print("remove all functions for Geminux from powershell PROFILE, if added any")
            print(f"visit https://www.github.com/mintRaven-05 for more projects{ansi["White"]}")
            #------------------------------------------------------------------------------------------------------------------------
    elif ch.upper() == "N" or ch.upper() == "NO":
        print("quiting . . .")
        sys.exit(0)
#------------------------------------------------------------------------------------------------------------------------------------
except  Exception as e:
    print(print(f"{ansi["Red"]}[ERROR] Could not complete uninstallation: ", e, f"{ansi["White"]}"))
#------------------------------------------------------------------------------------------------------------------------------------
#END
