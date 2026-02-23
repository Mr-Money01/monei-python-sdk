"""Kyc Verification related enums"""
from enum import Enum


class KycDocType(str, Enum):
    nin = "nin"
    bvn = "bvn"
    voters_card = "voters_card"
    drivers_license = "drivers_license"
    international_passport = "international_passport"
    selfie = "selfie"
    utility_bill = "utility_bill"
    bank_statement = "bank_statement"

class KycTier(str, Enum):
    tier_1 = "tier_1"
    tier_2 = "tier_2"
    tier_3 = "tier_3"
    tier_4 = "tier_4"
    
