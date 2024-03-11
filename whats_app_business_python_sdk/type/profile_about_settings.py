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

from whats_app_business_python_sdk.type.profile_about_settings_profile import ProfileAboutSettingsProfile

class RequiredProfileAboutSettings(TypedDict):
    pass

class OptionalProfileAboutSettings(TypedDict, total=False):
    profile: ProfileAboutSettingsProfile

class ProfileAboutSettings(RequiredProfileAboutSettings, OptionalProfileAboutSettings):
    pass