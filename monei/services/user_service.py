"""User service implementation"""

from typing import Dict, Any
from ..models.user import UpdateUserResponseDto, UserDto, UpdateUserDto, UserKycInfoDto, UserResponseDto, VerifyBvnDto
from ..exceptions import MoneiAPIError


class UserService:
    """Service for user operations"""
    
    def __init__(self, client):
        self.client = client
    
    async def get_me(self) -> UserResponseDto:
        """Get current user information"""
        response = await self.client._request("GET", "/user/me")
        return UserResponseDto(**response)
    
    async def update(self, user_id: str, update_data: UpdateUserResponseDto) -> str:
        """Update user information"""
        response = await self.client._request(
            "PATCH", f"/user/update/{user_id}", data=update_data.dict(exclude_none=True)
        )
        return UpdateUserResponseDto(**response)
    
    async def kyc_verify_bvn(self, bvn: str) -> UserKycInfoDto:
        """Verify BVN for KYC"""
        request_data = VerifyBvnDto(bvn=bvn)
        response = await self.client._request(
            "POST", "/wallet/kyc/bvn", data=request_data.dict()
        )
        return UserKycInfoDto(**response['data'])