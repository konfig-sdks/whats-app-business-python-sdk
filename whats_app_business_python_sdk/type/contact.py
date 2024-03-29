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

from whats_app_business_python_sdk.type.address import Address
from whats_app_business_python_sdk.type.contact_ims import ContactIms
from whats_app_business_python_sdk.type.email import Email
from whats_app_business_python_sdk.type.name import Name
from whats_app_business_python_sdk.type.org import Org
from whats_app_business_python_sdk.type.phone import Phone
from whats_app_business_python_sdk.type.url import Url

class RequiredContact(TypedDict):
    pass

class OptionalContact(TypedDict, total=False):
    # Full contact address(es)
    addresses: typing.List[Address]

    # YYYY-MM-DD formatted string
    birthday: str

    # Contact email address(es)
    emails: typing.List[Email]

    ims: ContactIms

    name: Name

    org: Org

    # Contact phone number(s)
    phones: typing.List[Phone]

    # Contact URL(s)
    urls: typing.List[Url]

class Contact(RequiredContact, OptionalContact):
    pass
