import os
import ollama as llm

IGNORED_DIRS = {".git", "venv", "__pycache__"}

class readMeGen:
    def __init__(self):
        self.options = None
        self.model_name = None

    # set options for generation
    def set_options(self):
        self.options = llm.Options(
            temperature=0.7, # controls randomness of output
            max_tokens=2048, # maximum tokens to generate
        )

    # setting model to use for generation
    def set_model(self):
        MANUAL_MODEL_SET = None # set this to a specific model name if you want to use a different one
        response: llm.ListResponse = llm.list()
        if response.models:
            first_model_name = response.models[0].model
            size = response.models[0].size 
            print(f"The first model is: {first_model_name}, size: {size/1e9} GB")
            self.set_options()
            self.model_name = first_model_name
            return self

    def create_readme(self):
        if not is_readme_missing() or not is_ollama_running():
            return

        model = self.set_model()
        if model:
            print(model.options.temperature)
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
            return True
    except Exception as e:
        print(f"Error details: {e}")
    return False

# scan current directory for files and folders
def scan_directory():
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in IGNORED_DIRS]
        for file in files:
            if not file.startswith('.'):
                print(os.path.join(root, file))
