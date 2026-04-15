import pytest
import logging

logger = logging.getLogger(__name__)

pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestTransactionService:

    @pytest.fixture(autouse=True)
    async def _setup(self, transaction_service):
        self.service = transaction_service

        self.test_transaction_id = None
        self.test_transaction_reference = None

        transactions = await self.service.get_all()
        transaction = transactions['data']['transactions'][0] if transactions['data']['transactions'] else None
        logger.info(f"First transaction: {transaction}")
        

        if transaction:
            self.test_transaction_id = transaction['id']
            self.test_transaction_reference = transaction['reference'] 

    async def test_get_user_transactions(self):
        txs = await self.service.get_all()
        logger.info(f"User transactions: {txs}")

        #assert isinstance(txs, list)

        #if txs:
            #assert hasattr(txs[0], "id")
            #assert hasattr(txs[0], "reference")

    async def test_get_transaction_by_id(self):
        if not self.test_transaction_id:
            pytest.skip("No transaction available to test get_transaction_by_id")

        tx = await self.service.get_by_id(self.test_transaction_id)
        logger.info(f"Transaction by ID: {tx}")

        #assert tx.id == self.test_transaction_id

    async def test_get_transaction_by_reference(self):
        

        tx = await self.service.get_by_reference(
            self.test_transaction_reference
        )
        logger.info(f"Transaction by reference: {tx}")

        #assert tx.reference == self.test_transaction_reference

    async def test_get_deposits(self):
        tx = await self.service.get_deposits()
        logger.info(f"Transaction by deposits: {tx}")

    async def test_get_deposit(self):
        tx = await self.service.get_deposit(self.test_transaction_id)
        logger.info(f"Transaction by deposit: {tx}")
