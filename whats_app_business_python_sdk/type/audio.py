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

from whats_app_business_python_sdk.type.audio_by_id import AudioById
from whats_app_business_python_sdk.type.audio_by_provider import AudioByProvider

Audio = typing.Union[AudioById,AudioByProvider]
Audio = object