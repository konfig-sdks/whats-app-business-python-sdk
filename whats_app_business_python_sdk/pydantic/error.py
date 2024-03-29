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


class Error(BaseModel):
    # error title
    title: typing.Optional[str] = Field(None, alias='title')

    # See the https://developers.facebook.com/docs/whatsapp/api/errors for more information.
    code: typing.Optional[int] = Field(None, alias='code')

    # error detail
    details: typing.Optional[str] = Field(None, alias='details')

    # location for error detail
    href: typing.Optional[str] = Field(None, alias='href')
    class Config:
        arbitrary_types_allowed = True
