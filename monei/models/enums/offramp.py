"""Offramp related enums"""
from enum import Enum


class OfframpStatus(str, Enum):
    initiated = "initiated"
    quote_created = "quote_created"
    awaiting_deposit = "awaiting_deposit"
    deposit_received = "deposit_received"
    pending = "pending"
    processing = "processing"
    fiat_sent = "fiat_sent"
    completed = "completed"
    failed = "failed"
    cancelled = "cancelled"
    refunded = "refunded"
    expired = "expired"

class Providers(str, Enum):
    monirates= "monirates"
    bitnob = "bitnob"
    paycrest = "paycrest"

class OfframpAssets(str, Enum):
    USDT = "USDT"
    USDC = "USDC"
    CNGN = "CNGN"

class OfframpNetworks(str, Enum):
    base = "base"
    polygon = "polygon"
    arbitrum_one = "arbitrum-one"
    bnb_smart_chain= "bnb-smart-chain"
    ethereum = "ethereum"
    starknet = "starknet"
    optimism= "optimism"
    lisk = "lisk"
    scroll = "scroll"

class OfframpCurrency(str, Enum):
    NGN = "NGN"
    GHS = "GHS"
    KES = "KES"
    USD = "USD"
  
class WalletType(str, Enum):
    MONEI_WALLET = "MONEI_WALLET"
    EXTERNAL_WALLET = "EXTERNAL_WALLET"
    
    


    
