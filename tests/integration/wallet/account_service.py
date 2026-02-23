import os
import pytest
import logging
from monei.models.wallet import CreateVirtualAccountDto

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestWalletService:

    @pytest.fixture(autouse=True)
    async def _setup(self, wallet_account_service):
        self.client = wallet_account_service
        
        
    async def test_get_wallet(self):
        chain_id = "1"
        response = await self.client.wallet.get_wallet(chain_id)
        logger.info(f"Wallet info: {response}")
        #assert hasattr(wallet, "nairaBalance")

    async def test_naira_wallet(self):
        response = await self.client.wallet.get_wallet()
        logger.info(f"Naira Wallet info: {response}")
        #assert hasattr(wallet, "nairaBalance")
    

    async def test_create_virtual_account(self):
        request = CreateVirtualAccountDto(
            nin = "1234567123",
            reference = "ref-001"

        )
        response = await self.client.wallet.get_wallet(request)
        logger.info(f"Virtual Account: {response}")
      
    

    