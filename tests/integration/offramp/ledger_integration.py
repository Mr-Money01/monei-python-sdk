import os
import pytest
import logging
from monei.models.offramp import (
    OfframpStatusRequestDto, OfframpHistoryRequestDto,OfframpExchangeRateDto,SwapCryptoToFiatRequestDto,OfframpStatus,WalletType,OfframpCurrency, Providers, OfframpAssets,OfframpNetworks
)

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestOfframpLedgerService:

    @pytest.fixture(autouse=True)
    async def _setup(self, offramp_ledger_service,offramp_exchange_service):
        self.ledger = offramp_ledger_service
        self.exchange = offramp_exchange_service
        
        # Create a test order to use for status checks

        try:
            quote_request = OfframpExchangeRateDto(
                token = OfframpAssets.USDT,
                network = OfframpNetworks.ethereum,
                amount = 100,
                fiat = OfframpCurrency.NGN
            )

            quote = await self.exchange.get_quote(quote_request)

            initiate_request = SwapCryptoToFiatRequestDto(
                amount = 100,
                token = OfframpAssets.USDT,
                network = OfframpNetworks.ethereum,
                fiatCurrency = OfframpCurrency.NGN,
                bankCode = "GTBINGLA",
                accountNumber = "0123456789",
                accountName = "John Doe"
            
            )
            order = await self.exchange.initiate_swap(initiate_request)
            self.test_order_reference = order.data.reference
            logger.info(f"Created test order: {self.test_order_reference}")

        except Exception as e:
            logger.warning(f"Could not create test order: {e}")
            self.test_order_reference = None
    # ---------------- Read-only endpoints ---------------- #

    async def test_get_history_default_pagination(self):
        # should get offramp history with default pagination

        
       
        response = await self.ledger.get_transactions()

        #logger.info(f"Transactions: {response}")

        # Assert
        assert "message" in response
        assert "data" in response
        #assert isinstance(response.meta, dict)
        assert "meta" in response
        assert "currentPage" in response.meta
        assert "itemsPerPage" in response.meta
        assert "totalItems" in response.meta
        assert "totalPages" in response.meta

        # Summary log
        logger.info({
            "totalTransactions": len(response.data),
            "page": response.meta.currentPage,
            "limit": response.meta.itemsPerPage,
            "totalRecords": response.meta.totalItems,
            "totalPages": response.meta.totalPages,
        })
        
        # check first transaction if exists 
        if len(response.data) > 0:
            first_tx = response.data[0]

            assert "id" in first_tx
            assert "reference" in first_tx
            assert "status" in first_tx
            assert "cryptoAmount" in first_tx
            assert "fiatAmount" in first_tx
            assert "exchangeRate" in first_tx

            logger.info({
                "simple_transaction": {
                    "id": first_tx.id,
                    "reference": first_tx.reference,
                    "status": first_tx.status,
                    "cryptoAmount": first_tx.cryptoAmount,
                    "fiatAmount": first_tx.fiatAmount
                }
            })



    
    async def test_get_history_with_pagination(self):
        # should get offramp history with custom pagination
       
        response = await self.ledger.get_transactions()

        logger.info(f"Transactions: {response}")

    
    async def test_get_offramp_with_different_pages(self):
        # should get offramp history with different pages
       
        response = await self.ledger.get_transactions()

        logger.info(f"Transactions: {response}")
        

    async def test_offramp_transaction_status(self):
        request = OfframpStatusRequestDto(
            reference = self.test_order_reference

        )
        response = await self.ledger.track_order(request)
        logger.info(f"transaction status: {response}")
        
