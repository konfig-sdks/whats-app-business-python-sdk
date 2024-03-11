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


class DateTimeComponent(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Date/time by component
    """


    class MetaOapg:
        
        class properties:
            day_of_month = schemas.Int32Schema
            
            
            class day_of_week(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    enum_value_to_name = {
                        1: "MONDAY",
                        2: "TUESDAY",
                        3: "WEDNESDAY",
                        4: "THURSDAY",
                        5: "FRIDAY",
                        6: "SATURDAY",
                        7: "SUNDAY",
                    }
                
                @schemas.classproperty
                def MONDAY(cls):
                    return cls(1)
                
                @schemas.classproperty
                def TUESDAY(cls):
                    return cls(2)
                
                @schemas.classproperty
                def WEDNESDAY(cls):
                    return cls(3)
                
                @schemas.classproperty
                def THURSDAY(cls):
                    return cls(4)
                
                @schemas.classproperty
                def FRIDAY(cls):
                    return cls(5)
                
                @schemas.classproperty
                def SATURDAY(cls):
                    return cls(6)
                
                @schemas.classproperty
                def SUNDAY(cls):
                    return cls(7)
            hour = schemas.Int32Schema
            minute = schemas.Int32Schema
            month = schemas.Int32Schema
            year = schemas.Int32Schema
            __annotations__ = {
                "day_of_month": day_of_month,
                "day_of_week": day_of_week,
                "hour": hour,
                "minute": minute,
                "month": month,
                "year": year,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["day_of_month"]) -> MetaOapg.properties.day_of_month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["day_of_week"]) -> MetaOapg.properties.day_of_week: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hour"]) -> MetaOapg.properties.hour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minute"]) -> MetaOapg.properties.minute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["month"]) -> MetaOapg.properties.month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["year"]) -> MetaOapg.properties.year: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["day_of_month", "day_of_week", "hour", "minute", "month", "year", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["day_of_month"]) -> typing.Union[MetaOapg.properties.day_of_month, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["day_of_week"]) -> typing.Union[MetaOapg.properties.day_of_week, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hour"]) -> typing.Union[MetaOapg.properties.hour, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minute"]) -> typing.Union[MetaOapg.properties.minute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["month"]) -> typing.Union[MetaOapg.properties.month, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["year"]) -> typing.Union[MetaOapg.properties.year, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["day_of_month", "day_of_week", "hour", "minute", "month", "year", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        day_of_month: typing.Union[MetaOapg.properties.day_of_month, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        day_of_week: typing.Union[MetaOapg.properties.day_of_week, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hour: typing.Union[MetaOapg.properties.hour, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        minute: typing.Union[MetaOapg.properties.minute, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        month: typing.Union[MetaOapg.properties.month, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        year: typing.Union[MetaOapg.properties.year, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DateTimeComponent':
        return super().__new__(
            cls,
            *args,
            day_of_month=day_of_month,
            day_of_week=day_of_week,
            hour=hour,
            minute=minute,
            month=month,
            year=year,
            _configuration=_configuration,
            **kwargs,
        )
