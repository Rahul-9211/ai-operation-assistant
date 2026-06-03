from asyncio import streams
from pydantic import BaseModel

class Identity(BaseModel):
    name: str
    email: str
    phone: str
    address:str