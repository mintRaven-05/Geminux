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
#------------------------------------------------------------------------------------------------------------------------------------
import google.generativeai as genai
from essentials.ansi import ansi_color_dict, bordered_textbox
import essentials.history as history
from config.ConfigHandle import GetUserConfig,GetOutputConfigs, GetSafetyProtocols
#------------------------------------------------------------------------------------------------------------------------------------
user = GetUserConfig()
conf = GetOutputConfigs()
protocols = GetSafetyProtocols()
#------------------------------------------------------------------------------------------------------------------------------------
genai.configure(api_key = user["API_KEY"])
model = genai.GenerativeModel(user["MODEL_VERSION"])
#------------------------------------------------------------------------------------------------------------------------------------
BORDER_COLOR = ansi_color_dict[conf["BORDER_COLOR"]]["active"]
HEADLINE_COLOR = ansi_color_dict[conf["HEADLINE_COLOR"]]["active"]
HEADLINE_TEXT = conf["HEADLINE_TEXT"]
MODEL = user["MODEL_VERSION"]
RESET = ansi_color_dict["White"]["active"]
PROMPT_COLOR = ansi_color_dict[conf["PROMPT_COLOR"]]["active"]
PROMPT = conf["PROMPT"]
INPUT_COLOR = ansi_color_dict[conf["INPUT_COLOR"]]["active"]
ERROR_COLOR = ansi_color_dict["Red"]["active"]
#------------------------------------------------------------------------------------------------------------------------------------
print(f'{HEADLINE_COLOR} Model : {MODEL}{RESET}')
print(f'{HEADLINE_COLOR}{HEADLINE_TEXT}{RESET}')
#------------------------------------------------------------------------------------------------------------------------------------
try:
    prompt = input(f"{PROMPT_COLOR}{PROMPT}{RESET}{INPUT_COLOR}")
#------------------------------------------------------------------------------------------------------------------------------------
except KeyboardInterrupt:
    print(f"\n{ERROR_COLOR}[EXIT]{RESET}")
print(RESET, end = "")
#------------------------------------------------------------------------------------------------------------------------------------
prompts, responses = history.LoadHistory()
session = model.start_chat(history=history.GenerateHistoryStub(prompts, responses))
#------------------------------------------------------------------------------------------------------------------------------------
try:
    response = session.send_message(prompt, safety_settings=protocols)  
    bordered_textbox(response.text, BORDER_COLOR)
    history.UpdateHistory(prompt, response.text)
#------------------------------------------------------------------------------------------------------------------------------------
except Exception as e:
    print(f"{ERROR_COLOR}[Error] Could not process prompt : {e}{RESET}")
#------------------------------------------------------------------------------------------------------------------------------------
