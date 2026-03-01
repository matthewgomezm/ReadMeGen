import os
import ollama as llm

# checks if ReadMe already exists
def is_readme_missing():
    if os.path.exists("README.md"):
        print("README.md already exists. Remove it to generate a new one.")
        return False
    print("README.md does not exist.")
    return True

# checks if ollama server is running
def is_ollama_running():
    try:
        if llm.list() != 0:
            print("Ollama server is running.")
    except Exception as e:
        print(f"Error details: {e}")

# set options for generation
def set_options():
    options = llm.Options(
        temperature=0.7, # controls randomness of output
        max_tokens=2048, # maximum tokens to generate
    )
    return options

# scan current directory for files and folders
def scan_directory():
    items = os.listdir(".")
    print(f"Scanning current directory: {items}")
    return items

# setting model to use for generation
def set_model():
    MANUAL_MODEL_SET = None # set this to a specific model name if you want to use a different one
    response: llm.ListResponse = llm.list()
    if response.models:
        first_model_name = response.models[0].model
        size = response.models[0].size 
        print(f"The first model is: {first_model_name}, size: {size// 1e9} GB")
        set_options()


