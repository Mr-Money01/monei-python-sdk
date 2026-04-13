import os
from urllib import response
import pytest
import logging
from decimal import Decimal
from monei.models.exchange import (
    SwapNativeToTokenDto, SwapSolToTokenDto, SwapTokenToNativeDto, SwapTokenToSolDto, SwapTokenToTokenDto, EvmSwapTokenToTokenDto, SwapSolToTokenDto
)

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestExchangeService:

    @pytest.fixture(autouse=True)
    async def _setup(self, evm_exchange_service, sol_exchange_service):
        self.evm_exchange = evm_exchange_service
        self.sol_exchange = sol_exchange_service
        # EVM
        self.chain_id = int(os.getenv("TEST_CHAIN_ID", 11155111))
        self.usdc_address = '0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238'
        self.eurc_address = '0x08210F9170F89Ab7658F0B5E3fF39b0E03C594D4'
        self.wallet_recipient = os.getenv("TEST_EVM_RECEIVER")
        # Solana
        self.sol_usdc_mint = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'
        self.sol_usdt_mint = 'Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB'
        self.test_usdc_token = "4zMMC9srt5Ri5X14GAgXhaHii3GnPAEERYPJgZJDncDU"
        self.test_eurc_token = "HzwqbKZw8HxMN6bF2yFZNrht3c2iXXzpKcFu7uBEDKtr"
        self.sol_amount = float(os.getenv("SOL_AMOUNT", 0.01))
        self.sol_test_recipient = os.getenv("SOL_TEST_RECIPIENT")

    # ---------------- EVM Exchange ---------------- #
    @pytest.mark.skipif(
        not os.getenv("ENABLE_SOL_SWAP_TESTS"),
        reason="Solana swap tests disabled"
    )
    async def test_get_native_to_token_price(self):
        request = SwapNativeToTokenDto(
            chainId=self.chain_id,
            tokenOut=self.usdc_address,
            amount="0.01"
        )
        response = await self.evm_exchange.get_native_to_token_price(request)
        logger.info(f"Native->Token quote: {response}")

        
        # Assertions
        #assert "data" in response
        #assert "message" in response
        #assert "statusCode" in response

        # Extract typed data
        #data = response.data

    @pytest.mark.skipif(
        not os.getenv("ENABLE_SOL_SWAP_TESTS"),
        reason="Solana swap tests disabled"
    )    
    async def test_get_token_to_token_price(self):
        request = EvmSwapTokenToTokenDto(
            tokenIn=self.usdc_address,
            tokenOut=self.eurc_address,
            amount= '0.2',
            chainId= 11155111
        )
        response = await self.evm_exchange.get_token_to_token_price(request)
        logger.info(f"Token->Token quote: {response}")
        #assert hasattr(response, "data")
        # Assertions
        #assert "data" in response
        #assert "message" in response
        #assert "statusCode" in response

        # Extract typed data
        #data = response.data

    @pytest.mark.skipif(
        not os.getenv("ENABLE_SOL_SWAP_TESTS"),
        reason="Solana swap tests disabled"
    )
    async def test_get_token_to_native_price(self):
        request = SwapTokenToNativeDto(
            chainId=self.chain_id,
            tokenIn='0xfb5B838b6cfEEdC2873aB27866079AC55363D37E',
            amount="0.1"
        )
        response = await self.evm_exchange.get_token_to_native_price(request)
        logger.info(f"Native->Token quote: {response}")
        #assert hasattr(quote, "price")
        # Assertions
        #assert "data" in response
        #assert "message" in response
        #assert "statusCode" in response

        # Extract typed data
        #data = response.data

    @pytest.mark.skipif(
        not os.getenv("ENABLE_SOL_SWAP_TESTS"),
        reason="Solana swap tests disabled"
    )
    async def test_swap_native_to_token(self):
        request = SwapNativeToTokenDto(
            chainId=11155111,
            tokenOut= self.usdc_address,
            amount="0.001"
        )
        response = await self.evm_exchange.swap_native_to_token(request)
        logger.info(f"Native->Token swap TX: {response}")
        
        # Assertions
        #assert "data" in response
        #assert "message" in response
        #assert "statusCode" in response

        # Extract typed data
        #data = response.data
        #logger.info(f"Swap transaction data: {data}")
        #assert "txhash" in data

    @pytest.mark.skipif(
        not os.getenv("ENABLE_SOL_SWAP_TESTS"),
        reason="Solana swap tests disabled"
    )
    async def test_swap_token_to_native(self):
        request = SwapTokenToNativeDto(
            chainId=11155111,
            tokenIn=self.usdc_address,
            amount="0.0001"
        )
        response = await self.evm_exchange.swap_token_to_native(request)
        logger.info(f"Native->Token swap TX: {response}")

        # Assertions
        #assert "data" in response
        #assert "message" in response
        #assert "statusCode" in response

        # Extract typed data
        #data = response.data
        #logger.info(f"Swap transaction data: {data}")
        #assert "txhash" in data

    @pytest.mark.skipif(
        not os.getenv("ENABLE_SOL_SWAP_TESTS"),
        reason="Solana swap tests disabled"
    )
    async def test_swap_token_to_token(self):
        request = EvmSwapTokenToTokenDto(
            tokenIn=self.usdc_address,
            tokenOut=self.eurc_address,
            amount= '1.5',
            chainId= 11155111
        )
        response = await self.evm_exchange.swap_token_to_token(request)
        #logger.info(f"Token->Token swap TX: {response}")

        # Assertions
        #assert "data" in response
        #assert "message" in response
        #assert "statusCode" in response

        # Extract typed data
        #data = response.data
        #logger.info(f"Swap transaction data: {data}")
        #assert "txhash" in data
        
    # ---------------- Solana Exchange ---------------- #

    
    async def test_get_sol_to_token_quote(self):
        quote = await self.sol_exchange.get_sol_to_token_quote(
            
            input_mint=self.test_usdc_token,
            amount=self.sol_amount
        )
        logger.info(f"Solana swap quote: {quote}")
        assert "price" in quote or "data" in quote


    async def test_get_token_to_sol_quote(self):
        quote = await self.sol_exchange.get_token_to_sol_quote(
            input_mint=self.test_usdc_token,
            amount=self.sol_amount  
        )
             
        #await self.client.exchange.get_token_to_sol_quote(quote)
        logger.info(f"Solana swap quote: {quote}")
        #assert "price" in quote or "data" in quote


    async def test_get_token_to_token_quote(self):
        quote = await self.sol_exchange.get_token_to_token_quote(
            input_mint=self.test_usdc_token,
            output_mint=self.test_eurc_token,
            amount=self.sol_amount
        )
             
        #await self.client.exchange.get_token_to_sol_quote(quote)
        logger.info(f"Solana swap quote: {quote}")
        #assert "price" in quote or "data" in quote

          
             
        #await self.client.exchange.get_token_to_sol_quote(quote)
        logger.info(f"Solana swap quote: {quote}")
        #assert "price" in quote or "data" in quote

    
    
    async def test_swap_sol_to_token(self):
        
        request = SwapSolToTokenDto(
            outputMint=self.test_usdc_token,
            amount=0.01
        )
        response = await self.sol_exchange.swap_sol_to_token(request)
        logger.info(f"SOL->Token swap TX: {response}")
        #assert response.statusCode == 200
        #assert response.message is not None
        #assert response.data is not None

        #assert response.data.txUrl is not None
        #assert response.data.signature is not None

        
    async def test_swap_token_to_sol(self):
        request = SwapTokenToSolDto(
            inputMint=self.test_usdc_token,
            amount=0.01
        )
        response = await self.sol_exchange.swap_token_to_sol(request)
        logger.info(f"SOL->Token swap TX: {response}")
        #assert response.statusCode == 200
        #assert response.message is not None
        #assert response.data is not None

        #assert response.data.txUrl is not None
        #assert response.data.signature is not None

    
    async def test_swap_token_to_token_solana(self):
        request = SwapTokenToTokenDto(
            inputMint=self.sol_usdc_mint,
            outputMint=self.sol_usdt_mint,
            amount= 0.01
        )
        tx = await self.sol_exchange.swap_token_to_token_solana(request)
        logger.info(f"Token->Token Solana swap TX: {tx}")
        #assert response.statusCode == 200
        #assert response.message is not None
        #assert response.data is not None

        #assert response.data.txUrl is not None
        #assert response.data.signature is not None

    
    
