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


class RequiredUserLoginResponseItem(TypedDict):
    pass

class OptionalUserLoginResponseItem(TypedDict, total=False):
    # Token expiration timestamp. By default, this is 7 days.
    expires_after: datetime

    # Authentication token to be used for all other WhatsApp Business API calls. The token must be sent in the authorization header in the format: Authorization: Bearer <authentication-token>
    token: str

class UserLoginResponseItem(RequiredUserLoginResponseItem, OptionalUserLoginResponseItem):
    pass
