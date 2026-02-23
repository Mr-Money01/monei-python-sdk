import os
import pytest
import logging
from monei.models.bills import (
    BillCategory, AirtimePurchaseDto, DataPurchaseDto, ElectricityPaymentDto, CableTvPaymentDto
)
from monei.models.beneficiaries import CreateMobileBeneficiaryDto

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestBillService:
    @pytest.fixture(autouse=True)
    async def _setup(self, monei_client):
        self.client = monei_client


    async def test_get_biller_items_utility_bills(self):
        items = await self.client.bills.get_biller_items(BillCategory.UTILITYBILLS, "IBADAN DISCO ELECTRICITY")
        logger.info(f"Biller items: {items}")
        assert isinstance(items, list)


    async def get_kyc_status(self):
        
        convs = await self.client.get_kyc_status()

        logger.info(f"Conversations: {convs}")
        assert isinstance(convs, list)


