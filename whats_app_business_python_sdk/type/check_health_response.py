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

from whats_app_business_python_sdk.type.gateway_node_status import GatewayNodeStatus
from whats_app_business_python_sdk.type.gateway_status import GatewayStatus

class RequiredCheckHealthResponse(TypedDict):
    pass

class OptionalCheckHealthResponse(TypedDict, total=False):
    health: typing.Union[GatewayStatus, typing.Dict[str, GatewayNodeStatus]]

class CheckHealthResponse(RequiredCheckHealthResponse, OptionalCheckHealthResponse):
    pass