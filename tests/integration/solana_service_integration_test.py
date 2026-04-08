from inspect import signature
import os
import pytest
import logging
import json
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
        result = await self.client.solana.get_wallet_address()
        logger.info(f"Solana Wallet address: {result.address}")
        data = result["data"]

        assert "statusCode" in result
        assert "message" in result
        assert "data" in result
        assert "address" in data

    async def test_get_native_balance(self):
        result = await self.client.solana.get_native_balance(self.network)
        logger.info(f"Solana NATIVE balance: {result.balance}")
        data = result["data"]
        assert "statusCode" in result
        assert "message" in result
        assert "data" in result
        assert "balance" in data
        assert Decimal(data["balance"]) >= 0

    async def test_get_token_balance(self):
        result = await self.client.solana.get_token_balance(self.test_spl_token, self.network)
        logger.info(f"Solana Token balance: {result.balance}")
        data = result["data"]
        assert "statusCode" in result
        assert "message" in result
        assert "data" in result
        assert "balance" in data
        assert Decimal(data["balance"]) >= 0
        logger.info(f"Solana Token balance: {data['balance']}")
        assert Decimal(data["balance"]) >= 0

    async def test_get_portfolio(self):
        result = await self.client.solana.get_portfolio(self.network)
        #logger.info(f"Portfolio: {portfolio}")

        # === BASE RESPONSE ===
        assert "statusCode" in result
        assert "message" in result
        assert "data" in result

        p = result["data"]

        # === PORTFOLIO DATA ===
        assert "userId" in p
        assert "address" in p
        assert "nativeBalance" in p
        assert "nativeBalanceLamports" in p
        assert "tokens" in p

        # === VALIDATE NATIVE BALANCE TYPES ===
        assert isinstance(p["nativeBalance"], str)
        assert isinstance(p["nativeBalanceLamports"], str)

        # === TOKENS ARRAY ===
        assert isinstance(p["tokens"], list)

        if len(p["tokens"]) > 0:
            for t in p["tokens"]:
                # === MATCH OBJECT (like Jest toMatchObject) ===
                assert isinstance(t.get("mintAddress"), str)
                assert isinstance(t.get("name"), str)
                assert isinstance(t.get("symbol"), str)
                assert isinstance(t.get("balance"), (int, float))
                assert isinstance(t.get("rawBalance"), str)
                assert isinstance(t.get("decimals"), int)

        logger.info(
            "Sample Token Info: decimals=%s symbol=%s balance=%s mint=%s",
            t["decimals"],
            t["symbol"],
            t["balance"],
            t["mintAddress"],
        )

        logger.info(
            "Solana Portfolio Summary: %s",
            {
                "address": p.get("address"),
                "solBalance": p.get("nativeBalance"),
                "usdValue": p.get("totalValueUsd"),
                "tokenCount": len(p["tokens"]),
            },
        )

        

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
        result = await self.client.solana.transfer_sol(request)

        #logger.info(f"Transfer SOL response: {response}")
        data = result["data"]

        assert "statusCode" in result
        assert result["statusCode"] == 200
        assert "message" in result
        assert "data" in result
        assert "signature" in data
        assert isinstance(data["signature"], str)
        signature = result["data"]["signature"]
        logger.info("SOL Transfer Signature: %s", signature)


    
    async def test_transfer_token(self):
        request = TransferTokenDto(
            to=self.test_recipient,
            tokenMintAddress=self.test_spl_token,
            amount="0.0001",
            network=self.network
        )
        result = await self.client.solana.transfer_token(request)
        #logger.info(f"Transfer token response: {result}")
        # === BASE RESPONSE ===
        assert "statusCode" in result
        assert result["statusCode"] == 200
        assert "message" in result
        assert "data" in result

        # === NESTED PROPERTY ===
        assert "signature" in result["data"]

        # === LOGGING TRANSFER SIGNATURE ===
        signature = result["data"]["signature"]
        logger.info("Token Transfer Signature: %s", signature)
