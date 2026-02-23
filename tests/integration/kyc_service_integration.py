import os
import pytest
import logging
from monei.models.kyc import KycStatusResponseDto,CheckTierEligibilityDto,SubmitNinDto,NinVerificationResponseDto,LimitResponseDto,SubmitBvnDto,BvnVerificationResponseDto,DocumentUploadResponseDto,EligibilityCheckResponseDto,CheckTierEligibilityDto,UploadDocumentDto
from monei.models.enums.kyc import KycTier

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestKycService:

    @pytest.fixture(autouse=True)
    async def _setup(self, kyc_service):
        self.client = kyc_service
        

    async def test_get_kyc_status(self):
        convs = await self.client.get_kyc_status()

        logger.info(f"Conversations: {convs}")
        

    async def test_submit_nin(self):
        request = SubmitNinDto(
            nin='12345678991'
        )
        nin_response = await self.client.submit_nin(request)
        logger.info(f"submit_nin: {nin_response}")
        

    # ---------------- Chat endpoints ---------------- #

    
    async def test_submit_bvn(self):
        request = SubmitBvnDto(
            bvn='12345678991'
        )
        response = await self.client.submit_bvn(request)
        logger.info(f"submit bvn: {response}")
        #assert hasattr(response, "message")

    # ---------------- Conversation management ---------------- #

    
    async def test_upload_document(self):
        
        request = UploadDocumentDto(

            documentNumber='1112244678',
            documentType='voters_card',
            documentUrl="https://s3.amazonaws.com/bucket/documents/user-id-front.jpg"
        )
        init_response = await self.client.upload_document(request)
        logger.info(f"Initialized conversation: {init_response}")
        

    

    
    async def test_check_eligibility(self):
        request=CheckTierEligibilityDto(
            targetTier = "tier_1"

        )
        

        messages = await self.client.check_eligibility(request)
        logger.info(f"Messages: {messages}")
    

        
      
        
   
    async def test_get_limits(self):
        
        #initialize first then stream
        response = await self.client.get_limits()
        logger.info(f"Stream chat response: {response}")
        assert isinstance(response, dict)


