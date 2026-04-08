import os
import pytest
import logging
from monei.models.wallet import DepositAuthDto,Customization,Customer,AddCardDto,FlwBillingAddressDto,DepositDto,DepositWithPaymentMethodDto,FlwAvsAuthDto,GeneratePaymentLinkDto
from monei.models.enums.wallet import DepositAuthType, DepositMethods
logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestWalletDepositService:

    @pytest.fixture(autouse=True)
    async def _setup(self, wallet_deposit_service):
        self.client = wallet_deposit_service
        
        self.test_bank_account = os.getenv("TEST_BANK_ACCOUNT")
        self.test_bank = os.getenv("TEST_BANK")
        

    async def test_deposit(self):
        deposit_method = DepositMethods.CARD

        card_details = AddCardDto(
            expiryMonth='11',
            expiryYear='31',
            cardNumber='4242 4242 5252 4242',
            cvv='123',
            cardHolderName='John Smith'
        )

        request = DepositDto(
            amount= 100,
            reference='uniquereference0099339',
            currency="NGN",
            card= card_details,
            narration='card deposit to wallet'
        ) 
        
        response = await self.client.deposit(deposit_method, request)
        logger.info(f"deposit info: {response}")
        #assert hasattr(wallet, "nairaBalance")

        # Assert
        assert "statusCode" in response
        assert "message" in response
        assert "data" in response

    
    async def test_deposit_via_payment_id(self):
        request = DepositWithPaymentMethodDto(
            amount= 1000,
            paymentMethodId= 'ad4fe7df-b026-4329-b488-a7b2546d2040',
            reference='unique-reference-1669223',
            currency='NGN',
            redirectUrl='https://citizen.com',
            meta =  {},
            narration='Deposit to wallet via payment method'

        )
        response = await self.client.deposit_via_payment_id(request)
        logger.info(f"deposit_via_payment_id: {response}")

        # Assert
        assert "statusCode" in response
        assert "message" in response
        assert "data" in response
       

   
    async def test_authorize(self):

        

        avs_address = FlwBillingAddressDto(
            city='sound city',
            country='nigeria',
            line1='david street',
            line2='ola avenue',
            postal_code='423432',
            state='Lagos'
        )

        avs = FlwAvsAuthDto(

            address= avs_address

        )

        request = DepositAuthDto(
            type= DepositAuthType.otp,
            reference='unique-reference-0098',
            pin='',
            otp='123456',
            avs= avs 
        )

        response = await self.client.authorize(request)
        logger.info(f"Test Authorize: {response}")

        # Assert
        assert "statusCode" in response
        assert "message" in response
        assert "data" in response
        

    @pytest.mark.skipif(
        not os.getenv("ENABLE_SOL_SWAP_TESTS"),
        reason="Solana swap tests disabled"
    )
    async def test_generate_payment_link(self):

        customer = Customer(
            email='',
            phoneNumber='',
            name='',
        )

        customization = Customization(
            title = 'Citizen'

        )

        request = GeneratePaymentLinkDto(
            amount=100,
            reference='unique-reference-0086',
            currency='',
            redirectUrl='https://citizen.com',
            customization=customization,
            customer=customer,
            narration= ''

        )
        
        
        response = await self.client.generate_payment_link(request)
        logger.info(f"Payment Link: {response}")

        # Assert
        assert "statusCode" in response
        assert "message" in response
        assert "data" in response
        

    
    async def test_payment_status(self):
        reference = 'unique-reference-002'
        response = await self.client.payment_status(reference)
        logger.info(f"Payment status: {response}")

        # Assert
        assert "statusCode" in response
        assert "message" in response
        assert "data" in response
        
