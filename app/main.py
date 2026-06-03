from app.classes.identity import Identity  # pyright: ignore[reportMissingImports]
from app.classes.openAI import ChatRequest, ChatResponse
from app.services.identity import IdentityService
from app.services.openAI import OpenAIService
from fastapi import FastAPI  # pyright: ignore[reportMissingImports]
app = FastAPI()

@app.post("/")
def read_root(request: Identity):
    identity_service = IdentityService()
    return identity_service.create_identity(request);   

# @app.get("/test")
# async def test(request: {string}):
#     return {"message": "Hello, World!sss 2"}

@app.post("/chat")
async def chat(request: ChatRequest , response_body =  ChatResponse):
    openai_service = OpenAIService()
    return openai_service.callModal(request.message);
