import openai 

import json 


API_KEY_FILE = "key.txt"


def load_api_key(file_path = API_KEY_FILE):
    "loading key from OPENAI path"
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"API key file '{file_path}' not found.")

def write_to_file(file_path, content):
    """Write content to a file."""
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except Exception as e:
        raise IOError(f"Error writing to file '{file_path}': {e}")
