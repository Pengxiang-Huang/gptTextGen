import json


def load_api_key(file_path):
    """Load OpenAI API key from a file."""
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"API key file '{file_path}' not found.")


def load_json(file_path):
    """Load JSON content from a file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file '{file_path}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file '{file_path}'.")


def write_to_file(file_path, content):
    """Write content to a file."""
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except Exception as e:
        raise IOError(f"Error writing to file '{file_path}': {e}")
