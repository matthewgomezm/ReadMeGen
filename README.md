## Project Overview

This project provides a Python script that generates a README.md file for a codebase using the Ollama AI model. The script analyzes the project's source files, collects their contents, and leverages an LLM to create a professional, comprehensive README.md. The generated README includes a project overview, installation instructions, usage examples, and a summary of the project structure.

---

## Features

- **Automated README Generation**: Uses Ollama to generate a well-structured README.md based on the project's code.
- **Project Analysis**: Scans the codebase for relevant files (e.g., `.py`, `.js`, `.md`) and includes their contents in the prompt.
- **Customizable**: Easily extendable to support additional file types or model configurations.

---

## Installation

### Prerequisites

1. **Python 3.8+**: Ensure Python is installed on your system.
2. **Ollama**: Install the Ollama server and a model of your choice (e.g., `llama3`).
   - [Ollama Installation Guide](https://ollama.com/download)

### Install Dependencies

```bash
pip install ollama
```

---

## Usage

### Step 1: Ensure Ollama is Running

Start the Ollama server:

```bash
ollama run
```

### Step 2: Run the Script

Execute the main script to generate the README:

```bash
python main.py
```

This will create a `README.md` file in the current directory, containing the generated documentation.

---

## Project Structure

The project consists of the following files:

- **`generate.py`**: Core script that:
  - Walks the project directory.
  - Collects relevant file contents.
  - Uses Ollama to generate the README.md.

- **`main.py`**: Entry point that initializes and runs the `generate.py` script.

---

## Contribution

Feel free to extend the script to support additional file types, models, or customization options. Contributions are welcome!

---

**This is the product of the AI ReadMe with Local LLM. I personally ran it on M4 Pro Apple Silicon, with Qwen_Qwen3-8B pulled from Hugging Face. Very cool!**
**Working on shell scripting to extend functionality.**
