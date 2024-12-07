import openai

OUTPUT_FILE = "output.txt"


def generate_paragraph(api_key, prompt):
    """Generate a paragraph using GPT"""
    openai.api_key = api_key

    try:
        # define the customization
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7  # randomness
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        raise RuntimeError(f"OpenAI API error: {e}")
