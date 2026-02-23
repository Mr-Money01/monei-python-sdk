""""""

from typing import Dict, Any, List, Optional
from ..models.business import (
    CreateCustomerDto,UpdateCustomerDto
)
from ..exceptions import MoneiAPIError


class BusinessService:
    """Service for customer busineess operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def create_business_customer(self, business_id: str, request:CreateCustomerDto) -> Dict:
        """"""        
        response = await self.client._request("POST", f"/customers/{business_id}", data=request.dict())
        return response
    
    async def get_business_customers(self, business_id: str) -> Dict:
        """"""
       
        response = await self.client._request(
            "GET", f"/customers/{business_id}"
        )
        return response
    
    async def get_customer_details(self, business_id: str, customer_id: str) -> Dict:
        """"""
       
        response = await self.client._request(
            "GET", f"/customers/{business_id}/{customer_id}"
        )
        return response
    
    
    async def update_customer(self, business_id: str,customer_id: str, request:UpdateCustomerDto) -> Dict:
        """"""
        
        response = await self.client._request(
            "PATCH", f"/customers/{business_id}/{customer_id}", data=request.dict()
        )
        return response
    
    async def disable_customer(self, business_id: str,customer_id: str) -> Dict:
        """"""
        
        response = await self.client._request(
            "PATCH", f"/customers/{business_id}/{customer_id}"
        )
        return response
