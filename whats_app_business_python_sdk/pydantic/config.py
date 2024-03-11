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

from whats_app_business_python_sdk.pydantic.config_basic import ConfigBasic
from whats_app_business_python_sdk.pydantic.config_bearer import ConfigBearer

Config = typing.Union[ConfigBearer,ConfigBasic]
