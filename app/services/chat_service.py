import json
import numpy as np

from app.services import document_service
from app.services.embedding_service import EmbeddingService
from app.services.openAI import OpenAIService

embedding_service  = EmbeddingService()
class ChatService:
    def _chat(self, message : str):
        question_embedding = embedding_service.create_embedding(message)
        question_embedding = np.array(question_embedding, dtype=np.float32)
        with open("game.json", "r") as f:
            documents = json.load(f)
        context =  embedding_service.compare_embedding(question_embedding , documents)
        openAi_service = OpenAIService();
        print("question->", message)
        return openAi_service.call_model(message, context)

            
