import openai


def requestGpt(api_key, prompt):
    """
    Generate a paragraph using OpenAI's GPT model.
    Args:
        api_key: OpenAI API key.
        prompt: Formatted prompt for the model.
    Returns:
        Generated paragraph as a string.
    """

    client = openai.OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    message = completion.choices[0].message.content.strip()

    print(message)

    return message
