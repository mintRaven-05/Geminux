
# GEMINUX
Python Licence 

## Purpose
Geminux is a CLI tool, which uses the google AI studio Gemini API to provide an interactive session between the user and Google Gemini. It leverages the power of Gemini 1.5 pro, a versatile language model trained by Google, to create natural language text. This tool is created with new features which are not provided by Google, and we will discuss them one by one later in this file.

### Prerequisites 
- Having Nerd Font is necessary, else some of the symbols might not be displayed. After installing Nerd Font, apply it to your terminal.
- You can install the font from this link https://www.nerdfonts.com/font-downloads
- It is necessary to make an account in Google AI studio and get yourself an API key, as it will be required while proceeding with the installation process.
- If you don't have an API, you can make one from here https://ai.google.dev/gemini-api
- You also need python pre-installed in the machine.
- If you don't have python installed, you can install the latest version by visiting the link below.
- https://www.python.org/

### Notice
This tool is currently made for just Linux and not windows. I will soon make windows integration for this CLI tool

### Features
- ***Coherent Text Generation***: Generate creative responses based on prompts given by the user
- ***Ability to remember context***: It can remember upto last 5 conversations, by implementing a soft training using the data from a history file.
- ***Configurable***: User configure the whole output along with the ability to change to model name and also the name by which the user wants the model to address him/her.
- ***Easy to use CLI interface***: User is provided with a very easy to use interface with text generation animation.

## Installation
An installer script is already made. All you need to do is run the script using python. Copy the following codes and run it on your terminal.

- Copy the repository

```bash
git clone 
```

- Run the installer script

```bash
cd Geminux
python install.py
```

After running the script, provide a name to the model (optional) and an API key (mandatory) when required and it will install the model the default aliases for your respective shell. You will get the name of the alias by which you can activate the model at the end after installation.

## Demo

![[Geminux  1.gif]]
