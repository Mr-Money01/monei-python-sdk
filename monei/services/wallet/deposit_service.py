"""Wallet service implementation"""

from typing import Dict, Any, List, Optional
from ...models.wallet import (
    DepositDto,DepositAuthDto, DepositWithPaymentMethodResponseDto,PaymentResponseDto,StatusResponseDto,DepositWithPaymentMethodDto,DepositAuthResponseDto,GeneratePaymentLinkDto,PaymentLinkResponseDto,
)
from ...models.enums.wallet import DepositMethods
from ...exceptions import MoneiAPIError


class WalletDepositService:
    """Deposit Service for wallet operations"""
    
    def __init__(self, client):
        self.client = client


    async def initialize(self, method:DepositMethods , request: DepositDto ) -> PaymentResponseDto:  

        params = {'method': method.value}
        response = await self.client._request("POST", "/wallet/deposit", data=request.dict(), params = params)
        return PaymentResponseDto(**response)
    

    
    async def with_payment_method(self, request:DepositWithPaymentMethodDto)-> PaymentResponseDto:

        """create a payment method for user"""
            
        response = await self.client._request("POST", "/wallet/deposit/payment-method", data=request.dict())
        return DepositWithPaymentMethodResponseDto(**response)
    
    async def authorize(self, request: DepositAuthDto) -> DepositAuthResponseDto:
        """Authorize a pending charge"""
        
        response = await self.client._request(
            "POST", "/wallet/deposit/authorize", data=request.dict()
        )
        return response
    
    async def generate_payment_link(self, request: GeneratePaymentLinkDto) -> PaymentLinkResponseDto:
        """"""
        response = await self.client._request(
            "POST", "/wallet/deposit/payment-link", data=request.dict()
        )
        return PaymentLinkResponseDto(**response)
    
    async def get_status(self, reference:str) -> StatusResponseDto:
        """"""
        response = await self.client._request(
            "GET", f"/wallet/deposit/status/{reference}", 
        )
        return StatusResponseDto(**response)
    