import pytest
import logging

from monei.models.payment_method import (
     PaymentMethodDto
)
from monei.models.enums.payment_method import (
     PaymentMethodType
)

logger = logging.getLogger(__name__)


@pytest.mark.asyncio
class TestPaymentMethodService:
    @pytest.fixture(autouse=True)
    async def _setup(self, payment_method_service):
        self.client = payment_method_service
    # === createPaymentMethod ===
    async def test_create_payment_method(self):
        

        payment_method_data = PaymentMethodDto(
            type=PaymentMethodType.CARD,
            subWalletId="6b4fcf43-fcf4-4d3a-a2f9-41463f97db7b",
            card={
                "expiryMonth": "12",
                "expiryYear": "30",
                "cardNumber": "4242 4242 4242 4242",
                "cvv": "123",
                "cardHolderName": "John Doe"
            }
        )

        # Act
        result = await self.client.create(payment_method_data)
        logger.info("Retrieved wallet: %s", result)

        # Assert
        assert "statusCode" in result
        assert "message" in result
        assert "data" in result

    # === getUserPaymentMethod ===
    async def test_get_payment_method(self):
        
        sub_wallet_id = "6b4fcf43-fcf4-4d3a-a2f9-41463f97db7b"

        result = await self.client.get_all(sub_wallet_id)
        logger.info("Payment Methods: %s", result)

        assert "statusCode" in result
        assert "message" in result
        assert "data" in result

    # === getUserPaymentMethodDetails ===
    async def test_get_payment_details(self):
       
        payment_method_id = "ad4fe7df-b026-4329-b488-a7b2546d2040"

        result = await self.client.get(payment_method_id)
        logger.info("Payment Method Details: %s", result)

        assert "statusCode" in result
        assert "message" in result
        assert "data" in result

    # === deleteUserPaymentMethod ===
    async def test_delete_payment_method(self):
        

        payment_method_id = "ad4fe7df-b026-4329-b488-a7b2546d2040"

        result = await self.client.delete(payment_method_id)
        logger.info("Delete Payment Method Response: %s", result)

        
        assert "statusCode" in result
        assert "message" in result
        assert "data" in result

    # === setDefaultPaymentMethod ===
    async def test_set_default_payment_method(self):
        

        payment_method_id = "b02cf699-3ad9-4e2e-be6b-65c1c94210aa"

        result = await self.client.set_default(payment_method_id)
        logger.info("Default Payment Method: %s", result)

        assert "statusCode" in result
        assert "message" in result
        assert "data" in result