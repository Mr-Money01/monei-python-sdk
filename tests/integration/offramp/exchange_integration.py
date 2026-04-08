import os
import pytest
import logging
from monei.models.offramp import (
    SwapCryptoToFiatRequestDto,OfframpExchangeRateDto
    
)
from monei.models.enums.offramp import OfframpAssets, OfframpNetworks, OfframpCurrency

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestOfframpExchangeService:

    @pytest.fixture(autouse=True)
    async def _setup(self, offramp_exchange_service):
        self.client = offramp_exchange_service
      
        

    async def test_get_assets(self):
        assets = await self.client.get_assets()

        logger.info(f"Assets: {assets}")
        

    async def test_get_fiat_quote(self):
        request = OfframpExchangeRateDto(
            token = OfframpAssets.USDT,
            network = OfframpNetworks.ethereum,
            amount = 100,
            fiat = OfframpCurrency.NGN

        ) 
        quote = await self.client.get_quote(request)
        logger.info(f"Quote: {quote}")
        

    
    async def test_crypto_to_usdt(self):
        request = SwapCryptoToFiatRequestDto(
            amount = 100,
            token = OfframpAssets.USDT,
            network = OfframpNetworks.ethereum,
            fiatCurrency = OfframpCurrency.NGN,
            bankCode = "GTBINGLA",
            accountNumber = "0123456789",
            accountName = "John Doe"
         
        )
        response = await self.client.initiate_swap(request)
        logger.info(f"Chat response: {response}")
        #assert hasattr(response, "message")


    async def test_crypto_to_usdc(self):

        #  Arrange - get quote for USDC first

        request = OfframpExchangeRateDto(
            token = OfframpAssets.USDC,
            network = OfframpNetworks.ethereum,
            amount = 600,
            fiat = OfframpCurrency.NGN

        ) 
        usdc_quote = await self.client.get_quote(request)
        logger.info(f"Quote: {usdc_quote}")


        request = SwapCryptoToFiatRequestDto(
            amount = 600,
            token = "USDC",
            network = "ethereum",
            fiatCurrency = OfframpNetworks.ethereum,
            bankCode = "GTBINGLA",
            accountNumber = "0123456789",
            accountName = "John Doe"
         
        )
        response = await self.client.crypto_to_fiat(request)
        logger.info(f"Chat response: {response}")
        #assert hasattr(response, "message")

 
