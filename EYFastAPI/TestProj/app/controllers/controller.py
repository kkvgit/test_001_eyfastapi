import logging
from typing import List
from fastapi import APIRouter, HTTPException
from models.addition import AddRequest, AddResponse
from multiprocessing import Pool
import datetime

router = APIRouter()

logger = logging.getLogger(__name__)

def add_list(list_numbers: List[int]) -> List[int]:
    return sum(list_numbers)

@router.post("/add/", response_model=AddResponse)
async def perform_addition(request: AddRequest):
    try:
        
        started_at = datetime.datetime.now()
        with Pool() as pool:
            result = pool.map(add_list, request.payload)        
        completed_at = datetime.datetime.now()

        response_data = {"batchid":request.batchID,
                         "response":result,
                         "status":"complete",
                         "started_at": str(started_at), 
                         "completed_at": str(completed_at)}
        return response_data
    except Exception as e:
        logger.exception(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
