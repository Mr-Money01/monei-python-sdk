"""Bill payment service"""

from typing import List, Optional
from ...models.bills import (
    
    BillHistoryResponseDto, BillResponseDto, TransactionResponseDto
)



class BillRecordsService:
    """Records Services for bill operations"""
    
    def __init__(self, client):
        self.client = client
    
   
    async def get_bills(self) -> BillHistoryResponseDto:
        """Get bill payment history"""
        response = await self.client._request("GET", "/bills/records")
        #return [BillDto(**bill) for bill in response['data']]
        return BillHistoryResponseDto(**response)
    
    async def get_bill_by_reference(self, reference: str) -> BillResponseDto:
        """Get bill payment history"""
        response = await self.client._request("GET", f"/bills/records/reference/{reference}")
        #return [BillDto(**bill) for bill in response['data']]
        return BillResponseDto(**response)
    
    async def generate_receipt(self, transaction_id: str) -> TransactionResponseDto:
        """Get bill payment history"""
        response = await self.client._request("GET", f"/bills/records/receipt/{transaction_id}")
        #return [BillDto(**bill) for bill in response['data']]
        return TransactionResponseDto(**response)
    
    
