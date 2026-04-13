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
        
    # ---------------- Read-only endpoints ---------------- #

    async def test_get_biller_items_airtime(self):
        result = await self.client.get_biller(BillCategory.AIRTIME, "MTN")
        logger.info(f"AIRTIME Biller items: {result}")
         # === BASE RESPONSE ===
        assert "statusCode" in result
        assert result.statusCode == 200
        assert "message" in result
        assert "data" in result

        items = result.data

        # === ARRAY CHECK ===
        assert isinstance(items, list)


        # === VALIDATE EVERY ITEM ===
        for index, item in enumerate(items):
            # === FIELD EXISTENCE ===
            expected_fields = [
                "id", "biller_code", "name", "default_commission", "date_added",
                "country", "is_airtime", "biller_name", "item_code", "short_name",
                "fee", "commission_on_fee", "reg_expression", "label_name",
                "amount", "is_resolvable", "group_name", "category_name",
                "is_data", "default_commission_on_amount",
                "commission_on_fee_or_amount", "validity_period"
            ]

        for field in expected_fields:
            assert field in item, f"Missing field {field} at index {index}"

        # === TYPE CHECKS ===
        assert isinstance(item.id, int)
        assert isinstance(item.biller_code, str)
        assert isinstance(item.name, str)
        assert isinstance(item.default_commission, (int, float))
        assert isinstance(item.country, str)
        assert isinstance(item.is_airtime, bool)
        assert isinstance(item.item_code, str)
        assert isinstance(item.short_name, str)
        assert isinstance(item.fee, (int, float))
        assert isinstance(item.commission_on_fee, bool)
        assert isinstance(item.reg_expression, str)
        assert isinstance(item.label_name, str)
        assert isinstance(item.amount, (int, float))
        assert isinstance(item.is_resolvable, bool)
        assert isinstance(item.group_name, str)
        assert isinstance(item.category_name, str)

        assert item.is_data is None or isinstance(item.is_data, bool)

        assert isinstance(item.default_commission_on_amount, (int, float))
        assert isinstance(item.commission_on_fee_or_amount, (int, float))

        assert item.validity_period is None or isinstance(item.validity_period, str)

    async def test_get_biller_items_mobile_data(self):
        result = await self.client.get_biller(BillCategory.MOBILEDATA, "MTN")

        logger.info(f"MOBILEDATA Biller items: {result}")
        
        assert "statusCode" in result
        #assert result["statusCode"] == 200
        assert "message" in result
        assert "data" in result

    async def test_get_biller_items_cable_bills(self):
        result = await self.client.get_biller(BillCategory.CABLEBILLS, "DSTV")
        logger.info(f"Cable Biller items: {result}")
        
        assert "statusCode" in result
        #assert result["statusCode"] == 200
        assert "message" in result
        assert "data" in result

    async def test_get_biller_items_utility_bills(self):
        result = await self.client.get_biller(BillCategory.UTILITYBILLS, "IBADAN DISCO ELECTRICITY")
        logger.info(f"Utility Biller items: {result}")
        assert "statusCode" in result
        #assert result["statusCode"] == 200
        assert "message" in result
        assert "data" in result 

    async def test_get_biller_items_electricity(self):

        result = await self.client.get_electricity_biller()
        logger.info(f"Electricity Biller items: {result}")
        
        assert "StatusCode" in result
        assert result.StatusCode == 200
        assert "message" in result
        assert "data" in result
