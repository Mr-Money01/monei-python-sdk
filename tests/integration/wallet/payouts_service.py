import os
import pytest
import logging
from monei.models.wallet import InitiateBankTransferDto,PeerTransferDto

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestWalletPayoutsService:

    @pytest.fixture(autouse=True)
    async def _setup(self, wallet_payout_service):
        self.client = wallet_payout_service
        self.pin = os.getenv("PIN")
        self.test_bank_account = os.getenv("TEST_BANK_ACCOUNT")
        self.test_bank = os.getenv("TEST_BANK")


    async def test_bank_transfer(self):
        request = InitiateBankTransferDto(
            amount= 400,
            bank='000',
            accountNumber='0736379044',
            transactionPin=self.pin,
            reference='bank-transfer-001',
            narration='',
            meta={}

        )
        response = await self.client.bank_transfer(request)
        logger.info(f"Bank Transfer: {response}")
        

   
    async def test_peer_transfer(self):
        request = PeerTransferDto(
            receiver='tobentra32@gmail.com',
            amount=100,
            transactionPin=self.pin,
            currency='NGN'
            
        )
        response = await self.client.peer_transfer(request)
        logger.info(f"peer Transfer: {response}")
        

   
 