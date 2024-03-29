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

from whats_app_business_python_sdk.type.business_profile_websites import BusinessProfileWebsites

class RequiredBusinessProfile(TypedDict):
    # Description of the business Maximum of 256 characters
    description: str

    # Address of the business Maximum of 256 characters
    address: str

    # Email address to contact the business Maximum of 128 characters
    email: str

    # Industry of the business Maximum of 128 characters
    vertical: str

    websites: BusinessProfileWebsites

class OptionalBusinessProfile(TypedDict, total=False):
    pass

class BusinessProfile(RequiredBusinessProfile, OptionalBusinessProfile):
    pass
