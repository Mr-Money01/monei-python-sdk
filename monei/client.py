"""Main Monei client implementation"""

import os
from dotenv import load_dotenv
from typing import Dict, Any, Optional
import httpx
from .exceptions import (
    MoneiAPIError,
    AuthenticationError,
    ValidationError,
    NotFoundError,
    RateLimitError,
)

# Load .env as soon as pytest starts
load_dotenv()
from .services.user_service import UserService
from .services.wallet_service import WalletService
from .services.evm_service import EvmService
from .services.solana_service import SolanaService
from .services.transaction_service import TransactionService
from .services.bill_service import BillService
from .services.beneficiary_service import BeneficiaryService
from .services.exchange_service import ExchangeService
from .services.agent_service import AgentService
#from .services.kyc_verification_service import KycVerificationService
from .services.payment_method_service import PaymentMethodService
from .services.offramp.exchange import OfframpExchangeService
from .services.offramp.ledger import OfframpLedgerService
from .services.offramp.payouts import OfframpPayoutsService
from .services.wallet.account_service import WalletAccountService
from .services.wallet.deposit_service import WalletDepositService
from .services.wallet.payout_service import WalletPayoutService
from .services.wallet.utility_service import WalletUtilityService
from .services.bills.discovery_service import BillDiscoveryService
from .services.bills.pay_service import BillPayService
from .services.bills.records_service import BillRecordsService
from .services.bills.validation_service import BillValidationService
from .services.business_service import BusinessService


class MoneiClient:
    """Main client for interacting with the Monei API"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ):
        """
        Initialize the Monei client.
        
        Args:
            api_key: Your Monei API key. If not provided, will try to get from MONEI_API_KEY environment variable.
            base_url: Base URL for the API. Defaults to production API.
            timeout: Request timeout in seconds.
            
        Raises:
            AuthenticationError: If no API key is provided.
        """
        self.api_key = api_key or os.getenv('MONEI_API_KEY')
        if not self.api_key:
            raise AuthenticationError(
                "No API key provided. Provide api_key parameter or set MONEI_API_KEY environment variable."
            )
            
        self.base_url = base_url or "https://api.monei.cc"
        self.timeout = timeout
        self._client = None
        
        # Initialize services
        self.user = UserService(self)
        self.wallet = WalletService(self)
        self.evm = EvmService(self)
        self.solana = SolanaService(self)
        self.transactions = TransactionService(self)
        self.bills = BillService(self)
        self.beneficiaries = BeneficiaryService(self)
        self.exchange = ExchangeService(self)
        self.agent = AgentService(self)
        #self.kyc = KycVerificationService(self)
        self.payment_methods = PaymentMethodService(self)
        self.offramp_exchange = OfframpExchangeService(self)
        self.offramp_payouts = OfframpPayoutsService(self)
        self.offramp_ledger = OfframpLedgerService(self)
        self.wallet_account = WalletAccountService(self)
        self.wallet_deposit = WalletDepositService(self)
        self.wallet_payout = WalletPayoutService(self)
        self.wallet_utility = WalletUtilityService(self)
        self.bill_discovery = BillDiscoveryService(self)
        self.bill_pay = BillPayService(self)
        self.bill_record = BillRecordsService(self)
        self.business_service = BusinessService(self)
    
    @property
    def client(self) -> httpx.AsyncClient:
        """Lazy initialization of HTTP client"""
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=self.timeout,
                headers={
                    "X-API-KEY": self.api_key,
                    "Content-Type": "application/json",
                    "User-Agent": f"Monei-Python-SDK/0.1.0"
                }
            )
        return self._client
    
    async def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make authenticated request to Monei API"""
        url = f"/api/v1{endpoint}"
        
        try:
            response = await self.client.request(
                method=method,
                url=url,
                json=data,
                params=params
            )
            
            print(f"Request URL: {response}")
            # Handle different status codes
            if response.status_code in [200, 201]:
                if not response.content:
                    return None
                return response.json() 
            elif response.status_code == 400:
                raise ValidationError(f"Validation error: {response.text}", response.status_code, response)
            elif response.status_code == 401:
                raise AuthenticationError(f"Authentication failed: {response.text}", response.status_code, response)
            elif response.status_code == 404:
                raise NotFoundError(f"Resource not found: {response.text}", response.status_code, response)
            elif response.status_code == 429:
                raise RateLimitError(f"Rate limit exceeded: {response.text}", response.status_code, response)
            else:
                raise MoneiAPIError(
                    f"API request failed with status {response.status_code}: {response.text}",
                    response.status_code,
                    response
                )
                
        except httpx.TimeoutException:
            raise MoneiAPIError("Request timeout")
        except httpx.RequestError as e:
            raise MoneiAPIError(f"Request error: {str(e)}")
    
    async def close(self):
        """Close the HTTP client"""
        if self._client:
            await self._client.aclose()
            self._client = None
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()