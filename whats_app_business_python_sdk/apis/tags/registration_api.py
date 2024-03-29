# coding: utf-8

"""
    WhatsApp Business API

    See https://developers.facebook.com/docs/whatsapp

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from whats_app_business_python_sdk.paths.account.post import RequestCode
from whats_app_business_python_sdk.paths.account_verify.post import VerifyAccount
from whats_app_business_python_sdk.apis.tags.registration_api_raw import RegistrationApiRaw


class RegistrationApi(
    RequestCode,
    VerifyAccount,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: RegistrationApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = RegistrationApiRaw(api_client)
