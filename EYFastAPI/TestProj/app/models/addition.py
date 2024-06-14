from pydantic import BaseModel
from typing import List

class AddRequest(BaseModel):
    batchID: str
    payload: List[List[int]]

class AddResponse(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: str
    completed_at: str
    
    
