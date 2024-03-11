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

from whats_app_business_python_sdk.pydantic.backup_settings import BackupSettings

class BackupSettingsResponse(BaseModel):
    settings: typing.Optional[BackupSettings] = Field(None, alias='settings')
    class Config:
        arbitrary_types_allowed = True
