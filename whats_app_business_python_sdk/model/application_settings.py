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


class ApplicationSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            callback_backoff_delay_ms = schemas.StrSchema
            callback_persist = schemas.BoolSchema
            heartbeat_interval = schemas.IntSchema
            max_callback_backoff_delay_ms = schemas.StrSchema
        
            @staticmethod
            def media() -> typing.Type['Media']:
                return Media
            on_call_pager = schemas.StrSchema
            pass_through = schemas.BoolSchema
            sent_status = schemas.BoolSchema
            unhealthy_interval = schemas.IntSchema
        
            @staticmethod
            def webhooks() -> typing.Type['Webhooks']:
                return Webhooks
            __annotations__ = {
                "callback_backoff_delay_ms": callback_backoff_delay_ms,
                "callback_persist": callback_persist,
                "heartbeat_interval": heartbeat_interval,
                "max_callback_backoff_delay_ms": max_callback_backoff_delay_ms,
                "media": media,
                "on_call_pager": on_call_pager,
                "pass_through": pass_through,
                "sent_status": sent_status,
                "unhealthy_interval": unhealthy_interval,
                "webhooks": webhooks,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callback_backoff_delay_ms"]) -> MetaOapg.properties.callback_backoff_delay_ms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callback_persist"]) -> MetaOapg.properties.callback_persist: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heartbeat_interval"]) -> MetaOapg.properties.heartbeat_interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_callback_backoff_delay_ms"]) -> MetaOapg.properties.max_callback_backoff_delay_ms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["media"]) -> 'Media': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["on_call_pager"]) -> MetaOapg.properties.on_call_pager: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pass_through"]) -> MetaOapg.properties.pass_through: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sent_status"]) -> MetaOapg.properties.sent_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unhealthy_interval"]) -> MetaOapg.properties.unhealthy_interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhooks"]) -> 'Webhooks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["callback_backoff_delay_ms", "callback_persist", "heartbeat_interval", "max_callback_backoff_delay_ms", "media", "on_call_pager", "pass_through", "sent_status", "unhealthy_interval", "webhooks", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callback_backoff_delay_ms"]) -> typing.Union[MetaOapg.properties.callback_backoff_delay_ms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callback_persist"]) -> typing.Union[MetaOapg.properties.callback_persist, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heartbeat_interval"]) -> typing.Union[MetaOapg.properties.heartbeat_interval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_callback_backoff_delay_ms"]) -> typing.Union[MetaOapg.properties.max_callback_backoff_delay_ms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["media"]) -> typing.Union['Media', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["on_call_pager"]) -> typing.Union[MetaOapg.properties.on_call_pager, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pass_through"]) -> typing.Union[MetaOapg.properties.pass_through, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sent_status"]) -> typing.Union[MetaOapg.properties.sent_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unhealthy_interval"]) -> typing.Union[MetaOapg.properties.unhealthy_interval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhooks"]) -> typing.Union['Webhooks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["callback_backoff_delay_ms", "callback_persist", "heartbeat_interval", "max_callback_backoff_delay_ms", "media", "on_call_pager", "pass_through", "sent_status", "unhealthy_interval", "webhooks", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        callback_backoff_delay_ms: typing.Union[MetaOapg.properties.callback_backoff_delay_ms, str, schemas.Unset] = schemas.unset,
        callback_persist: typing.Union[MetaOapg.properties.callback_persist, bool, schemas.Unset] = schemas.unset,
        heartbeat_interval: typing.Union[MetaOapg.properties.heartbeat_interval, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        max_callback_backoff_delay_ms: typing.Union[MetaOapg.properties.max_callback_backoff_delay_ms, str, schemas.Unset] = schemas.unset,
        media: typing.Union['Media', schemas.Unset] = schemas.unset,
        on_call_pager: typing.Union[MetaOapg.properties.on_call_pager, str, schemas.Unset] = schemas.unset,
        pass_through: typing.Union[MetaOapg.properties.pass_through, bool, schemas.Unset] = schemas.unset,
        sent_status: typing.Union[MetaOapg.properties.sent_status, bool, schemas.Unset] = schemas.unset,
        unhealthy_interval: typing.Union[MetaOapg.properties.unhealthy_interval, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        webhooks: typing.Union['Webhooks', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicationSettings':
        return super().__new__(
            cls,
            *args,
            callback_backoff_delay_ms=callback_backoff_delay_ms,
            callback_persist=callback_persist,
            heartbeat_interval=heartbeat_interval,
            max_callback_backoff_delay_ms=max_callback_backoff_delay_ms,
            media=media,
            on_call_pager=on_call_pager,
            pass_through=pass_through,
            sent_status=sent_status,
            unhealthy_interval=unhealthy_interval,
            webhooks=webhooks,
            _configuration=_configuration,
            **kwargs,
        )

from whats_app_business_python_sdk.model.media import Media
from whats_app_business_python_sdk.model.webhooks import Webhooks
