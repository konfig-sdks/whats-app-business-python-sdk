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


class WebhookContact(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def profile() -> typing.Type['WebhookContactProfile']:
                return WebhookContactProfile
            wa_id = schemas.StrSchema
            __annotations__ = {
                "profile": profile,
                "wa_id": wa_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile"]) -> 'WebhookContactProfile': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wa_id"]) -> MetaOapg.properties.wa_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["profile", "wa_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile"]) -> typing.Union['WebhookContactProfile', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wa_id"]) -> typing.Union[MetaOapg.properties.wa_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["profile", "wa_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        profile: typing.Union['WebhookContactProfile', schemas.Unset] = schemas.unset,
        wa_id: typing.Union[MetaOapg.properties.wa_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebhookContact':
        return super().__new__(
            cls,
            *args,
            profile=profile,
            wa_id=wa_id,
            _configuration=_configuration,
            **kwargs,
        )

from whats_app_business_python_sdk.model.webhook_contact_profile import WebhookContactProfile
