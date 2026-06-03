from random import choice
from app.core.config import OPENAI_API_KEY
from openai import OpenAI  # pyright: ignore[reportMissingImports]

client = OpenAI(api_key=OPENAI_API_KEY);

class OpenAIService:
    def callModal( self, message: str):

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )
        return {
            "request" : message, 
            "response_body" : response.choices[0].message.content
        }