import os
import pytest
import logging
from decimal import Decimal
from monei.models.exchange import (
    SwapNativeToTokenDto, SwapTokenToNativeDto, SwapTokenToSolDto, SwapTokenToTokenDto, SwapSolToTokenDto
)

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestExchangeService:

    @pytest.fixture(autouse=True)
    async def _setup(self, monei_client):
        self.client = monei_client
        # EVM
        self.chain_id = int(os.getenv("TEST_CHAIN_ID", 56))
        self.usdc_address = '0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d'
        self.usdt_address = '0x55d398326f99059fF775485246999027B3197955'
        self.wallet_recipient = os.getenv("TEST_EVM_RECEIVER")
        # Solana
        self.sol_usdc_mint = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'
        self.sol_usdt_mint = 'Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB'
        self.sol_amount = float(os.getenv("SOL_AMOUNT", 0.0001))
        self.sol_test_recipient = os.getenv("SOL_TEST_RECIPIENT")

    # ---------------- EVM Exchange ---------------- #

    async def test_get_native_to_token_price(self):
        request = SwapNativeToTokenDto(
            chainId=self.chain_id,
            tokenOut=self.usdc_address,
            amount="0.01"
        )
        quote = await self.client.exchange.get_swap_native_to_token_price(request)
        logger.info(f"Native->Token quote: {quote}")
        #assert hasattr(quote, "price")

    async def test_get_token_to_token_price(self):
        request = SwapTokenToTokenDto(
            inputMint=self.usdc_address,
            outputMint=self.usdt_address,
            amount= 0.2
        )
        quote = await self.client.exchange.get_swap_token_to_token_price(request)
        logger.info(f"Token->Token quote: {quote}")
        assert hasattr(quote, "amount")

    async def test_get_token_to_native_price(self):
        request = SwapTokenToNativeDto(
            chainId=self.chain_id,
            tokenIn='0xfb5B838b6cfEEdC2873aB27866079AC55363D37E',
            amount="0.1"
        )
        quote = await self.client.exchange.get_swap_token_to_native_price(request)
        logger.info(f"Native->Token quote: {quote}")
        #assert hasattr(quote, "price")
    
    async def test_swap_native_to_token(self):
        request = SwapNativeToTokenDto(
            chainId=56,
            tokenOut= self.usdc_address,
            amount="0.001"
        )
        tx = await self.client.exchange.swap_native_to_token(request)
        logger.info(f"Native->Token swap TX: {tx}")
        assert hasattr(tx, "txHash")




    async def test_swap_token_to_native(self):
        request = SwapTokenToNativeDto(
            chainId=56,
            tokenIn=self.usdt_address,
            amount="0.0001"
        )
        tx = await self.client.exchange.swap_token_to_native(request)
        logger.info(f"Native->Token swap TX: {tx}")
        assert hasattr(tx, "txHash")

    
    async def test_swap_token_to_token(self):
        request = SwapTokenToTokenDto(

            inputMint=self.usdc_address,
            outputMint=self.usdt_address,
            amount= 0.0001
        )
        tx = await self.client.exchange.swap_token_to_token(request)
        logger.info(f"Token->Token swap TX: {tx}")
        assert hasattr(tx, "txHash")

    # ---------------- Solana Exchange ---------------- #

    async def test_get_sol_to_token_quote(self):
        quote = await self.client.exchange.get_sol_to_token_quote(
            
            input_mint='Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB',
            amount=self.sol_amount
        )
        logger.info(f"Solana swap quote: {quote}")
        assert "price" in quote or "data" in quote
    
    async def test_get_token_to_sol_quote(self):
        quote = await self.client.exchange.get_token_to_sol_quote(
            input_mint='Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB',
            
            amount=0.1
        )
             
        #await self.client.exchange.get_token_to_sol_quote(quote)
        logger.info(f"Solana swap quote: {quote}")
        #assert "price" in quote or "data" in quote

    async def test_get_token_to_token_quote(self):
        quote = await self.client.exchange.get_token_to_token_quote(
            input_mint='Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB',
            output_mint ='Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB',       
            amount=0.0001
        )
             
        #await self.client.exchange.get_token_to_sol_quote(quote)
        logger.info(f"Solana swap quote: {quote}")
        #assert "price" in quote or "data" in quote

    
    #DONE
    async def test_swap_sol_to_token(self):
        
        request = SwapSolToTokenDto(
            outputMint=self.sol_usdc_mint,
            amount=0.0001
        )
        tx = await self.client.exchange.swap_sol_to_token(request)
        logger.info(f"SOL->Token swap TX: {tx}")
        assert hasattr(tx, "signature")

        

    async def test_swap_token_to_sol(self):
        request = SwapTokenToSolDto(
            inputMint='Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB',
            amount=0.0001
        )
        tx = await self.client.exchange.swap_token_to_sol(request)
        logger.info(f"SOL->Token swap TX: {tx}")
        assert hasattr(tx, "signature")

    
    async def test_swap_token_to_token_solana(self):
        request = SwapTokenToTokenDto(
            inputMint=self.sol_usdc_mint,
            outputMint=self.sol_usdt_mint,
            amount= 0.0001
        )
        tx = await self.client.exchange.swap_token_to_token_solana(request)
        logger.info(f"Token->Token Solana swap TX: {tx}")
        assert hasattr(tx, "txHash")

    
    async def test_swap_token_to_sol(self):
        request = SwapSolToTokenDto(
            to=self.sol_test_recipient,
            tokenMint=self.sol_input_mint,
            amount=str(self.sol_amount)
        )
        tx = await self.client.exchange.swap_token_to_sol(request)
        logger.info(f"Token->SOL swap TX: {tx}")
        assert hasattr(tx, "txHash")
