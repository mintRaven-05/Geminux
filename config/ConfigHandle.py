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

import os
import json

HOME = os.path.expanduser("~")

def GetUserConfig():
    with open(f"{HOME}/.config/Geminux/config.json", "r") as conf_file:
        config = json.load(conf_file)
        user_details = config[0]
        conf_file.close()
    
    return user_details

def GetOutputConfigs():
    with open(f"{HOME}/.config/Geminux/config.json", "r") as conf_file:
        config = json.load(conf_file)
        border_details = config[1]
        conf_file.close()
    
    return border_details

def GetSafetyProtocols():
    with open(f"{HOME}/.config/Geminux/config.json", "r") as conf_file:
        config = json.load(conf_file)
        safety_protocols = config[2]["SAFETY_PROTOCOLS"][0]
        conf_file.close()
    
    return safety_protocols



