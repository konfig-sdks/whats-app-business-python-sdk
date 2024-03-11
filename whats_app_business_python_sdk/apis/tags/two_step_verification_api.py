# coding: utf-8

"""
    WhatsApp Business API

    See https://developers.facebook.com/docs/whatsapp

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from whats_app_business_python_sdk.paths.settings_account_two_step.delete import Disable
from whats_app_business_python_sdk.paths.settings_account_two_step.post import EnableAccount
from whats_app_business_python_sdk.apis.tags.two_step_verification_api_raw import TwoStepVerificationApiRaw


class TwoStepVerificationApi(
    Disable,
    EnableAccount,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TwoStepVerificationApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TwoStepVerificationApiRaw(api_client)
