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

from whats_app_business_python_sdk.type.currency import Currency
from whats_app_business_python_sdk.type.date_time_object import DateTimeObject

class RequiredLocalizableParam(TypedDict):
    # Default text if localization fails
    default: str

class OptionalLocalizableParam(TypedDict, total=False):
    currency: Currency

    date_time: DateTimeObject

class LocalizableParam(RequiredLocalizableParam, OptionalLocalizableParam):
    pass
