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

import sys
import json
import time
import platform
import subprocess
from os import path, environ

HOME = path.expanduser("~")
SHELL = environ.get("SHELL", "")
USER = HOME[6:]

try:
    ch = input("Do you want to proceed with the installation of Geminux [y/n] ?")
    if ch.upper() == "Y" or ch.upper() == "YES":
        if platform.architecture()[1] == "ELF":
            print("collecting modules 1 of 1")
            time.sleep(0.5)
            subprocess.call(
                ["pip", "install", "google-generativeai", "--break-system-packages"]
            )
            time.sleep(1)
            print("\033[0;32m[+]\033[0;37m module installed")
            time.sleep(0.5)
            MODEL_NAME = input("""
    By what name would you like to address Geminux ? 
    Default name is Geminux [This is an optional parameter, you can change the name later from ~/.config/geminux/config.json]
    press enter to keep default settings or enter a name if you want.
    >""")
            if MODEL_NAME == "":
                MODEL_NAME = "Geminux"
            API_KEY = input("Enter your API key : ")
            with open("config/config.json", "r") as file:
                json_data = json.load(file)
                file.close()

            json_data[0]["API_KEY"] = API_KEY
            json_data[0]["USER"] = USER
            json_data[0]["MODEL_NAME"] = MODEL_NAME

            with open("config/config.json", "w") as file:
                json.dump(json_data, file)
                file.close()
            print("\033[0;32m[+]\033[0;37m Config file generated")
            time.sleep(1)
            print(f"Creating {HOME}/.Geminux")
            subprocess.call(["mkdir", f"{HOME}/.Geminux"])
            time.sleep(0.5)
            print(f"Creating build files inside {HOME}/.Geminux")
            subprocess.call(["cp", "-r", "config", f"{HOME}/.Geminux"])
            subprocess.call(["cp", "-r", "essentials", f"{HOME}/.Geminux"])
            subprocess.call(["cp", "-r", "history", f"{HOME}/.Geminux"])
            subprocess.call(["cp", "main.py", f"{HOME}/.Geminux"])
            time.sleep(0.5)
            print("Creating uninstaller")
            subprocess.call(["cp", "uninstall.py", f"{HOME}/.Geminux"])
            time.sleep(0.5)
            print(f"Creating {HOME}/.config/Geminux")
            subprocess.call(["mkdir", f"{HOME}/.config/Geminux"])
            time.sleep(0.5)
            print(f"Adding config.json to {HOME}/.config/Geminux")
            subprocess.call(["cp", "config/config.json", f"{HOME}/.config/Geminux"])
            subprocess.call(["rm", f"{HOME}/.Geminux/config/config.json"])
            time.sleep(0.5)
            print(f"Generating history.json file")

            if "zsh" in SHELL:
                print("updating ~/.zshrc")
                with open(f"{HOME}/.zshrc", "a") as shell_file:
                    shell_file.write("alias geminux='python ~/.Geminux/main.py'\n")
                    shell_file.write("bindkey -s '^ ' 'geminux^M'")
                    shell_file.write("\n")
                    shell_file.close()
                print("type geminux to activate the model")
                print(
                    "you can also use the keybinding ctrl + space to activate the same"
                )
                print("you can now re-lode the terminal")

            elif "bash" in SHELL:
                with open(f"{HOME}/.bashrc", "a") as shell_file:
                    shell_file.write("alias geminux='python ~/.geminux/main.py'\n")
                    shell_file.close()

                print("type geminux to activate the model")
                print("you can now re-lode the terminal")
        else:
            print("Development and itegration for platforms other than linux is still going on...sorry for the inconvinience")
    elif ch.upper() == "N" or ch.upper() == "NO":
        print("Understandable . . .")
        sys.exit(0)
    else:
        print("Invalid Choice")
        print("exiting . . .")
        sys.exit(0)

except Exception as e:
    print("\033[0;31m[ERROR]\033[0;37m Could not complete installation : ", e)
    subprocess.call("rm", "-rf", f"{HOME}/.Geminux")
