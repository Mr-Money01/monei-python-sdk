import os
import pytest
import logging
from monei.models.offramp import (
    OfframpStatusRequestDto
)

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestOfframpLedgerService:

    @pytest.fixture(autouse=True)
    async def _setup(self, offramp_ledger_service):
        self.client = offramp_ledger_service
        
    # ---------------- Read-only endpoints ---------------- #

    async def test_get_offramp_transactions(self):
       
        response = await self.client.get_offramp_transactions()

        logger.info(f"Transactions: {response}")
        

    async def test_offramp_transaction_status(self):
        request = OfframpStatusRequestDto(
            reference = "OFF-LXKR5WO6KD"

        )
        response = await self.client.offramp_transaction_status(request)
        logger.info(f"transaction status: {response}")
        
