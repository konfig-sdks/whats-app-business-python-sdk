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


class WebhookVideo(BaseModel):
    # Optional. Only present if specified.
    caption: typing.Optional[str] = Field(None, alias='caption')

    # Absolute filename and location on media volume. This parameter is deprecated.
    file: typing.Optional[str] = Field(None, alias='file')

    # ID of the media. Can be used to delete the media if stored locally on the client.
    id: typing.Optional[str] = Field(None, alias='id')

    link: typing.Optional[str] = Field(None, alias='link')

    # Mime type of media
    mime_type: typing.Optional[str] = Field(None, alias='mime_type')

    # Checksum
    sha256: typing.Optional[str] = Field(None, alias='sha256')
    class Config:
        arbitrary_types_allowed = True
