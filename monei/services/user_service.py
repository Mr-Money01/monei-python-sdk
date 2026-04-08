"""User service implementation"""

from typing import Dict, Any
from ..models.user import UpdateUserResponseDto, UserDto, UpdateUserDto, UserKycInfoDto, UserResponseDto, VerifyBvnDto
from ..models.kyc import KycStatusResponseDto,LimitResponseDto
from ..exceptions import MoneiAPIError


class UserService:
    """Service for user operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_current_user(self) -> UserResponseDto:
        """Get current user information"""
        response = await self.client._request("GET", "/user/me")
        return UserResponseDto(**response)
    
    async def update_user(self, user_id: str, update_data: UpdateUserResponseDto) -> str:
        """Update user information"""
        response = await self.client._request(
            "PATCH", f"/user/update/{user_id}", data=update_data.dict(exclude_none=True)
        )
        return UpdateUserResponseDto(**response)
    
    async def get_kyc_status(self) -> KycStatusResponseDto:
        """Get kyc status"""
          
        response = await self.client._request("GET", "/kyc/status")
        return response
    
    async def get_deposit_limit(self) -> LimitResponseDto:

        """Get users limit"""     
        response = await self.client._request("GET", "/kyc/limits")
        return response