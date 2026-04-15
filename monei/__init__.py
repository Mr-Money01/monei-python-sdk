"""
MrMonei Python SDK
"""

from .client import MoneiClient
from .exceptions import (
    MoneiAPIError,
    AuthenticationError,
    ValidationError,
    NotFoundError,
    RateLimitError,
    InsufficientBalanceError,
)

# Import models
from .models.user import UserDto, UpdateUserDto, UserKycInfoDto, VerifyBvnDto, UserResponseDto, UpdateUserResponseDto
from .models.wallet import (
    UserWalletDto, FundWalletByNairaDto, DepositResponseDto,
    WithdrawWalletDto, PeerTransferDto, BankDto, BankAccountDto,UserWalletResponseDto, GetNairaWalletResponseDto, NairaWalletDto, FundwalletResponseDto, VerifyBankAccountRequestDto, BankListResponseDto,
    VirtualAccountDto, CreateVirtualAccountDto,AddCardDto, AddUssdDto, DepositDto, DepositNextActionDto, PaymentDto, Customer, Customization, InitiateBankTransferDto, InitiateBankTransferResponseDto,InitiateBankTransferResponseDataDto,
    DepositWithPaymentMethodDto, DepositWithPaymentMethodResponseDto, PaymentMethodNextActionDto, PaymentResponseDto, DepositAuthResponseDto, DepositAuthDto, FlwAvsAuthDto, FlwBillingAddressDto,GeneratePaymentLinkDto,PaymentLinkDto, PaymentLinkResponseDto,
    StatusResponseDto, InitiateBankTransferDto, InitiateBankTransferResponseDto, InitiateBankTransferResponseDataDto, PeerTransferResponseDto, VerifyBankAccountRequestDto, VerifyBankResponseDto, VerifyBankAccountDto, BankAccountResponseDto, NairaBalanceDto,
    NairaBalanceResponseDto
)
from .models.evm import (
    BalanceDto, UserEvmPortfolioDto, SendNativeTokenDto,SendTokenDto,Response,
    SendNativeTokenResponseDto,BalanceResponseDto, UserTokenBalanceDto,SendTokenResponseDto,
    SupportedChainDto,SupportedChainsResponseDto,UserTokenBalanceDto
    
)
from .models.solana import (
    AddressDto, PortfolioDto, TransferSolDto, TransferTokenDto,
    SignatureDto, SolanaNetwork,BalanceDto,WalletAddressResponseDto,BalanceResponseDto,TokenInfoDto,PortfolioResponseDto,
    SignatureResponseDto
)
from .models.transactions import TransactionResponseDto, TransactionDto,UserTransactionsResponseDto,UserTransactionsDataDto,PaginationDto,TransactionsRequestDto


from .models.offramp import (
    OframpQuoteRequestDto,AssetsResponseDto,OfframpExchangeRateDto,OframpQuoteResponseDto,SwapCryptoToFiatRequestDto,CryptoAmountDto,FiatAmountDto,AmountsDto,
    BeneficiaryDto,OnChainDto,TimestampsDto,OfframpOrderResponseDataDto,OfframpOrderResponseDto,PayoutBankDto,PayoutBanksResponseDto,VerifyOfframpBankAccountResponseDataDto,
    VerifyOfframpBankAccountResponseDto,VerifyOfframpBankAccountRequestDto,OfframpHistoryRequestDto,OfframpTransactionResponseDto,TransactionBeneficiaryDto,MetaDto,
    OfframpTransactionListResponseDto,OfframpTransactionDetailResponseDto,OfframpStatusRequestDto

)

from .models.payment_method import (
    Capabilities,PaymentMethodDetailsDto,PaymentMethodDto,SyncPaymentMethodsDto,CreatePaymentMethodDto,AddUssdDto,AddCardDto,
    PaymentMethodResponseDto,PaymentMethodsResponseDto,DeletePaymentMethodResponseDto
    
)


from .models.bills import (
    BillerDto, AirtimePurchaseDto, DataPurchaseDto,ElectricityPaymentDto, CableTvPaymentDto,
    BillPaymentDto, BillDto, BillCategory,ElectricityBillerDto,ElectricityBillerResponseDto,BillerItemsResponseDto,ValidateBillDto,
    BillPaymentResponseDto,BillHistoryDto,BillHistoryResponseDto,BillResponseDto,BillNotFoundResponseDto,UserInfoDto,MetadataDto,BillTransactionResponseDto
)

from .models.exchange import (
    SwapNativeToTokenDto, SwapTokenToTokenDto, SwapTokenToNativeDto,
    SwapSolToTokenDto, SwapPriceDto, SwapDto, TxHashDto,EvmSwapTokenToTokenDto,SwapTokenToSolDto,TokenDto,SwapPriceResponseDto,
    TxHashResponseDto,SwapQuoteResponseDto,SwapQuoteDto,SwapTokenInfoDto,SwapAmountsDto,SwapRatesDto,SwapFeesDto,SwapRouteDto,
    UsdValuesDto,SwapResponseDto

)

from .models.agent import (
    AgentChatRequestDto, AgentStreamRequestDto, GuestAgentRequestDto,
    AgentChatResponseDto, ConversationListResponseDto,
    ConversationMessagesResponseDto, CreateConversationDto, PinConversationDto
)

from .models.beneficiaries import (
    BeneficiaryDto, CreateBeneficiaryDto, UpdateBeneficiaryDto,
    TransferToBeneficiaryDto, BeneficiaryType,
    CreateMobileBeneficiaryDto, CreateElectricityBeneficiaryDto,
    CreateCableTvBeneficiaryDto, UpdateBillBeneficiaryDto
)

