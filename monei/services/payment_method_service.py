"""Wallet service implementation"""

from typing import Dict, Any, List, Optional
from ..models.payment_method import (
    CreatePaymentMethodDto, PaymentMethodResponseDto,DeletePaymentMethodResponseDto,PaymentMethodsResponseDto
)
from ..exceptions import MoneiAPIError


class PaymentMethodService:
    """Service for payment method operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_all(self, sub_wallet_id: str) -> PaymentMethodsResponseDto:
        """"""
        params = {}
        if sub_wallet_id:
            params['sub_wallet_id'] = sub_wallet_id
            
        response = await self.client._request("GET", "/payment-methods", params=params)
        return PaymentMethodsResponseDto(**response)
    
    async def create(self, request:CreatePaymentMethodDto) -> PaymentMethodResponseDto:
        """Fund wallet with Naira"""
       
        response = await self.client._request(
            "POST", "/payment-methods", data=request.dict()
        )
        return PaymentMethodResponseDto(**response)
    
    
    async def set_default(self, id: str) -> PaymentMethodResponseDto:
        """Set default payment method"""
        params = {}
        if id:
            params['id'] = id
        response = await self.client._request(
            "PATCH", f"/payment-methods/{id}/default", params=params
        )
        return PaymentMethodResponseDto(**response)
    
    async def delete(self, id: str) -> DeletePaymentMethodResponseDto:
        """Delete a user payment method"""
        params = {}
        if id:
            params['id'] = id
        response = await self.client._request(
            "DELETE", f"/payment-methods/{id}", params=params
        )
        return DeletePaymentMethodResponseDto(**response)
    
    async def get(self, id:str) -> PaymentMethodResponseDto:
        """Get a payment method details using its id"""
        params = {}
        if id:
            params['id'] = id
        response = await self.client._request("GET", f"/payment-methods/{id}")

        #banks = response["data"]
        #return [BankDto(**bank) for bank in banks]
        return PaymentMethodResponseDto(**response)
   