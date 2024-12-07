import os
import logging
from lib.request import requestGpt
from lib.utils import load_api_key, load_json, write_to_file

# Configure logging
LOG_FILE = "output/log.txt"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Paths
INPUT_PROMPT_FOLDER = "prompts/"
OUTPUT_FOLDER = "output/"
INPUT_FOLDER = "input/"


def list_prompts(folder):
    """List all JSON prompt files in the prompts folder."""
    try:
        return [file for file in os.listdir(folder) if file.endswith(".json")]
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt folder '{folder}' not found.")


def main():
    try:
        # Load OpenAI API key
        api_key = load_api_key(f"{INPUT_FOLDER}openai_key.txt")
        logging.info("OpenAI API key loaded successfully.")

        # List available prompts
        prompts = list_prompts(INPUT_PROMPT_FOLDER)
        if not prompts:
            raise FileNotFoundError("No prompt files found in the prompts/ folder.")

        print("Available Prompts:")
        for i, prompt_file in enumerate(prompts, start=1):
            print(f"{i}. {prompt_file}")
        prompt_choice = int(input("Select a prompt by number: ")) - 1

        # Ensure valid selection
        if prompt_choice < 0 or prompt_choice >= len(prompts):
            raise ValueError("Invalid prompt selection.")

        prompt_path = f"{INPUT_PROMPT_FOLDER}{prompts[prompt_choice]}"
        prompt_data = load_json(prompt_path)

        # User input for dynamic parts
        topic = input("Enter the topic for the paragraph: ").strip()
        formatted_prompt = prompt_data.get("template", "").format(input=topic)

        # Generate paragraph
        paragraph = requestGpt(api_key, formatted_prompt)
        logging.info(f"generate an paragraph: {paragraph}")

        # Save to output
        output_file = f"{OUTPUT_FOLDER}paragraph.txt"
        write_to_file(output_file, paragraph)
        logging.info(f"Paragraph generated and saved to: {output_file}")
        print(f"Paragraph generated and saved to: {output_file}")

    except Exception as e:
        logging.error(f"Error: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
