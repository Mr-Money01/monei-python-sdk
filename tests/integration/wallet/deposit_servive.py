import os
import pytest
import logging
from monei.models.wallet import DepositAuthDto,Customization,Customer,CardDepositDto,FlwBillingAddressDto,DepositDto,DepositWithPaymentMethodDto,FlwAvsAuthDto,GeneratePaymentLinkDto
from monei.models.enums.wallet import DepositMethods
logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestWalletService:

    @pytest.fixture(autouse=True)
    async def _setup(self, wallet_deposit_service):
        self.client = wallet_deposit_service
        
        self.test_bank_account = os.getenv("TEST_BANK_ACCOUNT")
        self.test_bank = os.getenv("TEST_BANK")
        

    async def test_deposit(self):
        method = DepositMethods(
            CARD = "CARD"

        )
        request = DepositDto(
            amount= 100,
            reference='',
            currency="NGN",
            card= card_details,
            narration=''
        ) 
        card_details = CardDepositDto(
            expiryMonth='',
            expiryYear='',
            cardNumber='',
            cvv='',
            cardHolderName=''

        )
        response = await self.client.wallet.deposit(method,request)
        logger.info(f"deposit info: {response}")
        #assert hasattr(wallet, "nairaBalance")

    @pytest.mark.skipif(
        not os.getenv("ENABLE_SOL_SWAP_TESTS"),
        reason="Solana swap tests disabled"
    )
    async def test_deposit_via_payment_id(self):
        request = DepositWithPaymentMethodDto(
            amount= 100,
            paymentMethodId= 'str',
            reference='',
            currency='',
            redirectUrl='',
            meta =  {},
            narration=''

        )
        response = await self.client.wallet.deposit_via_payment_id(request)
        logger.info(f"deposit_via_payment_id: {response}")
       

   
    async def test_authorize(self):

        avs = FlwAvsAuthDto(

            address= avs_address

        )

        avs_address = FlwBillingAddressDto(
            city='',
            country='',
            line1='',
            line2='',
            postal_code='',
            state=''
        )

        request = DepositAuthDto(
            type= 'DepositAuthType',
            reference='',
            pin='',
            otp='',
            avs= avs 
        )

        response = await self.client.wallet.authorize(request)
        logger.info(f"Test Authorize: {response}")
        


    async def test_generate_payment_link(self):
        request = GeneratePaymentLinkDto(
            amount=100,
            reference='',
            currency='',
            redirectUrl='',
            customization=customization,
            customer=customer,
            narration= ''

        )
        customer = Customer(
            email='',
            phoneNumber='',
            name='',
            

        )
        customization = Customization(
            title = ''

        )
        response = await self.client.wallet.generate_payment_link(request)
        logger.info(f"Payment Link: {response}")
        

    
    async def test_payment_status(self):
        reference = 'test-refernce'
        response = await self.client.wallet.payment_status(reference)
        logger.info(f"Payment status: {response}")
        
