
import pandas as pd 
import requests
from datetime import datetime
from pprint import pprint
import tiktoken
from pypdf import PdfReader
from IPython.display import Markdown, display
import os
from matplotlib import pyplot, image
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

print(client)
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     model="gpt-4o",
# )