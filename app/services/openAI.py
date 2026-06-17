from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

class OpenAIService:

    def call_model(
        self,
        message: str,
        context: str | None = None
    ):

        messages = []

        if context:
            messages.append({
                "role": "system",
                "content": f"""
                Answer only from the provided context.

                Context:
                {context}
                """
            })

        messages.append({
            "role": "user",
            "content": message
        })

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        print("context->", context)
        return {
            "request": message,
            "response_body": response.choices[0].message.content
        }