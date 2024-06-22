import os
import json
from collections import deque
from config.ConfigHandle import GetUserConfig

HOME = os.path.expanduser("~")
user = GetUserConfig()
username = user["USER"]
modelname = user["MODEL_NAME"]


def LoadHistory() -> tuple[deque, deque]:
    with open(f"{HOME}/.Geminux/history/history.json", "r") as json_file:
        DATA = json.load(json_file)
        PROMPTS = []
        RESPONSES = []
        for i in range(len(DATA)):
            PROMPTS.append(DATA[i]["prompt"])
            RESPONSES.append(DATA[i]["response"])
        PROMPT_QUEUE = deque(PROMPTS)
        RESPONSE_QUEUE = deque(RESPONSES)
    return PROMPT_QUEUE, RESPONSE_QUEUE


def UpdateHistory(prompt:str, response:str) -> None:
    with open(f"{HOME}/.Geminux/history/history.json", "r") as read_json_file:
        data = json.load(read_json_file)
        count = len(data)
        prompt_list = []
        response_list = []

        for i in range(len(data)):
            prompt_list.append(data[i]["prompt"])
            response_list.append(data[i]["response"])

        prompt_queue = deque(prompt_list)
        response_queue = deque(response_list)

        if count == 5:
            prompt_queue.popleft()
            response_queue.popleft()
            del data[0]
            data.append({"prompt" : prompt, "response" : response})
            read_json_file.close()
            with open(f"{HOME}/.Geminux/history/history.json", "w") as write_json_file_hist:
                json.dump(data, write_json_file_hist)
                write_json_file_hist.close()


def GenerateHistoryStub(prompts : deque, responses : deque) -> list:
    
    history = [

        {
            "role" : "user",
            "parts" : [
                f"Your name is {modelname}, assistant of {username} for his personal assistance"
            ],

        },
        {
            "role" : "model",
            "parts" : [
                f"greetings {username}, i am {modelname} you personal assitant. How can i help you today ?"
            ]
        },
        {
            "role" : "user",
            "parts": [
                "No matter what i ask, always provide brief answers with details always in the form of bullet points. Also avoid using bold letters"
            ],
        },
        {
            "role" : "model",
            "parts" : [
                f"understood {username}, i will always provide brief answers with details in bullet point format. I will also not use bold letters from now on"
            ]
        },
             {
         "role" : "user",
         "parts" : [
             prompts[0]
         ]
     },
     {
         "role" : "model",
         "parts" : [
             responses[0]
         ]
     },
     {
         "role" : "user",
         "parts" : [
             prompts[1]
         ]
     },
     {
         "role" : "model",
         "parts" : [
             responses[1]
         ]
     },
     {
         "role" : "user",
         "parts" : [
             prompts[2]
         ]
     },
     {
         "role" : "model",
         "parts" : [
             responses[2]
         ]
     },
     {
         "role" : "user",
         "parts" : [
             prompts[3]
         ]
     },
     {
         "role" : "model",
         "parts" : [
             responses[3]
         ]
     },
     {
         "role" : "user",
         "parts" : [
             prompts[4]
         ]
     },
     {
         "role" : "model",
         "parts" : [
             responses[4]
         ]
     },
    ]
    return history
