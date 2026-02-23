import os
import pytest
import logging
from monei.models.wallet import WithdrawWalletDto, PeerTransferDto

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestWalletService:

    @pytest.fixture(autouse=True)
    async def _setup(self, monei_client):
        self.client = monei_client
        
        self.test_bank_account = os.getenv("TEST_BANK_ACCOUNT")
        self.test_bank = os.getenv("TEST_BANK")
        

    async def test_get_wallet(self):
        wallet = await self.client.wallet.get_wallet()
        logger.info(f"Wallet info: {wallet}")
        #assert hasattr(wallet, "nairaBalance")

    @pytest.mark.skipif(
        not os.getenv("ENABLE_SOL_SWAP_TESTS"),
        reason="Solana swap tests disabled"
    )
    async def test_fund_wallet(self):
        response = await self.client.wallet.fund_wallet(100.0)
        logger.info(f"Fund wallet response: {response}")
        assert hasattr(response, 'link')

    @pytest.mark.skipif(
        not os.getenv("ENABLE_SOL_SWAP_TESTS"),
        reason="Solana swap tests disabled"
    )
    async def test_withdraw_to_bank(self):
        request = WithdrawWalletDto(
            amount=100,
            accountNumber=self.test_bank_account,
            bank=self.test_bank,
            transactionPin="0990",
            currency="NGN",
            reference="Test withdrawal",
            narration="Withdrawal for testing"
        )
        response = await self.client.wallet.withdraw_to_bank(request)
        logger.info(f"Withdraw response: {response}")
        assert "data" in response
        assert "message" in response
        assert "statusCode" in response


    async def test_get_banks(self):
        banks = await self.client.wallet.get_banks()
        logger.info(f"Banks: {banks}")
        #assert isinstance(banks, list)
        #assert len(banks) > 0
        #assert hasattr(banks[0], "name")

    
    async def test_verify_bank_account(self):
        bank_account = await self.client.wallet.verify_bank_account(
            self.test_bank_account,
            self.test_bank
        )
        logger.info(f"Verified bank account: {bank_account}")
        #assert bank_account.accountNumber == self.test_bank_account
