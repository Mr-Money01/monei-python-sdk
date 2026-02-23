import os
import pytest
import logging
from monei.models.wallet import InitiateBankTransferDto,PeerTransferDto

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestWalletPayoutsService:

    @pytest.fixture(autouse=True)
    async def _setup(self, wallet_payouts_service):
        self.client = wallet_payouts_service
        
        self.test_bank_account = os.getenv("TEST_BANK_ACCOUNT")
        self.test_bank = os.getenv("TEST_BANK")
        

    async def test_bank_transfer(self):
        request = InitiateBankTransferDto(
            amount= 100,
            bank='',
            accountNumber='',
            transactionPin='',
            reference='',
            narration='',
            meta={}

        )
        response = await self.client.wallet.bank_transfer(request)
        logger.info(f"Bank Transfer: {response}")
        

    @pytest.mark.skipif(
        not os.getenv("ENABLE_SOL_SWAP_TESTS"),
        reason="Solana swap tests disabled"
    )
    async def test_peer_transfer(self):
        request = PeerTransferDto(
            receiver='',
            amount=100,
            transactionPin='',
            currency='NGN'
            
        )
        response = await self.client.wallet.peer_transfer(request)
        logger.info(f"peer Transfer: {response}")
        assert hasattr(response, 'link')

   
 