"""Bill payment service"""

from typing import List, Optional
from ...models.bills import (
    ElectricityBillerResponseDto,BillCategory,ElectricityBillerResponseDto,BillerItemsResponse
)

class BillDiscoveryService:
    """Discovery Service for bill payment operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_biller(self, category: BillCategory, biller_name: str) -> BillerItemsResponse:
        """Get biller items"""
        response = await self.client._request(
            "GET", f"/bills/get-biller-items/{category.value}/{biller_name}"
        )
        #return [BillerDto(**item) for item in response['data']]
        return response

    async def get_electricity_biller(self) -> ElectricityBillerResponseDto:
        """Get all electricity distribution companies"""
        response = await self.client._request(
            "GET", f"/bills/discovery/electricity-operators"
        )
        #return [ElectricityBillerDto(**item) for item in response['data']]
        return response
    
    