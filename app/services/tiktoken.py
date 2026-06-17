import tiktoken

class TiktokenService:
    def get_token_count(self, text : str):
        encoded_token = tiktoken.encoding_for_model("gpt-4o")
        return len(encoded_token.encode(text))