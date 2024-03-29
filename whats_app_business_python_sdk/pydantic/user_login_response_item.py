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


class UserLoginResponseItem(BaseModel):
    # Token expiration timestamp. By default, this is 7 days.
    expires_after: typing.Optional[datetime] = Field(None, alias='expires_after')

    # Authentication token to be used for all other WhatsApp Business API calls. The token must be sent in the authorization header in the format: Authorization: Bearer <authentication-token>
    token: typing.Optional[str] = Field(None, alias='token')
    class Config:
        arbitrary_types_allowed = True
