from typing import Any
from aiogram.filters import Filter
from aiogram.types import Message,ContentType


class Voice(Filter):
        
    async def __call__(self, message: Message) -> bool:
        return message.content_type == ContentType.VOICE
 
        
class Checker(Filter):
    
    def __init__(self,id:int):
        self.id = id
         
    async def __call__(self,  message:Message) -> bool:
        return message.message_id-1 == self.id