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

from whats_app_business_python_sdk.pydantic.date_time_component import DateTimeComponent
from whats_app_business_python_sdk.pydantic.date_time_unix_epoch import DateTimeUnixEpoch

class DateTimeObject(BaseModel):
    component: typing.Optional[DateTimeComponent] = Field(None, alias='component')

    unix_epoch: typing.Optional[DateTimeUnixEpoch] = Field(None, alias='unix_epoch')
    class Config:
        arbitrary_types_allowed = True