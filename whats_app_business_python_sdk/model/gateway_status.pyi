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


class GatewayStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def CONNECTED(cls):
        return cls("connected")
    
    @schemas.classproperty
    def CONNECTING(cls):
        return cls("connecting")
    
    @schemas.classproperty
    def DISCONNECTED(cls):
        return cls("disconnected")
    
    @schemas.classproperty
    def UNINITIALIZED(cls):
        return cls("uninitialized")
    
    @schemas.classproperty
    def UNREGISTERED(cls):
        return cls("unregistered")
