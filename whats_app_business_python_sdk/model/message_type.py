# coding: utf-8

"""
    WhatsApp Business API

    See https://developers.facebook.com/docs/whatsapp

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from whats_app_business_python_sdk import schemas  # noqa: F401


class MessageType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    type of the message
    """


    class MetaOapg:
        enum_value_to_name = {
            "audio": "AUDIO",
            "contacts": "CONTACTS",
            "document": "DOCUMENT",
            "hsm": "HSM",
            "image": "IMAGE",
            "location": "LOCATION",
            "text": "TEXT",
            "video": "VIDEO",
            "voice": "VOICE",
            "unknown": "UNKNOWN",
        }
    
    @schemas.classproperty
    def AUDIO(cls):
        return cls("audio")
    
    @schemas.classproperty
    def CONTACTS(cls):
        return cls("contacts")
    
    @schemas.classproperty
    def DOCUMENT(cls):
        return cls("document")
    
    @schemas.classproperty
    def HSM(cls):
        return cls("hsm")
    
    @schemas.classproperty
    def IMAGE(cls):
        return cls("image")
    
    @schemas.classproperty
    def LOCATION(cls):
        return cls("location")
    
    @schemas.classproperty
    def TEXT(cls):
        return cls("text")
    
    @schemas.classproperty
    def VIDEO(cls):
        return cls("video")
    
    @schemas.classproperty
    def VOICE(cls):
        return cls("voice")
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("unknown")
