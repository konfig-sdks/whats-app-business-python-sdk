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


class RequiredCheckContact(TypedDict):
    pass

class OptionalCheckContact(TypedDict, total=False):
    # The value you sent in the contacts field of the JSON request.
    input: str

    # Status of the user.
    status: str

    # WhatsApp user identifier that can be used in other API calls. Only returned if the status is valid.
    wa_id: str

class CheckContact(RequiredCheckContact, OptionalCheckContact):
    pass
