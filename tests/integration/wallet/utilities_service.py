import os
import pytest
import logging
from monei.models.wallet import VerifyBankAccountRequestDto

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestWalletUtilityService:

    @pytest.fixture(autouse=True)
    async def _setup(self, wallet_utility_service):
        self.client = wallet_utility_service
        
        self.test_bank_account = os.getenv("TEST_BANK_ACCOUNT")
        self.test_bank = os.getenv("TEST_BANK")
        

 
    async def test_get_banks(self):
        response = await self.client.wallet.get_banks()
        logger.info(f"Banks: {response}")
       

    
    async def test_verify_bank_account(self):
        request = VerifyBankAccountRequestDto(
            accountNumber='',
            bank=''
            
        )
        bank_account = await self.client.wallet.verify_bank_account(request)
        logger.info(f"Verified bank account: {bank_account}")
        
