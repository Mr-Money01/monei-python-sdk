import os
import pytest
import logging
from monei.models.user import UpdateUserDto, UpdateUserResponseDto

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.integration


@pytest.mark.asyncio
class TestUserService:

    @pytest.fixture(autouse=True)
    async def _setup(self, monei_client):
        self.client = monei_client
        user = await self.client.user.get_me()
        self.test_user_id = user.data.id
        logger.info(f"User id: {self.test_user_id}")
        

    async def test_get_me(self):
        result = await self.client.user.get_me()
        logger.info(f"User info: {result}")
        # === ASSERT BASE RESPONSE ===
        assert "statusCode" in result
        assert "message" in result
        assert "data" in result

        # === VERIFY USER DATA STRUCTURE ===
        user = result["data"]

        assert "id" in user
        assert "email" in user
        assert "firstName" in user
        assert "lastName" in user
        assert "kycInfo" in user

        assert isinstance(user["id"], int)
        assert isinstance(user["email"], str)
        assert isinstance(user["firstName"], str)
        assert isinstance(user["lastName"], str)

        # kycInfo could be dict or None depending on API
        assert user["kycInfo"] is None or isinstance(user["kycInfo"], dict)

        logger.info("Actual user data: %s", {
            "id": user["id"],
            "email": user["email"],
            "name": user["name"],
            "verified": user["verified"],
        })
        

    
    async def test_update_user(self):
        update_data = UpdateUserDto(first_name="Test", last_name="User")
        result = await self.client.user.update(self.test_user_id, update_data)
        #logger.info(f"Update user response: {message}")
        # === BASE ASSERT ===
        assert result["statusCode"] == 200

        # === DATA ASSERT ===
        user = result["data"]

        assert user["firstName"] == update_data.first_name
        assert user["lastName"] == update_data.last_name
        

    
