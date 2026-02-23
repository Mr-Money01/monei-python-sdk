import os
import pytest
import logging
from monei.models.offramp import (
    SwapCryptoToFiatRequestDto,OfframpExchangeRateDto
    
)

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
            token = "USDT",
            network = "polygon",
            amount = "100",
            fiat = "NGN"

        ) 
        quote = await self.client.get_fiat_quote(request)
        logger.info(f"Quote: {quote}")
        

    
    async def test_crypto_to_fiat(self):
        request = SwapCryptoToFiatRequestDto(
            amount = "100",
            token = "USDT",
            network = "base",
            fiatCurrency = "NGN",
            bankCode = "058",
            accountNumber = "0736379044",
            accountName = "ayodeji"
         
        )
        response = await self.client.crypto_to_fiat(request)
        logger.info(f"Chat response: {response}")
        #assert hasattr(response, "message")

 
