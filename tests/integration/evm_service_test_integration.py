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
        self.chain_id = 56  # Binance Smart Chain
        self.wallet_recipient = os.getenv("TEST_EVM_RECEIVER")
        self.token_address = os.getenv("EVM_TEST_TOKEN_ADDRESS")

   

    async def test_get_token_balance(self):
        token_address = "0x55d398326f99059fF775485246999027B3197955"  # DAI
        result = await self.service.get_token_balance(token_address, self.chain_id)
        logger.info(f"Token balance: {result.data.balance}")
        # === BASE RESPONSE ===
        assert "statusCode" in result
        assert "message" in result
        assert "data" in result

        # === NESTED PROPERTY ===
        assert "balance" in result.data

        # === LOGGING TOKEN BALANCE ===
        logger.info("Token Balance: %s", result.data.balance)

    async def test_get_native_balance(self):
        result = await self.service.get_native_balance(self.chain_id)
        logger.info(f"Native balance: {result.data.balance}")
        # === BASE RESPONSE ===
        assert "statusCode" in result
        assert "message" in result
        assert "data" in result

        # === NESTED PROPERTY ===
        assert "balance" in result.data

        # === LOGGING NATIVE BALANCE ===
        logger.info("Native Balance: %s", result.data.balance)

    async def test_get_portfolio(self):
        result = await self.service.get_portfolio(self.chain_id)
        logger.info(f"Portfolio: {result.data}")

        # Assert root fields
        assert result.statusCode is not None
        assert result.message is not None
        assert result.data is not None
        assert result.statusCode == 200

        # Extract typed portfolio
        p = result.data
        # === ASSERT ROOT PORTFOLIO FIELDS ===
        assert p.userId is not None
        assert p.walletAddress is not None
        assert p.network is not None
        assert p.totalPortfolioValueUSD is not None
        assert p.updatedAt is not None

        # === ASSERT NATIVE TOKEN ===
        native = p.nativeToken

        assert native.name is not None
        assert native.symbol is not None
        assert native.decimals is not None
        assert native.logoUrl is not None
        assert native.balance is not None
        assert native.balanceUSD is not None
        assert native.priceUSD is not None
        assert native.rawBalance is not None
        assert native.network is not None

        # === ASSERT TOKENS ARRAY ===
        tokens = p.tokens
        assert isinstance(tokens, list)

        if len(tokens) > 0:
            for t in tokens:
                assert isinstance(t.contractAddress, str)
                assert isinstance(t.name, str)
                assert isinstance(t.symbol, str)
                assert isinstance(t.decimals, int)
                assert isinstance(t.logoUrl, str)
                assert isinstance(t.type, str)
                assert isinstance(t.balance, str)
                assert isinstance(t.balanceUSD, str)
                assert isinstance(t.priceUSD, str)
                assert isinstance(t.rawBalance, str)
                assert isinstance(t.network, str)

        logger.info("Found %s tokens in portfolio.", len(tokens))
        logger.info("Checking first token: %s", tokens[0])

    async def test_send_native_token(self):
        request = SendNativeTokenDto(
            chainId=self.chain_id,
            to=self.wallet_recipient,
            amount="0.00001"
        )
        response = await self.service.send_native_token(request)
        logger.info(f"Send native TX response: {response}")
        assert hasattr(result, "statusCode")
        assert result.statusCode == 200
        assert hasattr(result, "data")
        assert hasattr(result.data, "txHash")

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
        #logger.info(f"Send token TX response: {response}")
        assert hasattr(result, "statusCode")
        assert result.statusCode == 200
        assert hasattr(result, "data")
        assert hasattr(result.data, "txHash")
