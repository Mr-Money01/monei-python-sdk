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
class TestBillPayService:

    @pytest.fixture(autouse=True)
    async def _setup(self, bill_pay_service):
        self.client = bill_pay_service 
        

 
    # ---------------- Action endpoints (toggled) ---------------- #

    
    async def test_buy_airtime(self):
        request = AirtimePurchaseDto(
            phoneNumber='08088447393',
            biller='airtel',
            amount=100
        )
        payment = await self.client.buy_airtime(request)
        logger.info(f"Airtime payment: {payment}")
        

    
    async def test_buy_data(self):
        request = DataPurchaseDto(
            phoneNumber='08088447393',
            biller='airtel',
            itemCode='MD136'
        )
        payment = await self.client.buy_mobile_data(request)
        logger.info(f"Data purchase: {payment}")
        

    
    async def test_buy_electricity(self):
        request = ElectricityPaymentDto(
            meterNumber='45083311550',
            disco='IBADAN DISCO ELECTRICITY',
            amount=500
        )
        payment = await self.client.buy_electricity(request)
        logger.info(f"Electricity payment: {payment}")
        

    
    async def test_subscribe_cable_tv(self):
        request = CableTvPaymentDto(
            smartcardNumber='1234567890',
            itemCode='CB177',
            biller='dstv'
        )
        payment = await self.client.subscribe_cable_tv(request)
        logger.info(f"Cable TV subscription: {payment}")
        

