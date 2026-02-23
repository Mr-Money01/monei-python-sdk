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

    async def test_validate_bill(self):
        request = CableTvPaymentDto(
            decoderNumber=self.test_cable_tv_account,
            package="basic",
            provider="DSTV"
        )
        payment = await self.client.bills.subscribe_cable_tv(request)
        logger.info(f"Cable TV subscription: {payment}")
        assert hasattr(payment, "transactionId")

    async def test_get_bills(self):
        bills = await self.client.bills.get_bills()
        logger.info(f"Bill payments: {bills}")
        assert isinstance(bills, list)

    async def test_get_bill_by_reference(self):
        reference = "test-reference-123"
        bills = await self.client.bills.get_bill_by_reference(reference)
        logger.info(f"Bill payments by reference '{reference}': {bills}")
        assert isinstance(bills, list)

    async def test_get_bill_receipt(self):
        transaction_id = "test-transaction-id-123"
        bills = await self.client.bills.get_bill_receipt(transaction_id)
        logger.info(f"Bill receipt for transaction ID '{transaction_id}': {bills}")
        assert isinstance(bills, list)


    
