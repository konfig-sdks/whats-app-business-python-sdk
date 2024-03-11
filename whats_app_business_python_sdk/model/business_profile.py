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


class BusinessProfile(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "address",
            "description",
            "vertical",
            "websites",
            "email",
        }
        
        class properties:
            description = schemas.StrSchema
            address = schemas.StrSchema
            email = schemas.StrSchema
            vertical = schemas.StrSchema
        
            @staticmethod
            def websites() -> typing.Type['BusinessProfileWebsites']:
                return BusinessProfileWebsites
            __annotations__ = {
                "description": description,
                "address": address,
                "email": email,
                "vertical": vertical,
                "websites": websites,
            }
    
    address: MetaOapg.properties.address
    description: MetaOapg.properties.description
    vertical: MetaOapg.properties.vertical
    websites: 'BusinessProfileWebsites'
    email: MetaOapg.properties.email
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vertical"]) -> MetaOapg.properties.vertical: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["websites"]) -> 'BusinessProfileWebsites': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "address", "email", "vertical", "websites", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vertical"]) -> MetaOapg.properties.vertical: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["websites"]) -> 'BusinessProfileWebsites': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "address", "email", "vertical", "websites", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        vertical: typing.Union[MetaOapg.properties.vertical, str, ],
        websites: 'BusinessProfileWebsites',
        email: typing.Union[MetaOapg.properties.email, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BusinessProfile':
        return super().__new__(
            cls,
            *args,
            address=address,
            description=description,
            vertical=vertical,
            websites=websites,
            email=email,
            _configuration=_configuration,
            **kwargs,
        )

from whats_app_business_python_sdk.model.business_profile_websites import BusinessProfileWebsites
