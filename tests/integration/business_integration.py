import os
import pytest
import logging
from decimal import Decimal
from monei.models.business import CreateCustomerDto,UpdateCustomerDto

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration



@pytest.mark.asyncio
class TestEvmService:

    @pytest.fixture(autouse=True)
    async def _setup(self, business_service):
        self.service = business_service
        self.business_id = "business_id"
        self.customer_id = "customer_id"

    async def test_create_business_customer(self):

        business_id = ''
        request = CreateCustomerDto(
            name= '',
            phone='' ,
            email='',
            externalRef=''

        )
        response = await self.service.create_business_customer(business_id,request)
        logger.info(f"Create Business Customer: {response}")
        #assert balance.balance is not None

    async def test_get_business_customers(self):
        
        response = await self.service.get_business_customer(self.business_id)
        logger.info(f"Get Business Customer: {response}")
        #assert balance.balance is not None

    async def test_customer_details(self):
        
        response = await self.service.get_customer_details(self.business_id,self.customer_id)
        logger.info(f"Customer Details: {response}")
        #assert balance.balance is not None

    async def test_update_business_customer(self):

        request = UpdateCustomerDto(
            name= '',
            phone='' ,
            email='',
            externalRef=''

        )
        response = await self.service.update_customer(request, self.business_id,self.customer_id)
        logger.info(f"Update Customer: {response}")
        #assert balance.balance is not None

    async def test_disable_business_customer(self):
        
        response = await self.service.disable_customer(self.customer_id,self.business_id)
        logger.info(f"Disable Customer: {response}")
        #assert balance.balance is not None