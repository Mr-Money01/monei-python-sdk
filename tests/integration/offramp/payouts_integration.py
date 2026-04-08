import os
import pytest
import logging
from monei.models.offramp import (
    VerifyOfframpBankAccountRequestDto
)

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestOfframpPayoutsService:

    @pytest.fixture(autouse=True)
    async def _setup(self, offramp_payouts_service):
        self.client = offramp_payouts_service
        
    # ---------------- Read-only endpoints ---------------- #

    async def test_get_offramp_banks(self):
        response = await self.client.get_offramp_banks()

        logger.info(f"Offramp Banks: {response}")
        # Assert
        assert "statusCode" in response
        assert "message" in response
        assert "data" in response
        

    async def test_verify_offramp_bank(self):
        request = VerifyOfframpBankAccountRequestDto(

            bankCode = 'GTBINGLA',
            accountNumber = "0223353863"

        )
        response = await self.client.verify_offramp_bank(request)
        logger.info(f"verify offramp: {response}")
        # Assert
        assert "statusCode" in response
        assert "message" in response
        assert "data" in response
        

