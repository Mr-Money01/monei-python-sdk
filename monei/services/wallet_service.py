"""Wallet service implementation"""

from typing import Dict, Any, List, Optional
from ..models.wallet import (
    FundwalletResponseDto, UserWalletDto, FundWalletByNairaDto, DepositResponseDto, VerifyBankResponseDto,
    WithdrawWalletDto, PeerTransferDto, BankAccountResponseDto,
    VerifyBankAccountRequestDto
)
from ..exceptions import MoneiAPIError


class WalletService:
    """Service for wallet operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_wallet(self, chain_id: Optional[int] = None) -> UserWalletDto:
        """Get wallet information"""
        params = {}
        if chain_id:
            params['chainId'] = chain_id
            
        response = await self.client._request("GET", "/wallet/me", params=params)
        return UserWalletDto(**response)
    
    async def fund_wallet(self, amount: float) -> FundwalletResponseDto:
        """Fund wallet with Naira"""
        request_data = FundWalletByNairaDto(amount=amount)
        response = await self.client._request(
            "POST", "/wallet/user/fund-wallet", data=request_data.dict()
        )
        return FundwalletResponseDto(**response)
    
    async def withdraw_to_bank(self, request: WithdrawWalletDto) -> Dict[str, Any]:
        """Withdraw to bank account"""
        response = await self.client._request(
            "POST", "/wallet/withdrawals", data=request.dict()
        )
        return response
    
    async def peer_transfer(self, request: PeerTransferDto) -> Dict[str, Any]:
        """Transfer to another user"""
        response = await self.client._request(
            "POST", "/wallet/peer-transfer", data=request.dict()
        )
        return response
    
    async def get_banks(self) -> BankAccountResponseDto:
        """Get available banks"""
        response = await self.client._request("GET", "/wallet/get-banks")

        #banks = response["data"]
        #return [BankDto(**bank) for bank in banks]
        return BankAccountResponseDto(**response)
    
    async def verify_bank_account(self, account_number: str, bank: str) -> VerifyBankResponseDto:
        """Verify bank account"""
        request_data = VerifyBankAccountRequestDto(
            accountNumber=account_number, bank=bank
        )
        response = await self.client._request(
            "POST", "/wallet/verify-bank-account", data=request_data.dict()
        )
        
        return VerifyBankResponseDto(**response)