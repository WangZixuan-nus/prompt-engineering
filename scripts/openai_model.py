from openai import OpenAI
from dotenv import load_dotenv

def __init__(self, model="gpt-4.1"):
    # Get API key from environment variable
    self.api_key = os.getenv("API_KEY") 

    if not self.api_key:
        print("ERROR: API_KEY not found in environment")
        raise ValueError(
            "API_KEY environment variable not set. "
            "Ensure it's in your .env file and load_dotenv() was called."
        )
    openai.api_key = self.api_key
    self.client = openai.OpenAI(api_key=self.api_key)
    self.model = model
