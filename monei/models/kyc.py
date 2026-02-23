"""Kyc Verification related models"""

from typing import Optional,Dict,Any
from enum import Enum
from .base import BaseDto
from pydantic import BaseModel
from .enums.kyc import (
   KycDocType, KycTier
)
from .wallet import VirtualAccountDto



class TierLimitsData(BaseModel):
    maxSingleTransaction:int
    dailyTransactionLimit:int
    monthlyTransactionLimit:int
    maxWalletBalance:int
    cryptoAllowed:bool
    crossBorderAllowed:bool
    cryptoDailyLimit:int
    p2pAllowed:bool
    withdrawalAllowed:bool




class KycStatusData(BaseModel):
    """kyc status response model"""
    currentTier: KycTier
    status: str
    limits:TierLimitsData
    requirements:str
    verified: VerificationStatusData
    canUpgrade:bool
    nextTier:KycTier


class KycStatusResponseDto(BaseModel):
    """kyc status response model"""
    statusCode: str
    message: str
    data: KycStatusData
    errors:Optional[Dict[str, Any]] = None

class VerificationStatusData(BaseDto):
    nin:bool
    bvn:bool
    governmentId:bool
    selfie:bool
    biometric:bool
    address:bool


class SubmitNinDto(BaseModel):
    nin: str

class NinVerificationData(BaseModel):
    tier: KycTier
    ninVerified:bool
    verifiedAt:str
    newLimits:TierLimitsData
    virtualAccount: VirtualAccountDto



class NinVerificationResponseDto(BaseModel):
    """nin verification response model"""
    statusCode: str
    message: str
    data: NinVerificationData
    errors:Optional[Dict[str, Any]] = None

class SubmitBvnDto(BaseModel):
    bvn:str

class BvnVerificationResponseDto(BaseModel):
    """submit bvn response model"""
    statusCode: str
    message: str
    data: Dict[str, Any]
    errors:Optional[Dict[str, Any]] = None

class DocumentUploadResponseDto(BaseModel):
    """upload document response model"""
    statusCode: str
    message: str
    data: Dict[str, Any]
    errors:Optional[Dict[str, Any]] = None

class EligibilityCheckResponseDto(BaseModel):
    """eligibility response model"""
    statusCode: str
    message: str
    data: Dict[str, Any]
    errors:Optional[Dict[str, Any]] = None

class CheckTierEligibilityDto(BaseModel):
    """eligibility request model"""
    targetTier: KycTier

class LimitResponseDto(BaseModel):
    """Get limit response model"""
    statusCode: str
    message: str
    data: Dict[str, Any]
    errors:Optional[Dict[str, Any]] = None

class UploadDocumentDto(BaseModel):
    documentType: KycDocType
    documentUrl: str
    documentNumber: str