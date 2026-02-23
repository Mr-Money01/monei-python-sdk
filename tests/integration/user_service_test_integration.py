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
        user = await self.client.user.get_me()
        logger.info(f"User info: {user}")
        assert user is not None
        

    
    async def test_update_user(self):
        update_data = UpdateUserDto(first_name="Test", last_name="User")
        message = await self.client.user.update(self.test_user_id, update_data)
        logger.info(f"Update user response: {message}")
        

    
