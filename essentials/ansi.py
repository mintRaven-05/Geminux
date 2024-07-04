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
import time
from dataclasses import dataclass
from config.ConfigHandle import GetOutputConfigs
#------------------------------------------------------------------------------------------------------------------------------------
confs = GetOutputConfigs()
#------------------------------------------------------------------------------------------------------------------------------------
@dataclass
class AnsiColor:
    active : str = "\033[0;37m"
    label : str = "White"
#------------------------------------------------------------------------------------------------------------------------------------
#create general ANSI colors
def MakeAnsiNormal(color : AnsiColor) -> dict[str, str]:
    ansi_chars = [c for c in color.active]
    ansi_chars[2] = "0"
    new_active = ''.join(ansi_chars)

    new_label = color.label
    ansi_dict = {"active" : new_active, "label" : new_label}
    return ansi_dict
#------------------------------------------------------------------------------------------------------------------------------------
#Create Bold ANSI colors
def MakeAnsiBold(color : AnsiColor) -> dict[str, str]:
    ansi_chars = [c for c in color.active]
    ansi_chars[2] = "1"
    new_active = ''.join(ansi_chars)

    new_label = 'Bold '+color.label
    ansi_dict = {"active" : new_active, "label" : new_label}
    return ansi_dict
#------------------------------------------------------------------------------------------------------------------------------------
#Create Underline style ANSI color
def MakeAnsiUnderline(color : AnsiColor) -> dict[str, str]:
    ansi_chars = [c for c in color.active]
    ansi_chars[2] = "4"
    new_active = ''.join(ansi_chars)

    new_label = 'Underline '+color.label
    ansi_dict = {"active" : new_active, "label" : new_label}
    return ansi_dict
#------------------------------------------------------------------------------------------------------------------------------------
#Create  Italic style ANSI color
def MakeAnsiItalic(color : AnsiColor) -> dict[str, str]:
    ansi_chars = [c for c in color.active]
    ansi_chars[2] = "3"
    new_active = ''.join(ansi_chars)

    new_label = 'Italic '+color.label
    ansi_dict = {"active" : new_active, "label" : new_label}
    return ansi_dict
#------------------------------------------------------------------------------------------------------------------------------------
#Create Bold and Underline style ANSI color
def MakeAnsiBoldUnderline(color : AnsiColor) -> dict[str, str]:
    ansi_chars = [c for c in color.active]
    ansi_chars[2] = "1;4"
    new_active = ''.join(ansi_chars)

    new_label = 'Bold Underline '+color.label
    ansi_dict = {"active" : new_active, "label" : new_label}
    return ansi_dict
#------------------------------------------------------------------------------------------------------------------------------------
#Create Bold and Italic style ANSI color
def MakeAnsiBoldItalic(color : AnsiColor) -> dict[str, str]:
    ansi_chars = [c for c in color.active]
    ansi_chars[2] = "1;3"
    new_active = ''.join(ansi_chars)

    new_label = 'Bold Italic '+color.label
    ansi_dict = {"active" : new_active, "label" : new_label}
    return ansi_dict 
#------------------------------------------------------------------------------------------------------------------------------------
#Create Underline and Italic style ANSI color
def MakeAnsiUnderlineItalic(color : AnsiColor) -> dict[str, str]:
    ansi_chars = [c for c in color.active]
    ansi_chars[2] = "3;4"
    new_active = ''.join(ansi_chars)

    new_label = 'Underline Italic '+color.label
    ansi_dict = {"active" : new_active, "label" : new_label}
    return ansi_dict
#------------------------------------------------------------------------------------------------------------------------------------
#Create Bold Underline and Italic style ANSI color
def MakeAnsiBoldUnderlineItalic(color : AnsiColor) -> dict[str, str]:
    ansi_chars = [c for c in color.active]
    ansi_chars[2] = "1;3;4"
    new_active = ''.join(ansi_chars)

    new_label = 'Bold Underline Italic '+color.label
    ansi_dict = {"active" : new_active, "label" : new_label}
    return ansi_dict
