import os
import pytest
import logging
from monei.models.bills import (
    BillCategory
)
from monei.models.beneficiaries import CreateMobileBeneficiaryDto

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestBillDiscoveryService:

    @pytest.fixture(autouse=True)
    async def _setup(self, bill_discovery_service):
        self.client = bill_discovery_service
        self.test_mobile_number = os.getenv("TEST_MOBILE_NUMBER")
        self.test_electricity_account = os.getenv("TEST_ELECTRICITY_ACCOUNT")
        self.test_cable_tv_account = os.getenv("TEST_CABLETV_ACCOUNT")
        self.test_airtime_amount = os.getenv("TEST_AIRTIME_AMOUNT", "50")
        self.test_data_amount = os.getenv("TEST_DATA_AMOUNT", "50")
        self.test_beneficiary_id = os.getenv("TEST_BENEFICIARY_ID")

    # ---------------- Read-only endpoints ---------------- #

    async def test_get_biller_items_airtime(self):
        items = await self.client.bills.get_biller_items(BillCategory.AIRTIME, "MTN")
        logger.info(f"Biller items: {items}")
        assert isinstance(items, list)

    async def test_get_biller_items_mobile_data(self):
        items = await self.client.bills.get_biller_items(BillCategory.MOBILEDATA, "MTN")
        logger.info(f"Biller items: {items}")
        assert isinstance(items, list)

    async def test_get_biller_items_cable_bills(self):
        items = await self.client.bills.get_biller_items(BillCategory.CABLEBILLS, "DSTV")
        logger.info(f"Biller items: {items}")
        assert isinstance(items, list)

    async def test_get_biller_items_utility_bills(self):
        items = await self.client.bills.get_biller_items(BillCategory.UTILITYBILLS, "IBADAN DISCO ELECTRICITY")
        logger.info(f"Biller items: {items}")
        assert isinstance(items, list)

    async def test_get_biller_items_electricity(self):
        items = await self.client.bills.get_electricity_biller_items()
        logger.info(f"Biller items: {items}")
        assert isinstance(items, list)
