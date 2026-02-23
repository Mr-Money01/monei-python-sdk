import os
import pytest
import logging


logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestBillService:

    @pytest.fixture(autouse=True)
    async def _setup(self, monei_client):
        self.client = monei_client
        self.test_mobile_number = os.getenv("TEST_MOBILE_NUMBER")
        self.test_electricity_account = os.getenv("TEST_ELECTRICITY_ACCOUNT")
        self.test_cable_tv_account = os.getenv("TEST_CABLETV_ACCOUNT")
        self.test_airtime_amount = os.getenv("TEST_AIRTIME_AMOUNT", "50")
        self.test_data_amount = os.getenv("TEST_DATA_AMOUNT", "50")
        self.test_beneficiary_id = os.getenv("TEST_BENEFICIARY_ID")
     

    async def test_get_bills(self):
        bills = await self.client.bills.get_bills()
        logger.info(f"Bill payments: {bills}")
        

    async def test_get_bill_by_reference(self):
        reference = "test-reference-123"
        bills = await self.client.bills.get_bill_by_reference(reference)
        logger.info(f"Bill payments by reference '{reference}': {bills}")
        

    async def test_get_bill_receipt(self):
        transaction_id = "test-transaction-id-123"
        bills = await self.client.bills.get_bill_receipt(transaction_id)
        logger.info(f"Bill receipt for transaction ID '{transaction_id}': {bills}")
        


    
