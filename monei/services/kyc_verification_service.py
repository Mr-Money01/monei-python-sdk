"""Kyc Verification service implementation"""

from typing import Dict, Any, List, Optional
from ..models.kyc import (
    KycStatusResponseDto,SubmitNinDto,NinVerificationResponseDto,LimitResponseDto,SubmitBvnDto,BvnVerificationResponseDto,DocumentUploadResponseDto,EligibilityCheckResponseDto,CheckTierEligibilityDto,UploadDocumentDto
)
from ..models.enums.kyc import KycTier
from ..exceptions import MoneiAPIError


class KycVerificationService:
    """Service for kyc verification operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_kyc_status(self) -> KycStatusResponseDto:
        """Get kyc status"""
          
        response = await self.client._request("GET", "/kyc/status")
        return response
    
    async def submit_nin(self, request: SubmitNinDto ) -> NinVerificationResponseDto:
        """submit nin for verification"""
       
        response = await self.client._request(
            "POST", "/kyc/submit-nin", data=request.dict()
        )
        return response
    
    async def submit_bvn(self, request:SubmitBvnDto ) -> BvnVerificationResponseDto:
        """submit bvn for verification"""
       
        response = await self.client._request(
            "POST", "/kyc/submit-bvn", data=request.dict()
        )
        return response
    
    
    async def upload_document(self, request: UploadDocumentDto) -> DocumentUploadResponseDto:
        
        """Upload a document"""
        
        response = await self.client._request(
            "POST", "/kyc/upload-document", data=request.dict()
        )
        return response
    
    async def check_eligibility(self, request:KycTier) -> EligibilityCheckResponseDto:

        """check user eligibility status"""
        response = await self.client._request(
            "POST", "/kyc/check-eligibility", data=request.dict()
        )
        return response
    
    async def get_limits(self) -> LimitResponseDto:

        """Get users limit"""     
        response = await self.client._request("GET", "/kyc/limits")
        return response
   