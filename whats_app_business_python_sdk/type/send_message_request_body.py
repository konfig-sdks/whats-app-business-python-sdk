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

from whats_app_business_python_sdk.type.audio import Audio
from whats_app_business_python_sdk.type.contact import Contact
from whats_app_business_python_sdk.type.document import Document
from whats_app_business_python_sdk.type.hsm import Hsm
from whats_app_business_python_sdk.type.image import Image
from whats_app_business_python_sdk.type.location import Location
from whats_app_business_python_sdk.type.message_type import MessageType
from whats_app_business_python_sdk.type.text import Text
from whats_app_business_python_sdk.type.video import Video

class RequiredSendMessageRequestBody(TypedDict):
    # When recipient_type is individual, this field is the WhatsApp ID (phone number) returned from contacts endpoint. When recipient_type is group, this field is the WhatsApp group ID.
    to: str

class OptionalSendMessageRequestBody(TypedDict, total=False):
    audio: Audio

    contacts: typing.List[Contact]

    document: Document

    hsm: Hsm

    image: Image

    location: Location

    # Specifying preview_url in the request is optional when not including a URL in your message. To include a URL preview, set preview_url to true in the message body and make sure the URL begins with http:// or https://. For more information, see the Sending URLs in Text Messages section.
    preview_url: bool

    # Determines whether the recipient is an individual or a group Specifying recipient_type in the request is optional when the value is individual. However, recipient_type is required when using group. If sending a text message to a group, see the Sending Group Messages documentation.
    recipient_type: str

    text: Text

    ttl: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    type: MessageType

    video: Video

class SendMessageRequestBody(RequiredSendMessageRequestBody, OptionalSendMessageRequestBody):
    pass