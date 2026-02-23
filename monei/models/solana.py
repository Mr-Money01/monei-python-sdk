"""Solana wallet models"""

from typing import Optional, List
from enum import Enum
from .base import BaseModel

class SolanaNetwork(str, Enum):
    MAINNET_BETA = "mainnet-beta"
    DEVNET = "devnet"
    TESTNET = "testnet"

class BalanceDto(BaseModel):
    """Balance model"""
    balance: str

class AddressDto(BaseModel):
    """Wallet address"""
    address: str

class TokenInfoDto(BaseModel):
    """Token information"""
    mintAddress: str
    name: str
    symbol: str
    balance: float
    rawBalance: str
    decimals: int
    priceUsd: Optional[float] = None
    valueUsd: Optional[float] = None

class PortfolioDto(BaseModel):
    """Solana portfolio"""
    userId: str
    address: str
    nativeBalance: str
    nativeBalanceLamports: str
    nativeBalanceUsd: Optional[float] = None
    tokens: List[TokenInfoDto]
    totalValueUsd: Optional[float] = None

class TransferSolDto(BaseModel):
    """Transfer SOL request"""
    to: str
    amount: str
    network: Optional[SolanaNetwork] = SolanaNetwork.MAINNET_BETA

class TransferTokenDto(BaseModel):
    """Transfer SPL token request"""
    to: str
    tokenMintAddress: str
    amount: str
    network: Optional[SolanaNetwork] = SolanaNetwork.MAINNET_BETA

class SignatureDto(BaseModel):
    """Transaction signature"""
    signature: str