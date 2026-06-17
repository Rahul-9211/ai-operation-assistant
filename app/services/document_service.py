from typing import Any


from fastapi import UploadFile
from pypdf import PdfReader

from app.services.chunking import ChunkingService
from app.services.embedding_service import EmbeddingService
from app.services.json_service import JsonService
from app.services.tiktoken import TiktokenService

class Document:
    def extract_character(self, file : UploadFile):
        reader = PdfReader(file.file)
      
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        chunked_data = ChunkingService().create_chunk(text, 100);
        embedding_service = EmbeddingService();
        document_list = []

        for idx, chunk in enumerate[Any](chunked_data):
            embedding = embedding_service.create_embedding(chunk)

            document_list.append({
                "id" : idx,
                "chunk" : chunk,
                "embedding" : embedding
            })

        # print("embedding->",  embedding)
        save_json_service = JsonService();
        save_json_service._save("game", document_list)
        return {
            "filename": file.filename,
            "pages": len(reader.pages),
            # "characters": len(text),
            # "preview": text,  
            "embedding_len":len(embedding),
            "chunk[0]" : chunked_data[1],
            "chunklength_character": len(chunked_data[1]),
            "chunklength_word": len(chunked_data[1].split()),
            "token_used": TiktokenService().get_token_count(chunked_data[1])
        }


