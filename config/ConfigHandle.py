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



