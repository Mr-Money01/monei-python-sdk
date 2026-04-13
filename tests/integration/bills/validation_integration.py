import os
import pytest
import logging
from monei.models.bills import (
     CableTvPaymentDto,
     ValidateBillDto
)

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestBillValidateService:

    @pytest.fixture(autouse=True)
    async def _setup(self, bill_validate_service):
        self.client = bill_validate_service
        self.test_mobile_number = os.getenv("TEST_MOBILE_NUMBER")
        self.test_electricity_account = os.getenv("TEST_ELECTRICITY_ACCOUNT")
        self.test_cable_tv_account = os.getenv("TEST_CABLETV_ACCOUNT")
        self.test_airtime_amount = os.getenv("TEST_AIRTIME_AMOUNT", "50")
        self.test_data_amount = os.getenv("TEST_DATA_AMOUNT", "50")
        self.test_beneficiary_id = os.getenv("TEST_BENEFICIARY_ID")


    async def test_validate_bill(self):
        request = ValidateBillDto(
            billerCode='BIL114',
            itemCode='UB161',
            customer="45083311550"
        )
        payment = await self.client.validate(request)
        logger.info(f"Bill validation: {payment}")
        

   

    
    
