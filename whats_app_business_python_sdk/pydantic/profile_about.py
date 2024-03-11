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


class ProfileAbout(BaseModel):
    # Text to display in your profile's About section The max length for the string is 139 characters.
    text: str = Field(alias='text')
    class Config:
        arbitrary_types_allowed = True