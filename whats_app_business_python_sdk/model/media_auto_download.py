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


class MediaAutoDownload(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    An array specifying which types of media to automatically download.
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "audio": "AUDIO",
                    "document": "DOCUMENT",
                    "voice": "VOICE",
                    "video": "VIDEO",
                    "image.": "IMAGE_",
                }
            
            @schemas.classproperty
            def AUDIO(cls):
                return cls("audio")
            
            @schemas.classproperty
            def DOCUMENT(cls):
                return cls("document")
            
            @schemas.classproperty
            def VOICE(cls):
                return cls("voice")
            
            @schemas.classproperty
            def VIDEO(cls):
                return cls("video")
            
            @schemas.classproperty
            def IMAGE_(cls):
                return cls("image.")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MediaAutoDownload':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
