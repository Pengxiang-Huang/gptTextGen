import os
import logging
from lib.request import requestGpt
from lib.utils import load_api_key, load_json, write_to_file, \
     contact_prompts, read_content

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


def genParagraph(api_key):
    """ Generate a paragraph based on prompts, redirect to the output dir"""
    prompt_path = f"{INPUT_PROMPT_FOLDER}gen.json"
    prompt_data = load_json(prompt_path)

    # Format the prompt (remove the keys, conjunct the values)
    formatted_prompts = contact_prompts(prompt_data)

    print(f"\nRequest for Paragraph generation is: {formatted_prompts}")

    # Generate paragraph
    paragraph = requestGpt(api_key, formatted_prompts)
    logging.info(f"generate an paragraph: {paragraph}")

    # Save to output
    output_file = f"{OUTPUT_FOLDER}paragraph.txt"
    write_to_file(output_file, paragraph)
    logging.info(f"Paragraph generated and saved to: {output_file}")
    print(f"\nParagraph generated and saved to: {output_file}")

    return


def reviewParagraph(api_key):
    """ Review the paragraph in the output dir based on the prompts """
    prompt_path = f"{INPUT_PROMPT_FOLDER}review.json"
    prompt_data = load_json(prompt_path)

    # Format the prompt (remove the keys, conjunct the values)
    formatted_prompts = contact_prompts(prompt_data)
    print(f"\nRequest for Paragraph review is: {formatted_prompts}")

    # read the paragraph from the output dir
    paragraph_path = f"{OUTPUT_FOLDER}paragraph.txt"
    paragraph = read_content(paragraph_path)

    # contact the prompt with paragraph
    conjunction = "Below is the paragraph you need to review: "
    full_content = formatted_prompts + conjunction + paragraph

    # Review paragraph
    review = requestGpt(api_key, full_content)

    # Save to the output
    output_file = f"{OUTPUT_FOLDER}review.txt"
    write_to_file(output_file, review)
    logging.info(f"Review generated and saved to: {output_file}")
    print(f"\nReview generated and saved to: {output_file}")

    return


def reviewDocument(api_key, doc_name):
    """ review the document in the input dir based on the prompts """
    # TODO
    return


def main():
    try:
        # Load OpenAI API key
        api_key = load_api_key(f"{INPUT_FOLDER}openai_key.txt")
        logging.info("OpenAI API key loaded successfully.")

        # List available prompts
        prompts = list_prompts(INPUT_PROMPT_FOLDER)
        if not prompts:
            raise FileNotFoundError("No prompt files found in the \
                                     prompts/ folder.")

        print("Available Prompts:")
        for i, prompt_file in enumerate(prompts, start=1):
            print(f"{i}. {prompt_file}")

        genParagraph(api_key)

        reviewParagraph(api_key)

    except Exception as e:
        logging.error(f"Error: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
