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


class RequiredDateTimeComponent(TypedDict):
    pass

class OptionalDateTimeComponent(TypedDict, total=False):
    # The day of month
    day_of_month: int

    # Both strings and numbers are accepted. If different from the value derived from the date (if specified), use the derived value.
    day_of_week: int

    # The hour
    hour: int

    # The minute
    minute: int

    # The month
    month: int

    # The year
    year: int

class DateTimeComponent(RequiredDateTimeComponent, OptionalDateTimeComponent):
    pass
