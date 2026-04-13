import os
import pytest
import logging


logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestBillRecordService:

    @pytest.fixture(autouse=True)
    async def _setup(self, bill_record_service):
        self.client = bill_record_service
        
    async def test_get_bills(self):
        bills = await self.client.get_bills()
        logger.info(f"Bill payments: {bills}")
        

    async def test_get_bill_by_reference(self):
        reference = "bill1775893118769-978e2b1c-edc7-4c67-bfcc-8438a0513f21"
        bills = await self.client.get_bill_by_reference(reference)
        logger.info(f"Bill payments by reference '{reference}': {bills}")
        

    async def test_get_bill_receipt(self):
        transaction_id = "fd67683c-7f62-4512-8495-7f4ce6be8da9"
        bills = await self.client.generate_receipt(transaction_id)
        logger.info(f"Bill receipt for transaction ID '{transaction_id}': {bills}")
        


    
