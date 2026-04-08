"""Bill payment service"""

from typing import List, Optional
from ...models.bills import (
     ValidateBillDto
    
)

class BillValidationService:
    """Validation Service for bill payment operations"""
    
    def __init__(self, client):
        self.client = client
    
   
    async def validate(self, request:ValidateBillDto) -> dict:
        """Validate bill information"""
       
        response = await self.client._request(
            "POST", "/bills/validation/customer", data=request.dict()
        )
        return response
    
    