import os
from typing import List, Union

from dotenv import find_dotenv, load_dotenv
from openai import AzureOpenAI

_ = load_dotenv(find_dotenv('.env'))
_ = load_dotenv(find_dotenv('.secrets'))

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
    api_version=os.getenv("AZURE_OPENAI_VERSION", "2023-12-01-preview"),
)

def get_completion(prompt: Union[str, List], *, temperature=0.3, model="gpt-4-32k", timeout=30):
    """
    Generates a completion using the OpenAI chat model.

    Args:
        prompt (Union[str, List]): The prompt or list of messages to generate completion from.
        temperature (float, optional): Controls the randomness of the output. Defaults to 0.3.
        model (str, optional): The name of the model to use. Defaults to "gpt-4-32k".
        timeout (int, optional): The maximum time in seconds to wait for the completion. Defaults to 30.

    Returns:
        str: The generated completion message.
    """
    if isinstance(prompt, str):
        messages = [{"role": "user", "content": prompt}]
    else:
        messages = prompt
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=messages, # type: ignore
            temperature=temperature,
            timeout=timeout
        )  # type: ignore
        message = completion.choices[0].message.content
        return message
    except Exception as e:
        print(e)
        return "Sorry, I couldn't understand that or an timeout or error occurred. Please try again."

ask = get_completion