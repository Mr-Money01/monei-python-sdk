import os
import pytest
import logging
from decimal import Decimal
from monei.models.solana import TransferSolDto, TransferTokenDto, SolanaNetwork

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestSolanaService:

    @pytest.fixture(autouse=True)
    async def _setup(self, monei_client):
        self.client = monei_client
        self.network = SolanaNetwork.MAINNET_BETA
        self.test_recipient = os.getenv("TEST_SOLANA_RECEIVER")
        self.test_spl_token = "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"

    # ---------------- Read-only endpoints ---------------- #

    async def test_get_wallet_address(self):
        address = await self.client.solana.get_wallet_address()
        logger.info(f"Wallet address: {address.address}")
        assert hasattr(address, "address")

    async def test_get_native_balance(self):
        balance = await self.client.solana.get_native_balance(self.network)
        logger.info(f"SOL balance: {balance.balance}")
        assert Decimal(balance.balance) >= 0

    async def test_get_token_balance(self):
        balance = await self.client.solana.get_token_balance(self.test_spl_token, self.network)
        logger.info(f"Token balance: {balance.balance}")
        assert Decimal(balance.balance) >= 0

    async def test_get_portfolio(self):
        portfolio = await self.client.solana.get_portfolio(self.network)
        logger.info(f"Portfolio: {portfolio}")
        assert hasattr(portfolio, "tokens")

    # ---------------- Transfer endpoints (risky) ---------------- #

    @pytest.mark.skipif(
        not os.getenv("ENABLE_BILL_PAYMENT_TESTS"),
        reason="Bill payment tests disabled"
    )
    async def test_transfer_sol(self):
        request = TransferSolDto(
            to=self.test_recipient,
            amount="0.0001",
            network=self.network
        )
        response = await self.client.solana.transfer_sol(request)
        logger.info(f"Transfer SOL response: {response}")
        assert hasattr(response, "signature")

    
    async def test_transfer_token(self):
        request = TransferTokenDto(
            to=self.test_recipient,
            tokenMintAddress=self.test_spl_token,
            amount="0.0001",
            network=self.network
        )
        response = await self.client.solana.transfer_token(request)
        logger.info(f"Transfer token response: {response}")
        assert hasattr(response, "signature")
