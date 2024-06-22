
import google.generativeai as genai
from essentials.ansi import ansi_color_dict, bordered_textbox
import essentials.history as history
from config.ConfigHandle import GetUserConfig,GetOutputConfigs, GetSafetyProtocols

user = GetUserConfig()
conf = GetOutputConfigs()
protocols = GetSafetyProtocols()

genai.configure(api_key = user["API_KEY"])

model = genai.GenerativeModel(user["MODEL_VERSION"])

print(f'{ansi_color_dict[conf["HEADLINE_COLOR"]]["active"]} Model : {user["MODEL_VERSION"]}{ansi_color_dict["White"]["active"]}')
print(f'{ansi_color_dict[conf["HEADLINE_COLOR"]]["active"]}{conf["HEADLINE_TEXT"]}{ansi_color_dict["White"]["active"]}')
prompt = input(f"{ansi_color_dict[conf["PROMPT_COLOR"]]["active"]}{conf["PROMPT"]}{ansi_color_dict["White"]["active"]}{ansi_color_dict[conf["INPUT_COLOR"]]["active"]}")
print(ansi_color_dict["White"]["active"], end = "")

prompts, responses = history.LoadHistory()
session = model.start_chat(history=history.GenerateHistoryStub(prompts, responses))

try:
    response = session.send_message(prompt, safety_settings=protocols)
    history.UpdateHistory(prompt, response.text)
    bordered_textbox(response.text, ansi_color_dict[conf["BORDER_COLOR"]]["active"])
except Exception as e:
    print(f"{ansi_color_dict["Red"]["active"]}[Error] Could not process prompt : {e}{ansi_color_dict["White"]["active"]}")