__version__ = "0.1.0"
__all__ = [
    "MoneiClient",
    "MoneiAPIError",
    "AuthenticationError", 
    "ValidationError",
    "NotFoundError",
    "RateLimitError",
    "InsufficientBalanceError",
    # Models
    "UserDto", "UpdateUserDto", "UserKycInfoDto", "VerifyBvnDto","UpdateUserResponseDto","UserResponseDto",
    "UserWalletDto", "FundWalletByNairaDto", "DepositResponseDto","InitiateBankTransferResponseDataDto","DepositWithPaymentMethodDto",
    "WithdrawWalletDto", "PeerTransferDto", "BankDto", "BankAccountDto","UserWalletResponseDto", "GetNairaWalletResponseDto","NairaWalletDto", 
    "FundwalletResponseDto", "VerifyBankAccountRequestDto", "BankListResponseDto","InitiateBankTransferDto", "InitiateBankTransferResponseDto",
    "VirtualAccountDto", "CreateVirtualAccountDto","AddCardDto", "AddUssdDto", "DepositDto", "DepositNextActionDto", "PaymentDto", "Customer", "Customization", 
    "DepositWithPaymentMethodResponseDto", "PaymentMethodNextActionDto", "PaymentResponseDto", "DepositAuthResponseDto", "DepositAuthDto", "FlwAvsAuthDto", 
    "GeneratePaymentLinkDto","PaymentLinkDto", "PaymentLinkResponseDto", "StatusResponseDto", "InitiateBankTransferDto", "InitiateBankTransferResponseDto",
    "InitiateBankTransferResponseDataDto", "PeerTransferResponseDto", "VerifyBankAccountRequestDto", "VerifyBankResponseDto", "VerifyBankAccountDto",
    "BankAccountResponseDto", "NairaBalanceDto","FlwBillingAddressDto","NairaBalanceResponseDto", 

    "BalanceDto", "UserEvmPortfolioDto", "SendNativeTokenDto","SendNativeTokenResponseDto","BalanceResponseDto", "UserTokenBalanceDto","SendTokenResponseDto",
    "SendTokenDto", "Response","SupportedChainDto","SupportedChainsResponseDto","UserTokenBalanceDto",

    "AddressDto", "PortfolioDto", "TransferSolDto", "TransferTokenDto","SignatureResponseDto",
    "SignatureDto", "SolanaNetwork","WalletAddressResponseDto","BalanceResponseDto","TokenInfoDto","PortfolioResponseDto",
    
    "TransactionResponseDto", "TransactionDto","UserTransactionsResponseDto","UserTransactionsDataDto","PaginationDto","TransactionsRequestDto",

    "OframpQuoteRequestDto","AssetsResponseDto","OfframpExchangeRateDto","OframpQuoteResponseDto","SwapCryptoToFiatRequestDto","CryptoAmountDto","FiatAmountDto","AmountsDto",
    "BeneficiaryDto","OnChainDto","TimestampsDto","OfframpOrderResponseDataDto","OfframpOrderResponseDto","PayoutBankDto","PayoutBanksResponseDto","VerifyOfframpBankAccountResponseDataDto",
    "VerifyOfframpBankAccountResponseDto","VerifyOfframpBankAccountRequestDto","OfframpHistoryRequestDto","OfframpTransactionResponseDto","TransactionBeneficiaryDto","MetaDto",
    "OfframpTransactionListResponseDto","OfframpTransactionDetailResponseDto","OfframpStatusRequestDto",

    "Capabilities","PaymentMethodDetailsDto","PaymentMethodDto","SyncPaymentMethodsDto","CreatePaymentMethodDto","AddUssdDto","AddCardDto",
    "PaymentMethodResponseDto","PaymentMethodsResponseDto","DeletePaymentMethodResponseDto",

    "BillerDto", "AirtimePurchaseDto", "DataPurchaseDto","ElectricityPaymentDto", "CableTvPaymentDto", "BillPaymentDto", "BillDto",
    "BillCategory","ElectricityBillerDto","ElectricityBillerResponseDto","BillerItemsResponseDto","ValidateBillDto","BillPaymentResponseDto",
    "BillHistoryDto","BillHistoryResponseDto","BillResponseDto","BillNotFoundResponseDto","UserInfoDto","MetadataDto","BillTransactionResponseDto",

    "SwapNativeToTokenDto", "SwapTokenToTokenDto", "SwapTokenToNativeDto", "EvmSwapTokenToTokenDto","TokenDto","SwapPriceResponseDto","UsdValuesDto",
    "SwapSolToTokenDto", "SwapPriceDto", "SwapDto", "TxHashDto","SwapTokenToSolDto","SwapResponseDto","SwapRouteDto",
    "TxHashResponseDto","SwapQuoteResponseDto","SwapQuoteDto","SwapTokenInfoDto","SwapAmountsDto","SwapRatesDto","SwapFeesDto",

    "AgentChatRequestDto", "AgentStreamRequestDto", "GuestAgentRequestDto",
    "AgentChatResponseDto", "ConversationListResponseDto",
    "ConversationMessagesResponseDto", "CreateConversationDto", "PinConversationDto"
    "BeneficiaryDto", "CreateBeneficiaryDto", "UpdateBeneficiaryDto",
    "TransferToBeneficiaryDto", "BeneficiaryType",
    "CreateMobileBeneficiaryDto", "CreateElectricityBeneficiaryDto", 
    "CreateCableTvBeneficiaryDto", "UpdateBillBeneficiaryDto"
]