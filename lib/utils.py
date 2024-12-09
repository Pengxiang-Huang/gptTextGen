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


def contact_prompts(prompt_data):
    """ Contact prompts from json data to a string """
    """ keys are dropped, only contact values """
    try:
        prompt_values = list(prompt_data.values())
        contacted_prompt = [", ".join(v) if isinstance(v, list)
                            else v for v in prompt_values]
        formatted_prompt = " ".join(contacted_prompt)
        return formatted_prompt
    except Exception as e:
        raise ValueError(f"Invalid json format in prompt data: {e}.")


def read_content(file_path):
    """ Read the paragraph content from the output dir """
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Paragraph file '{file_path}' not found.")
    except Exception as e:
        raise IOError(f"Error reading from file '{file_path}': {e}")
