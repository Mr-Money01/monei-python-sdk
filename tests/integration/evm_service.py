import os
from unittest import result
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
        self.chain_id = 11155111  
        self.wallet_recipient = os.getenv("TEST_EVM_RECEIVER")
        self.token_address = os.getenv("EVM_TEST_TOKEN_ADDRESS")

   

    async def test_get_token_balance(self):
        token_address = "0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238" 
        result = await self.service.get_token_balance(token_address, self.chain_id)
        logger.info(f"Token balance: {result}")
        # === BASE RESPONSE ===
        #assert "statusCode" in result
        #assert "message" in result
        #assert "data" in result

        # === NESTED PROPERTY ===
        #assert "balance" in result.data

        # === LOGGING TOKEN BALANCE ===
        #logger.info("Token Balance: %s", result.data.balance)

    async def test_get_native_balance(self):
        result = await self.service.get_native_balance(self.chain_id)
        logger.info(f"Native balance: {result}")
        # === BASE RESPONSE ===
        #assert "statusCode" in result
        #assert "message" in result
        #assert "data" in result

        # === NESTED PROPERTY ===
        #assert "balance" in result.data

        # === LOGGING NATIVE BALANCE ===
        #logger.info("Native Balance: %s", result.data.balance)

    async def test_get_portfolio(self):
        result = await self.service.get_portfolio(56)
        logger.info(f"Portfolio: {result.data}")

        

    async def test_send_native_token(self):
        request = SendNativeTokenDto(
            chainId=self.chain_id,
            to=self.wallet_recipient,
            amount="0.002"
        )
        response = await self.service.send_native_token(request)
        logger.info(f"Send native TX response: {response}")
       

    
    async def test_send_token(self):
        request = SendTokenDto(
            chainId=self.chain_id,
            tokenAddress='0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238',
            to=self.wallet_recipient,
            amount="0.2"
        )
        response = await self.service.send_token(request)
        #logger.info(f"Send token TX response: {response}")
       