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


class RequiredOrg(TypedDict):
    # Name of the contact's company
    company: str

class OptionalOrg(TypedDict, total=False):
    # Contact's business title
    title: str

    # Name of the contact's department
    department: str

class Org(RequiredOrg, OptionalOrg):
    pass
