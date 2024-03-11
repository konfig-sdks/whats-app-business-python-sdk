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

from whats_app_business_python_sdk.pydantic.contact import Contact
from whats_app_business_python_sdk.pydantic.error import Error
from whats_app_business_python_sdk.pydantic.message_context import MessageContext
from whats_app_business_python_sdk.pydantic.message_type import MessageType
from whats_app_business_python_sdk.pydantic.webhook_audio import WebhookAudio
from whats_app_business_python_sdk.pydantic.webhook_document import WebhookDocument
from whats_app_business_python_sdk.pydantic.webhook_image import WebhookImage
from whats_app_business_python_sdk.pydantic.webhook_location import WebhookLocation
from whats_app_business_python_sdk.pydantic.webhook_system import WebhookSystem
from whats_app_business_python_sdk.pydantic.webhook_text import WebhookText
from whats_app_business_python_sdk.pydantic.webhook_video import WebhookVideo
from whats_app_business_python_sdk.pydantic.webhook_voice import WebhookVoice

class WebhookMessage(BaseModel):
    audio: typing.Optional[WebhookAudio] = Field(None, alias='audio')

    contacts: typing.Optional[typing.List[Contact]] = Field(None, alias='contacts')

    context: typing.Optional[MessageContext] = Field(None, alias='context')

    document: typing.Optional[WebhookDocument] = Field(None, alias='document')

    errors: typing.Optional[typing.List[Error]] = Field(None, alias='errors')

    # WhatsApp ID of the sender
    from_: typing.Optional[str] = Field(None, alias='from')

    # Optional. WhatsApp group ID
    group_id: typing.Optional[str] = Field(None, alias='group_id')

    # Message ID
    id: typing.Optional[str] = Field(None, alias='id')

    image: typing.Optional[WebhookImage] = Field(None, alias='image')

    location: typing.Optional[WebhookLocation] = Field(None, alias='location')

    system: typing.Optional[WebhookSystem] = Field(None, alias='system')

    text: typing.Optional[WebhookText] = Field(None, alias='text')

    # Message received timestamp
    timestamp: typing.Optional[str] = Field(None, alias='timestamp')

    type: typing.Optional[MessageType] = Field(None, alias='type')

    video: typing.Optional[WebhookVideo] = Field(None, alias='video')

    voice: typing.Optional[WebhookVoice] = Field(None, alias='voice')
    class Config:
        arbitrary_types_allowed = True
