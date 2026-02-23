import os
import pytest
import logging
from monei.models.bills import (
     AirtimePurchaseDto, DataPurchaseDto, ElectricityPaymentDto, CableTvPaymentDto
)
from monei.models.beneficiaries import CreateMobileBeneficiaryDto

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestBillService:

    @pytest.fixture(autouse=True)
    async def _setup(self, bill_pay_service):
        self.client = bill_pay_service 
        self.test_mobile_number = os.getenv("TEST_MOBILE_NUMBER")
        self.test_electricity_account = os.getenv("TEST_ELECTRICITY_ACCOUNT")
        self.test_cable_tv_account = os.getenv("TEST_CABLETV_ACCOUNT")
        self.test_airtime_amount = os.getenv("TEST_AIRTIME_AMOUNT", "50")
        self.test_data_amount = os.getenv("TEST_DATA_AMOUNT", "50")
        self.test_beneficiary_id = os.getenv("TEST_BENEFICIARY_ID")

 
    # ---------------- Action endpoints (toggled) ---------------- #

    
    async def test_buy_airtime(self):
        request = AirtimePurchaseDto(
            phoneNumber='08088447393',
            biller='airtel',
            amount=100
        )
        payment = await self.client.bills.buy_airtime(request)
        logger.info(f"Airtime payment: {payment}")
        assert hasattr(payment, "transactionId")

    
    async def test_buy_data(self):
        request = DataPurchaseDto(
            phoneNumber='08088447393',
            biller='airtel',
            itemCode='MD136'
        )
        payment = await self.client.bills.buy_data(request)
        logger.info(f"Data purchase: {payment}")
        assert hasattr(payment, "transactionId")

    
    async def test_buy_electricity(self):
        request = ElectricityPaymentDto(
            meterNumber='45083311550',
            disco='IBADAN DISCO ELECTRICITY',
            amount=500
        )
        payment = await self.client.bills.buy_electricity(request)
        logger.info(f"Electricity payment: {payment}")
        assert hasattr(payment, "transactionId")

    @pytest.mark.skipif(
        not os.getenv("ENABLE_BILL_PAYMENT_TESTS"),
        reason="Bill payment tests disabled"
    )
    async def test_subscribe_cable_tv(self):
        request = CableTvPaymentDto(
            decoderNumber=self.test_cable_tv_account,
            package="basic",
            provider="DSTV"
        )
        payment = await self.client.bills.subscribe_cable_tv(request)
        logger.info(f"Cable TV subscription: {payment}")
        assert hasattr(payment, "transactionId")

