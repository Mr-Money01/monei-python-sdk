import os
import pytest
import logging
from decimal import Decimal
from monei.models.evm import SendNativeTokenDto, SendTokenDto

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration



@pytest.mark.asyncio
class TestEvmService:

    @pytest.fixture(autouse=True)
    async def _setup(self, evm_service):
        self.service = evm_service
        self.chain_id = 56  # Binance Smart Chain
        self.wallet_recipient = os.getenv("TEST_EVM_RECEIVER")
        self.token_address = os.getenv("EVM_TEST_TOKEN_ADDRESS")

   

    async def test_get_token_balance(self):
        token_address = "0x55d398326f99059fF775485246999027B3197955"  # DAI
        balance = await self.service.get_token_balance(token_address, self.chain_id)
        logger.info(f"Token balance: {balance}")
        #assert balance.balance is not None

    async def test_get_native_balance(self):
        balance = await self.service.get_native_balance(self.chain_id)
        logger.info(f"Native balance: {balance}")
        #assert balance.balance is not None

    async def test_get_portfolio(self):
        portfolio = await self.service.get_portfolio(self.chain_id)
        logger.info(f"Portfolio: {portfolio}")
        #assert portfolio is not None

    @pytest.mark.skipif(
        not os.getenv("ENABLE_BILL_PAYMENT_TESTS"),
        reason="Bill payment tests disabled"
    )


    async def test_send_native_token(self):
        request = SendNativeTokenDto(
            chainId=self.chain_id,
            to=self.wallet_recipient,
            amount="0.00001"
        )
        response = await self.service.send_native_token(request)
        logger.info(f"Send native TX response: {response}")
        assert hasattr(response, "txHash")

    

    @pytest.mark.skipif(
        not os.getenv("ENABLE_BILL_PAYMENT_TESTS"),
        reason="Bill payment tests disabled"
    )
    async def test_send_token(self):
        request = SendTokenDto(
            chainId=self.chain_id,
            tokenAddress=self.token_address,
            to=self.wallet_recipient,
            amount="0.00001"
        )
        response = await self.service.send_token(request)
        logger.info(f"Send token TX response: {response}")
        assert hasattr(response, "txHash")
