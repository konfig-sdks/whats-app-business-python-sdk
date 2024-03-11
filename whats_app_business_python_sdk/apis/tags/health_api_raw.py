# coding: utf-8

"""
    WhatsApp Business API

    See https://developers.facebook.com/docs/whatsapp

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from whats_app_business_python_sdk.paths.health.get import CheckStatusRaw
from whats_app_business_python_sdk.paths.stats_app.get import GetAppStatsRaw
from whats_app_business_python_sdk.paths.stats_db.get import GetDbStatsRaw
from whats_app_business_python_sdk.paths.metrics.get import GetMetricsDataRaw
from whats_app_business_python_sdk.paths.support.get import GetSupportInfoRaw


class HealthApiRaw(
    CheckStatusRaw,
    GetAppStatsRaw,
    GetDbStatsRaw,
    GetMetricsDataRaw,
    GetSupportInfoRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
