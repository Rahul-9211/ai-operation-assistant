import json
from app.services.openAI import client
import numpy  as np



class EmbeddingService:
    def create_embedding(self, text: str):
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding
    
    def compare_embedding(self, question_embedding : str , comparsion_doc : []):
        best_score = -1;
        best_chunk = "";
        for doc in comparsion_doc:
            doc_embedding = np.array(doc["embedding"], dtype=np.float32)
            doc_chunk =  np.array(doc["chunk"])
            score = np.dot(question_embedding, doc_embedding)/(np.linalg.norm(question_embedding)* np.linalg.norm(doc_embedding))
            if score > best_score:
                best_score = score
                best_chunk = doc_chunk
        
        return best_chunk


   

        
