# coding: utf-8

"""
    WhatsApp Business API

    See https://developers.facebook.com/docs/whatsapp

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from whats_app_business_python_sdk.pydantic.business_profile_websites import BusinessProfileWebsites

class BusinessProfile(BaseModel):
    # Description of the business Maximum of 256 characters
    description: str = Field(alias='description')

    # Address of the business Maximum of 256 characters
    address: str = Field(alias='address')

    # Email address to contact the business Maximum of 128 characters
    email: str = Field(alias='email')

    # Industry of the business Maximum of 128 characters
    vertical: str = Field(alias='vertical')

    websites: BusinessProfileWebsites = Field(alias='websites')
    class Config:
        arbitrary_types_allowed = True
