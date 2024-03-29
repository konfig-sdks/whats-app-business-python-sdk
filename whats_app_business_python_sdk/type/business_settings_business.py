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

from whats_app_business_python_sdk.type.business_profile import BusinessProfile

class RequiredBusinessSettingsBusiness(TypedDict):
    pass

class OptionalBusinessSettingsBusiness(TypedDict, total=False):
    profile: BusinessProfile

class BusinessSettingsBusiness(RequiredBusinessSettingsBusiness, OptionalBusinessSettingsBusiness):
    pass
