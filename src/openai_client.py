import openai
from config.settings import OPENAI_API_KEY, DEFAULT_MODEL, TEMPERATURE, MAX_TOKENS

class OpenAIClient:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def send_message(self, prompt, model=DEFAULT_MODEL, temperature=TEMPERATURE,
                     max_tokens=MAX_TOKENS):
        pass