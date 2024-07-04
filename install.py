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
#----------------------------------------------------------------------------------------------------------------------
import sys
import json
import time
import shutil
import platform
import subprocess
from os import path, environ, makedirs
#----------------------------------------------------------------------------------------------------------------------
ansi = {
    "White" : "\033[0;37m",
    "Green" : "\033[0;32m",
    "Yellow" : "\033[0;33m",
    "Red" : "\033[1;31m",
    "Bold Green" : "\033[1;32m"
}
#----------------------------------------------------------------------------------------------------------------------
HOME = path.expanduser("~")
LINUX_USER = HOME[6:]
WINDOWS_USER = HOME[9:]
#----------------------------------------------------------------------------------------------------------------------
def make_child_dir(dir):
    try:
        makedirs(dir)
    except FileExistsError:
        print(f"{dir} already exists")
#----------------------------------------------------------------------------------------------------------------------
try:
    ch = input(f"{ansi['Yellow']}Do you want to proceed with the installation of Geminux [y/n] ?{ansi['White']}")
    #------------------------------------------------------------------------------------------------------------------
    if ch.upper() == "Y" or ch.upper() == "YES":
        #--------------------------------------------------------------------------------------------------------------
        if platform.architecture()[1] == "ELF":
            SHELL = environ.get("SHELL", "")
            print(f"{ansi["Green"]}[+] collecting modules 1 of 1{ansi["White"]}")
            time.sleep(0.5)
            #-----------------------------------------------------------------------------------------------------------
            subprocess.call(
                ["pip", "install", "google-generativeai", "--break-system-packages"]
            )
            time.sleep(1)
            print(f"{ansi["Green"]}[+]module installed{ansi["White"]}")
            time.sleep(0.5)
            #-----------------------------------------------------------------------------------------------------------
            MODEL_NAME = input(f"""{ansi["Yellow"]}
    By what name would you like to address Geminux ? 
    Default name is Geminux [This is an optional parameter, you can change the name later from ~/.config/geminux/config.json]
    press enter to keep default settings or enter a name if you want.
    >{ansi["White"]}""")
            if MODEL_NAME == "":
                MODEL_NAME = "Geminux"
            API_KEY = input(f"{ansi["Yellow"]}Enter your API key : {ansi["White"]}")
            #-----------------------------------------------------------------------------------------------------------
            with open("config/config.json", "r") as file:
                json_data = json.load(file)
                file.close()
            #-----------------------------------------------------------------------------------------------------------
            json_data[0]["API_KEY"] = API_KEY
            json_data[0]["USER"] = LINUX_USER
            json_data[0]["MODEL_NAME"] = MODEL_NAME
            #-----------------------------------------------------------------------------------------------------------
            with open("config/config.json", "w") as file:
                json.dump(json_data, file)
                file.close()
            #-----------------------------------------------------------------------------------------------------------
            print(f"{ansi["Bold Green"]}[+]Config file generated")
            time.sleep(1)
            print(f"Creating {HOME}/.Geminux")
            subprocess.call(["mkdir", f"{HOME}/.Geminux"])
            time.sleep(0.5)
            #-----------------------------------------------------------------------------------------------------------
            print(f"Creating build files inside {HOME}/.Geminux")
            subprocess.call(["cp", "-r", "config", f"{HOME}/.Geminux"])
            subprocess.call(["cp", "-r", "essentials", f"{HOME}/.Geminux"])
            subprocess.call(["cp", "-r", "history", f"{HOME}/.Geminux"])
            subprocess.call(["cp", "main.py", f"{HOME}/.Geminux"])
            #-----------------------------------------------------------------------------------------------------------
            time.sleep(0.5)
            print("Creating uninstaller")
            subprocess.call(["cp", "uninstall.py", f"{HOME}/.Geminux"])
            time.sleep(0.5)
            #-----------------------------------------------------------------------------------------------------------
            print(f"Creating {HOME}/.config/Geminux")
            subprocess.call(["mkdir", f"{HOME}/.config/Geminux"])
            time.sleep(0.5)
            #-----------------------------------------------------------------------------------------------------------
            print(f"Adding config.json to {HOME}/.config/Geminux")
            subprocess.call(["cp", "config/config.json", f"{HOME}/.config/Geminux"])
            subprocess.call(["rm", f"{HOME}/.Geminux/config/config.json"])
            time.sleep(0.5)
            #-----------------------------------------------------------------------------------------------------------
            print(f"Generating history.json file{ansi["White"]}")
            #------------------------------------------------------------------------------------------------------------
            if "zsh" in SHELL:
                #--------------------------------------------------------------------------------------------------------
                print("updating ~/.zshrc")
                #--------------------------------------------------------------------------------------------------------
                with open(f"{HOME}/.zshrc", "a") as shell_file:
                    shell_file.write("alias geminux='python ~/.Geminux/main.py'\n")
                    shell_file.write("bindkey -s '^ ' 'geminux^M'")
                    shell_file.write("\n")
                    shell_file.close()
                #--------------------------------------------------------------------------------------------------------
                print("type geminux to activate the model")
                print("you can also use the keybinding ctrl + space to activate the same")
                print("you can now re-lode the terminal")
                #--------------------------------------------------------------------------------------------------------
            elif "bash" in SHELL:
                #--------------------------------------------------------------------------------------------------------
                with open(f"{HOME}/.bashrc", "a") as shell_file:
                    shell_file.write("alias geminux='python ~/.geminux/main.py'\n")
                    shell_file.close()
                #--------------------------------------------------------------------------------------------------------
                print("type geminux to activate the model")
                print("you can now re-lode the terminal")
            #------------------------------------------------------------------------------------------------------------        
            print(f"{ansi["Bold Green"]}For more projects visit www.github.com/mintRaven-05{ansi["White"]}")
            #------------------------------------------------------------------------------------------------------------
        elif platform.architecture()[1] == "WindowsPE":
            #------------------------------------------------------------------------------------------------------------
            print(f"{ansi["Green"]}[+] collecting modules 1 of 1{ansi["White"]}")
            time.sleep(1)
            subprocess.run("pip install google-generativeai")
            print(f"{ansi["Green"]}[+]module installed{ansi["White"]}")
            time.sleep(1)
            #------------------------------------------------------------------------------------------------------------
            MODEL_NAME = input(f"""{ansi["Yellow"]}
    By what name would you like to address Geminux ? 
    Default name is Geminux [This is an optional parameter, you can change the name later from ~/.config/geminux/config.json]
    press enter to keep default settings or enter a name if you want.
    >{ansi["White"]}""")
            if MODEL_NAME == "":
                MODEL_NAME = "Geminux"
            API_KEY = input(f"{ansi["Yellow"]}Enter your API key : {ansi["White"]}")
            #------------------------------------------------------------------------------------------------------------
            with open("config\\config.json", "r") as file:
                json_data = json.load(file)
                file.close()
            #------------------------------------------------------------------------------------------------------------
            json_data[0]["API_KEY"] = API_KEY
            json_data[0]["USER"] = WINDOWS_USER
            json_data[0]["MODEL_NAME"] = MODEL_NAME
            #------------------------------------------------------------------------------------------------------------
            with open("config\\config.json", "w") as file:
                json.dump(json_data, file)
                file.close()
            print(f"{ansi["Bold Green"]}Config file generated")
            time.sleep(1)
            #------------------------------------------------------------------------------------------------------------
            try:
                #--------------------------------------------------------------------------------------------------------
                parent_dir = f"{HOME}\\.Geminux"
                makedirs(parent_dir)
                config_child = f"{HOME}\\.Geminux\\config"
                essentials_child = f"{HOME}\\.Geminux\\essentials"
                history_child = f"{HOME}\\.Geminux\\hsitory"
                #--------------------------------------------------------------------------------------------------------
                make_child_dir(config_child)
                make_child_dir(essentials_child)
                make_child_dir(history_child)
                #--------------------------------------------------------------------------------------------------------
            except FileExistsError:
                #--------------------------------------------------------------------------------------------------------
                print(f"File {HOME}\\.Geminux already exists")
                #--------------------------------------------------------------------------------------------------------
            try:
                #--------------------------------------------------------------------------------------------------------
                config_dir = f"{HOME}\\.config"
                makedirs(config_dir)
                make_child_dir(f"{HOME}\\.config\\Geminux")
                #--------------------------------------------------------------------------------------------------------
            except FileExistsError:
                #--------------------------------------------------------------------------------------------------------
                print(f"{HOME}\\.config already exists")
                #--------------------------------------------------------------------------------------------------------

            #------------------------------------------------------------------------------------------------------------
            print(f"moving config.json into {HOME}\\.config")
            shutil.copy("./config/config.json", f"{HOME}\\.config\\Geminux")
            time.sleep(0.5)
            #------------------------------------------------------------------------------------------------------------
            print(f"moving config handlers into {HOME}\\.Geminux")
            shutil.copytree("config", f"{HOME}\\.Geminux\\config", dirs_exist_ok=True)
            time.sleep(0.5)
            #------------------------------------------------------------------------------------------------------------
            print(f"moving essential libs into {HOME}\\.Geminux")
            shutil.copytree("essentials", f"{HOME}\\.Geminux\\essentials", dirs_exist_ok=True)
            time.sleep(0.5)
            #------------------------------------------------------------------------------------------------------------
            print(f"moving history/history.json into {HOME}\\.Geminux")
            shutil.copytree("history", f"{HOME}\\.Geminux\\history", dirs_exist_ok=True)
            time.sleep(0.5)
            #------------------------------------------------------------------------------------------------------------
            print(f"moving main file to {HOME}\\.Geminux")
            shutil.copy2("./main.py", f"{HOME}\\.Geminux")
            time.sleep(0.5)
            #------------------------------------------------------------------------------------------------------------
            print("preparing uninstaller")
            shutil.copy2("./uninstall.py", f"{HOME}\\.Geminux")
            time.sleep(0.5)
            #------------------------------------------------------------------------------------------------------------
            print(f"Installation completed, you can add Geminux to your $PROFILE{ansi["White"]}")
            print("visit www.github.com/mintRaven-05 for more projects")
        #----------------------------------------------------------------------------------------------------------------
        else:
            print(f"{ansi["Red"]}Geminux is only compatible with Linux and Windows, you can install manually in that case !{ansi["White"]}")
    #--------------------------------------------------------------------------------------------------------------------     
    elif ch.upper() == "N" or ch.upper() == "NO":
        print("Understandable . . .")
        sys.exit(0)
    #--------------------------------------------------------------------------------------------------------------------
    else:
        print(f"{ansi["Red"]}Invalid Choice")
        print(f"exiting . . .{ansi["White"]}")
        sys.exit(0)
    #--------------------------------------------------------------------------------------------------------------------
except Exception as e:
    print(f"{ansi["Red"]}[ERROR]Could not complete installation : ", e, f"{ansi["White"]}")
#------------------------------------------------------------------------------------------------------------------------
#END
