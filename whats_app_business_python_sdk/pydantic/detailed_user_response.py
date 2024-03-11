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

from whats_app_business_python_sdk.pydantic.detailed_user_response_item import DetailedUserResponseItem
from whats_app_business_python_sdk.pydantic.response import Response

DetailedUserResponse = typing.Union[Response,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
DetailedUserResponse = object
