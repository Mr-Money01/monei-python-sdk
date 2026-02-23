""""""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from .base import BaseDto
from enum import Enum


class CreateCustomerDto(BaseModel):
    """"""
    name: str 
    phone: str  
    email: str
    externalRef: str


class UpdateCustomerDto(BaseModel):
    """"""
    name: str 
    phone: str  
    email: str
    externalRef: str