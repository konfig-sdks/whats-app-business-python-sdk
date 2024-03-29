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


class WebhookSystem(BaseModel):
    body: typing.Optional[str] = Field(None, alias='body')

    type: typing.Optional[Literal["group_created", "group_user_promoted", "group_user_demoted", "group_user_joined", "group_user_left", "group_subject_changed", "group_description_changed", "group_icon_changed", "group_icon_deleted", "group_invite_link_revoked", "user_identity_changed", "group_user_changed_number", "group_error_fetching_photo", "group_error_adding_users", "group_error_adding_user", "group_error_full_adding_users", "group_error_removing_user", "broadcast_list_created", "group_ended", "group_error_blocked_adding_user"]] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
