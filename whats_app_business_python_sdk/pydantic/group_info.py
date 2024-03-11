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

from whats_app_business_python_sdk.pydantic.group_info_admins import GroupInfoAdmins
from whats_app_business_python_sdk.pydantic.group_info_participants import GroupInfoParticipants

class GroupInfo(BaseModel):
    admins: typing.Optional[GroupInfoAdmins] = Field(None, alias='admins')

    # Group creation time
    creation_time: typing.Optional[int] = Field(None, alias='creation_time')

    # ID of the creator of this group
    creator: typing.Optional[str] = Field(None, alias='creator')

    participants: typing.Optional[GroupInfoParticipants] = Field(None, alias='participants')

    # Subject of the group
    subject: typing.Optional[str] = Field(None, alias='subject')
    class Config:
        arbitrary_types_allowed = True
