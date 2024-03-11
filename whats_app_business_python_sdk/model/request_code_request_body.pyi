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


class RequestCodeRequestBody(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "cc",
            "method",
            "cert",
            "phone_number",
        }
        
        class properties:
            cc = schemas.StrSchema
            cert = schemas.StrSchema
            
            
            class method(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SMS(cls):
                    return cls("sms")
                
                @schemas.classproperty
                def VOICE(cls):
                    return cls("voice")
            phone_number = schemas.StrSchema
            pin = schemas.StrSchema
            __annotations__ = {
                "cc": cc,
                "cert": cert,
                "method": method,
                "phone_number": phone_number,
                "pin": pin,
            }
    
    cc: MetaOapg.properties.cc
    method: MetaOapg.properties.method
    cert: MetaOapg.properties.cert
    phone_number: MetaOapg.properties.phone_number
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cc"]) -> MetaOapg.properties.cc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cert"]) -> MetaOapg.properties.cert: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pin"]) -> MetaOapg.properties.pin: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cc", "cert", "method", "phone_number", "pin", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cc"]) -> MetaOapg.properties.cc: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cert"]) -> MetaOapg.properties.cert: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pin"]) -> typing.Union[MetaOapg.properties.pin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cc", "cert", "method", "phone_number", "pin", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cc: typing.Union[MetaOapg.properties.cc, str, ],
        method: typing.Union[MetaOapg.properties.method, str, ],
        cert: typing.Union[MetaOapg.properties.cert, str, ],
        phone_number: typing.Union[MetaOapg.properties.phone_number, str, ],
        pin: typing.Union[MetaOapg.properties.pin, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RequestCodeRequestBody':
        return super().__new__(
            cls,
            *args,
            cc=cc,
            method=method,
            cert=cert,
            phone_number=phone_number,
            pin=pin,
            _configuration=_configuration,
            **kwargs,
        )