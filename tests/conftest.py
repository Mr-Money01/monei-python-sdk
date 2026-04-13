import sys
import asyncio
import os
import pytest
from dotenv import load_dotenv
from monei.client import MoneiClient

# -----------------------------
# Windows-safe event loop policy
# -----------------------------
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
API_KEY = os.getenv("MONEI_API_KEY2")
BASE_URL = os.getenv("BASE_URL")

DEV_API_KEY = os.getenv("DEV_API_KEY")
DEV_BASE_URL = os.getenv("DEV_BASE_URL")

SANDBOX_API_KEY = os.getenv("SANDBOX_API_KEY")

assert API_KEY, "Missing API_KEY in .env"
assert BASE_URL, "Missing BASE_URL in .env"
assert DEV_API_KEY, "Missing DEV_API_KEY in .env"
assert DEV_BASE_URL, "Missing DEV_BASE_URL in .env"
assert SANDBOX_API_KEY, "Missing SANDBOX_API_KEY in .env"

# -----------------------------
# Main Monei client fixture
# -----------------------------
@pytest.fixture
async def monei_client():
    """Function-scoped client for Windows-safe async tests."""
    client = MoneiClient(api_key=SANDBOX_API_KEY, base_url=BASE_URL)
    yield client
    await client.close()

# -----------------------------
# Service fixtures
# -----------------------------
@pytest.fixture
async def evm_service(monei_client):
    yield monei_client.evm

@pytest.fixture
async def wallet_service(monei_client):
    yield monei_client.wallet

@pytest.fixture
async def user_service(monei_client):
    yield monei_client.user

@pytest.fixture
async def solana_service(monei_client):
    yield monei_client.solana

@pytest.fixture
async def exchange_service(monei_client):
    yield monei_client.exchange

@pytest.fixture
async def evm_exchange_service(monei_client):
    yield monei_client.evm_exchange

@pytest.fixture
async def sol_exchange_service(monei_client):
    yield monei_client.sol_exchange

@pytest.fixture
async def bill_service(monei_client):
    yield monei_client.bills

@pytest.fixture
async def agent_service(monei_client):
    yield monei_client.agent

@pytest.fixture
async def transaction_service(monei_client):
    yield monei_client.transactions

@pytest.fixture
async def kyc_service(monei_client):
    yield monei_client.kyc

@pytest.fixture
async def payment_method_service(monei_client):
    yield monei_client.payment_methods

@pytest.fixture
async def offramp_exchange_service(monei_client):
    yield monei_client.offramp_exchange

@pytest.fixture
async def offramp_payouts_service(monei_client):
    yield monei_client.offramp_payouts

@pytest.fixture
async def offramp_ledger_service(monei_client):
    yield monei_client.offramp_ledger

@pytest.fixture
async def wallet_account_service(monei_client):
    yield monei_client.account

@pytest.fixture
async def wallet_deposit_service(monei_client):
    yield monei_client.deposit

@pytest.fixture
async def wallet_payout_service(monei_client):
    yield monei_client.payout

@pytest.fixture
async def wallet_utility_service(monei_client):
    yield monei_client.utility

@pytest.fixture
async def bill_discovery_service(monei_client):
    yield monei_client.bill_discovery

@pytest.fixture
async def bill_pay_service(monei_client):
    yield monei_client.bill_pay

@pytest.fixture
async def bill_record_service(monei_client):
    yield monei_client.bill_record

@pytest.fixture
async def bill_validate_service(monei_client):
    yield monei_client.bill_validate


@pytest.fixture
async def business_service(monei_client):
    yield monei_client.business_service