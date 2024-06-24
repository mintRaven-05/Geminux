# GEMINUX
#### Python Licence 

## Purpose

Geminux is a CLI tool, which uses the Google AI studio Gemini API to provide an interactive session between the user and Google Gemini. It leverages the power of Gemini 1.5 pro, a versatile language model trained by Google, to create natural language text. This tool is created with new features which are not provided by Google, and we will discuss them one by one later in this file.

### Prerequisites 
- Having Nerd Font is necessary, else some of the symbols might not be displayed. After installing Nerd Font, apply it to your terminal.
- You can install the font from this link https://www.nerdfonts.com/font-downloads
- It is necessary to make an account in Google AI studio and get yourself an API key, as it will be required while proceeding with the installation process.
- If you don't have an API, you can make one from here https://ai.google.dev/gemini-api
- You also need python pre-installed in the machine.
- If you don't have python installed, you can install the latest version by visiting the link below.
- https://www.python.org/

### Features
- ***Coherent Text Generation***: Generate creative responses based on prompts given by the user
- ***Ability to remember context***: It can remember upto last 5 conversations.
- ***Soft training:*** implementation of a soft training method using the data from a history file.
- ***Configurable***: User can configure the whole output along with safety protocols. 
- ***Easy to use CLI interface***: User is provided with a very easy to use interface with text generation animation.

## Installation
### Linux

An installer script is already made. All you need to do is run the script using python. Copy the following codes and run it in your terminal.

- Clone the repository

```bash
git clone https://github.com/mintRaven-05/Geminux.git
```

- Run the installer script

```bash
cd Geminux
python install.py
```

After running the script, provide a name to the model (optional) and an API key (mandatory) when required and it will install the model with the default aliases for your respective shell. You will get the name of the alias by which you can activate the model at the end after installation.

### Windows

The same installer script used for Linux can also be used to install Geminux in Windows using Python.
Copy the following codes and run it in your terminal.

- Clone the repository
  
```bash
git clone https://github.com/mintRaven-05/Geminux.git
```

- Run the installer script

```bash
cd Geminux
python install.py
```

After running the script, you can provide a name to the model (optional) and an API key (mandatory) when required and it will install the model.
After installation, you can add a function to your Powershell profile to activate Gemini anytime from anywhere in your Powershell.
If you don't have a Powershell profile, then you can create one using the following code

```bash
New-Item -Path $PROFILE -type File -force
```

if you already have one or you have created a new one, open it using the following command

```bash
notepad $PROFILE
```

and now add the function to activate Geminux globally

```bash
function geminux{python.exe "<YOUR HOME PATH>\.Gemminux\main.py"}
```

Save the file after writing the function and reload your terminal. Now you can type just `geminux` in your Powershell and it will start the model. 

## Demo Screenshot

![swappy-20240622_195759](https://github.com/I-DebjeetBanerjee/Geminux/assets/136410764/dd515daf-8f54-4904-ac81-bafdb7ba13ec)

## Configuration
After installing Geminux, a config folder will be created with the following path `~/.config/Geminux`, inside which `config.json` will be present. This file is divided into 3 categories.
- **User and model configuration**
- **Output configuration**
- **Safety protocols configuration**
#### User and model configuration

![swappy-20240622_200901](https://github.com/I-DebjeetBanerjee/Geminux/assets/136410764/30294a3f-2de7-45eb-861b-67270b6ebd5e)
- **`API_KEY`:** To hold your API, which will be used by the model to fetch responses.
- **`MODEL_VERSION`:** Specify the Gemini model that you want to use, default is `gemini-1.5-pro`
- **`MODEL_NAME`:** Specify the name by which you want to address it, default name is `Geminux`
- **`USER`:** Specify the name by which you want the model to address you.

#### Output configuration

![swappy-20240622_201325](https://github.com/I-DebjeetBanerjee/Geminux/assets/136410764/f30fcf52-fbea-4fe8-8ada-75b5df2f3a8d)
-  **`BORDER_*`*** : Everything that starts with BORDER_ are the components required by the border that encloses the response as show in the demo screenshot.
- **`HEADLINE_TEXT`:** This text will appear after the Model is printed over the terminal. Default is empty, and you keep it default if you don't want any custom headline.
- **`HEADLINE_COLOR`:** As the name suggests, this will set color to the headline, which includes the model version that will be printed.
- **`PROMPT`:** This is the input prompt which will appear when giving input to Geminux.
- **`PROMPT_COLOR`:** : Again as the name suggests, will set the prompt color.
- **`INPUT_COLOR`:** will set the style and color of the input that the you will give.
- **`RESPONSE_COLOR`:** This will set the color of the response enclosed inside the border.
- Different ANSI color choices and different styles are well documented inside the `config.json` file. You can use all those colors wherever it is applicable for Geminux.
#### Safety protocols configuration

![swappy-20240622_201354](https://github.com/I-DebjeetBanerjee/Geminux/assets/136410764/9aa20f5e-2061-48ad-9c9e-a84c59f0025f)
- There are only 4 categories of safety settings, as mentioned in the above screenshot
- Each one of them can be blocked by upto 5 different levels of thresholds.
- The 5 thresholds are listed below
	- `BLOCK_NONE`
	- `BLOCK_LOW_AND_ABOVE`
	- `BLOCK_MEDIUM_AND_ABOVE`
	- `BLOCK_ONLY_HIGH`
	- `HARM_BLOCK_THRESHOLD_UNSPECIFIED`
Everything is well documented inside the config file. You can config Geminux as per your need by changing these available settings.

## Uninstall

After installation, a folder is generated inside the home directory. Path to that folder is `~/.Geminux`. Inside this folder all the necessary files for Geminux to function are moved. But along with those necessary files, an uninstaller is also moved which is again a python script. So, in order to uninstall Geminux all you need to do is run the following command in your terminal.

```bash
python ~/.Geminux/uninstall.py
```

<p align="center">Copyright &copy; 2024 <a href="https://github.com/mintRaven-05" target="_blank">Debjeet Banerjee</a>
<p align="center"><a href="https://github.com/mintRaven-05/Geminux/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a></p>





