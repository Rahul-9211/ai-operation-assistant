from dotenv import load_dotenv # pyright: ignore[reportMissingImports]
import os

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))