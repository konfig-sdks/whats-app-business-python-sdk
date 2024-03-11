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


class ImageByProvider(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "provider",
            "link",
            "caption",
        }
        
        class properties:
            caption = schemas.StrSchema
            link = schemas.StrSchema
        
            @staticmethod
            def provider() -> typing.Type['Provider']:
                return Provider
            __annotations__ = {
                "caption": caption,
                "link": link,
                "provider": provider,
            }
    
    provider: 'Provider'
    link: MetaOapg.properties.link
    caption: MetaOapg.properties.caption
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caption"]) -> MetaOapg.properties.caption: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> 'Provider': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["caption", "link", "provider", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caption"]) -> MetaOapg.properties.caption: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> 'Provider': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["caption", "link", "provider", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        provider: 'Provider',
        link: typing.Union[MetaOapg.properties.link, str, ],
        caption: typing.Union[MetaOapg.properties.caption, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ImageByProvider':
        return super().__new__(
            cls,
            *args,
            provider=provider,
            link=link,
            caption=caption,
            _configuration=_configuration,
            **kwargs,
        )

from whats_app_business_python_sdk.model.provider import Provider
