"""Bill payment service"""

from typing import List, Optional
from ...models.bills import (
     BillResponseDto,AirtimePurchaseDto,DataPurchaseDto,ElectricityPaymentDto,CableTvPaymentDto
    
)

class BillPayService:
    """Pay Service for bill payment operations""" 
    def __init__(self, client):
        self.client = client
       
    
    async def buy_airtime(self, request: AirtimePurchaseDto) -> BillResponseDto:
        """Buy airtime"""
        response = await self.client._request(
            "POST", "/bills/pay/airtime", data=request.dict()
        )
        #return BillPaymentDto(**response['data'])
        return response
    
    async def buy_mobile_data(self, request: DataPurchaseDto) -> BillResponseDto:
        """Buy mobile data"""
        response = await self.client._request(
            "POST", "/bills/pay/data", data=request.dict()
        )
        #return BillPaymentDto(**response['data'])
        return response
    
    async def buy_electricity(self, request: ElectricityPaymentDto) -> BillResponseDto:
        """Pay electricity bill"""
        response = await self.client._request(
            "POST", "/bills/pay/electricity", data=request.dict()
        )
        #return BillPaymentDto(**response['data'])
        return response
    
    async def subscribe_cable_tv(self, request: CableTvPaymentDto) -> BillResponseDto:
        """Subscribe to cable TV"""
        response = await self.client._request(
            "POST", "/bills/pay/cable-tv", data=request.dict()
        )
        #return BillPaymentDto(**response['data'])
        return response
    
   