import os
import ollama as llm
import re

IGNORED_DIRS = {".git", "venv", "__pycache__"}

class readMeGen:
    def __init__(self):
        self.options = None
        self.model_name = None

    # set options for generation
    def set_options(self):
        self.options = llm.Options(
            temperature=0.7, # controls randomness of output, can change
            max_tokens=2048, # maximum tokens to generate, can change
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
        
        if not self.set_model():
            return
        
        code = self.get_context()
        if not code:
            return

        messages = [
            {
                "role": "system", 
                "content": "You are an expert technical writer. Create a professional, clear, and comprehensive README.md."
            },
            {
                "role": "user", 
                "content": (
                    f"Generate a README.md file for the following project codebase:\n\n{code}\n\n"
                    "The README should include a project overview, installation instructions, "
                    "usage examples, and a summary of the project structure. Do not include the thinking process in the README, just the final output."
                )
            }
        ]

        try:
            response = llm.chat(
                model=self.model_name, 
                messages=messages, 
                options=self.options
            )
            
            readme_text = response.message.content
            clean_content = re.sub(r'<think>.*?</think>', '', readme_text, flags=re.DOTALL).strip()
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(clean_content)
                        
        except Exception as e:
            print(f"An error occurred during README generation: {e}")

    def get_context(self):
        context = ""
        file_endings = ('.py', '.js', '.java', '.cpp', '.c', '.rb', '.go', '.ts',
                        '.html', '.css', '.json', '.xml', '.sh', '.md', '.h', '.hpp')
        
        for root, dirs, files in os.walk('.'):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in IGNORED_DIRS]
            
            for file in files:
                if file.endswith(file_endings):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            context += f"\n--- FILE: {file_path} ---\n"
                            context += f.read()
                    except Exception as e:
                        print(f"Could not read {file_path}: {e}")
                        
        return context
        
        
        
## some helper functions to manually check conditions

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