#------------------------------------------------------------------------------------------------------------------------------------
reset = AnsiColor("\033[0;37m")
red = AnsiColor("\033[0;31m", "Red")
blue = AnsiColor("\033[0;34m", "Blue")
cyan = AnsiColor("\033[0;36m", "Cyan")
green = AnsiColor("\033[0;32m", "Green")
black = AnsiColor("\033[0;30m", "Black")
yellow = AnsiColor("\033[0;33m", "Yellow")
purple = AnsiColor("\033[0;35m", "Purple")
#------------------------------------------------------------------------------------------------------------------------------------
#Color dictionary
ansi_color_dict = {
    #--------------------------------------------------------------------------------------------------------------------------------
    "Red" : MakeAnsiNormal(red),
    "Blue" : MakeAnsiNormal(blue),
    "Cyan" : MakeAnsiNormal(cyan),
    "White" : MakeAnsiNormal(reset),
    "Green" : MakeAnsiNormal(green),
    "Black" : MakeAnsiNormal(black),
    "Yellow" : MakeAnsiNormal(yellow),
    "Purple" : MakeAnsiNormal(purple),
    #--------------------------------------------------------------------------------------------------------------------------------
    "Bold Red" : MakeAnsiBold(red),
    "Bold Blue" : MakeAnsiBold(blue),
    "Bold Cyan" : MakeAnsiBold(cyan),
    "Bold White" : MakeAnsiBold(reset),
    "Bold Green" : MakeAnsiBold(green),
    "Bold Black" : MakeAnsiBold(black),
    "Bold Yellow" : MakeAnsiBold(yellow),
    "Bold Purple" : MakeAnsiBold(purple),
    #--------------------------------------------------------------------------------------------------------------------------------
    "Italic Red" : MakeAnsiItalic(red),
    "Italic Blue" : MakeAnsiItalic(blue),
    "Italic Cyan" : MakeAnsiItalic(cyan),
    "Italic White" : MakeAnsiItalic(reset),
    "Italic Green" : MakeAnsiItalic(green),
    "Italic Black" : MakeAnsiItalic(black),
    "Italic Yellow" : MakeAnsiItalic(yellow),
    "Italic Purple" : MakeAnsiItalic(purple),
    #--------------------------------------------------------------------------------------------------------------------------------
    "Underline Red" : MakeAnsiUnderline(red),
    "Underline Blue" : MakeAnsiUnderline(blue),
    "Underline Cyan" : MakeAnsiUnderline(cyan),
    "Underline White" : MakeAnsiUnderline(reset),
    "Underline Green" : MakeAnsiUnderline(green),
    "Underline Black" : MakeAnsiUnderline(black),
    "Underline Yellow" : MakeAnsiUnderline(yellow),
    "Underline Purple" : MakeAnsiUnderline(purple),
    #--------------------------------------------------------------------------------------------------------------------------------
    "Bold Italic Red" : MakeAnsiBoldItalic(red),
    "Bold Italic Blue" : MakeAnsiBoldItalic(blue),
    "Bold Italic Cyan" : MakeAnsiBoldItalic(cyan),
    "Bold Italic White" : MakeAnsiBoldItalic(reset),
    "Bold Italic Green" : MakeAnsiBoldItalic(green),
    "Bold Italic Black" : MakeAnsiBoldItalic(black),
    "Bold Italic Yellow" : MakeAnsiBoldItalic(yellow),
    "Bold Italic Purple" : MakeAnsiBoldItalic(purple),
    #--------------------------------------------------------------------------------------------------------------------------------
    "Bold Underline Red" : MakeAnsiBoldUnderline(red),
    "Bold Underline Blue" : MakeAnsiBoldUnderline(blue),
    "Bold Underline Cyan" : MakeAnsiBoldUnderline(cyan),
    "Bold Underline White" : MakeAnsiBoldUnderline(reset),
    "Bold Underline Green" : MakeAnsiBoldUnderline(green),
    "Bold Underline Black" : MakeAnsiBoldUnderline(black),
    "Bold Underline Yellow" : MakeAnsiBoldUnderline(yellow),
    "Bold Underline Purple" : MakeAnsiBoldUnderline(purple),
    "Underline Italic Red" : MakeAnsiUnderlineItalic(red),
    "Underline Italic Blue" : MakeAnsiUnderlineItalic(blue),
    "Underline Italic Cyan" : MakeAnsiUnderlineItalic(cyan),
    "Underline Italic White" : MakeAnsiUnderlineItalic(reset),
    "Underline Italic Green" : MakeAnsiUnderlineItalic(green),
    "Underline Italic Black" : MakeAnsiUnderlineItalic(black),
    "Underline Italic Yellow" : MakeAnsiUnderlineItalic(yellow),
    "Underline Italic Purple" : MakeAnsiUnderlineItalic(purple),
    #--------------------------------------------------------------------------------------------------------------------------------
    "Bold Underline Italic Red" : MakeAnsiBoldUnderlineItalic(red),
    "Bold Underline Italic Blue" : MakeAnsiBoldUnderlineItalic(blue),
    "Bold Underline Italic Cyan" : MakeAnsiBoldUnderlineItalic(cyan),
    "Bold Underline Italic White" : MakeAnsiBoldUnderlineItalic(reset),
    "Bold Underline Italic Green" : MakeAnsiBoldUnderlineItalic(green),
    "Bold Underline Italic Black" : MakeAnsiBoldUnderlineItalic(black),
    "Bold Underline Italic Yellow" : MakeAnsiBoldUnderlineItalic(yellow),
    "Bold Underline Italic Purple" : MakeAnsiBoldUnderlineItalic(purple),
    #--------------------------------------------------------------------------------------------------------------------------------
}
#------------------------------------------------------------------------------------------------------------------------------------
#Output Border that will enclose the response
def bordered_textbox(text : str, color : AnsiColor) -> str:
    lines = text.splitlines()
    width = max(len(s) for s in lines)

    res = [confs["BORDER_NW"] + confs["BORDER_ROOF"] * width + confs["BORDER_NE"]]
    for s in lines:
        if s != '':
            res.append(f'{color}{confs["BORDER_WALL"]}{reset.active}' + ansi_color_dict[confs["RESPONSE_COLOR"]]["active"]+(s + ' ' * width)[:width]+ansi_color_dict["White"]["active"] + f'{color}{confs["BORDER_WALL"]}{reset.active}')
        else:
            res.append(f'{color}{confs["BORDER_WALL"]}{reset.active}'+ (' ' * width)[:width] + f'{color}{confs["BORDER_WALL"]}{reset.active}')
    res.append(confs["BORDER_SW"] + confs["BORDER_FLOOR"] * width + confs["BORDER_SE"])
    print(color, end="")
    print(res[0])
    print(reset.active, end="")
    for string in res[1:-1]:
        
        for char in string:
            print(char, end="", flush=True)
            time.sleep(0.001)
    
        print()
    print(color, end="")
    print(res[-1])
    print(reset.active, end="")
    return '\n'.join(res)
#------------------------------------------------------------------------------------------------------------------------------------



