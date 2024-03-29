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


class RequiredProvider(TypedDict):
    name: str

class OptionalProvider(TypedDict, total=False):
    pass

class Provider(RequiredProvider, OptionalProvider):
    pass
