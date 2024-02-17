import os

from dotenv import load_dotenv

load_dotenv()

gpt_openai_api_key = os.getenv("OPENAI_API_KEY")
