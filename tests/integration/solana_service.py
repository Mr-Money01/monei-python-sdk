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
        self.network = SolanaNetwork.DEVNET
        self.test_recipient = os.getenv("TEST_SOLANA_RECEIVER")
        self.test_spl_token = "4zMMC9srt5Ri5X14GAgXhaHii3GnPAEERYPJgZJDncDU"
        self.test_spl_eurc = "HzwqbKZw8HxMN6bF2yFZNrht3c2iXXzpKcFu7uBEDKtr"
        


    # ---------------- Read-only endpoints ---------------- #

    async def test_get_wallet_address(self):
        result = await self.client.solana.get_address()
        logger.info(f"Solana Wallet address: {result}")
        #data = result["data"]

        #assert "statusCode" in result
        #assert "message" in result
        #assert "data" in result
        #assert "address" in data

    async def test_get_native_balance(self):
        result = await self.client.solana.get_native_balance(self.network)
        logger.info(f"Solana NATIVE balance: {result}")
        #data = result["data"]
        #assert "statusCode" in result
        #assert "message" in result
        #assert "data" in result
        #assert "balance" in data
        #assert Decimal(data["balance"]) >= 0

    async def test_get_token_balance(self):
        result = await self.client.solana.get_token_balance(self.test_spl_token, self.network)
        logger.info(f"Solana Token balance: {result}")
        #data = result["data"]
        #assert "statusCode" in result
        #assert "message" in result
        #assert "data" in result
        #assert "balance" in data
        #assert Decimal(data["balance"]) >= 0
        #logger.info(f"Solana Token balance: {data['balance']}")
        #assert Decimal(data["balance"]) >= 0

    async def test_get_portfolio(self):
        result = await self.client.solana.get_portfolio(self.network)
        logger.info(f"Portfolio: {result}")

       

    # ---------------- Transfer endpoints (risky) ---------------- #

    
    async def test_transfer_sol(self):
        # Get current balance
        balance_dto = await self.client.solana.get_native_balance(self.network)
        
        # Convert string balance to float
        current_balance = float(balance_dto.data.balance)
        logger.info(f"Current SOL balance: {current_balance} SOL")
        
        # Check if we have enough balance
        transfer_amount = 0.1
        min_rent_exempt = 0.00089  # Minimum SOL to keep for rent
        
        if current_balance < (transfer_amount + min_rent_exempt):
            logger.error(f"Insufficient balance!")
            logger.info(f"Need: {transfer_amount + min_rent_exempt} SOL")
            logger.info(f"Have: {current_balance} SOL")
            logger.info(f"Shortfall: {(transfer_amount + min_rent_exempt) - current_balance} SOL")
            return
        
        # Perform transfer
        request = TransferSolDto(
            to=self.test_recipient,
            amount=str(transfer_amount),  # Keep as string for the DTO
            network=self.network
        )
        
        result = await self.client.solana.send_native_token(request)
        
        # Log and assert
        logger.info(f"Transfer SOL response: {result}")
        
        # If result has statusCode, check it
        if hasattr(result, 'statusCode'):
            assert result.statusCode == 200
            logger.info(f"✅ Transfer successful! TX: {result.data.signature if hasattr(result, 'data') else 'unknown'}")

        #logger.info(f"Transfer SOL response: {response}")
        #data = result["data"]

        #assert "statusCode" in result
        #assert result["statusCode"] == 200
        #assert "message" in result
        #assert "data" in result
        #assert "signature" in data
        #assert isinstance(data["signature"], str)
        #signature = result["data"]["signature"]
        #logger.info("SOL Transfer Signature: %s", signature)


    
    async def test_transfer_token(self):
        request = TransferTokenDto(
            to=self.test_recipient,
            tokenMintAddress=self.test_spl_token,
            amount="0.1",
            network=self.network
        )
        result = await self.client.solana.send_token(request)
        logger.info(f"Transfer token response: {result}")
        # === BASE RESPONSE ===
        #assert "statusCode" in result
        #assert result["statusCode"] == 200
        #assert "message" in result
        #assert "data" in result

        # === NESTED PROPERTY ===
        #assert "signature" in result["data"]

        # === LOGGING TRANSFER SIGNATURE ===
        #signature = result["data"]["signature"]
        #logger.info("Token Transfer Signature: %s", signature)
