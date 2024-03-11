# coding: utf-8

"""
    WhatsApp Business API

    See https://developers.facebook.com/docs/whatsapp

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from whats_app_business_python_sdk.paths.certificates_webhooks_ca.delete import DeleteWebhookCa
from whats_app_business_python_sdk.paths.certificates_external_ca.get import DownloadCaCertificate
from whats_app_business_python_sdk.paths.certificates_webhooks_ca.get import DownloadWebhookCaCertificate
from whats_app_business_python_sdk.paths.certificates_external.post import UploadExternalCertificate
from whats_app_business_python_sdk.paths.certificates_webhooks_ca.post import UploadWebhookCaCertificate
from whats_app_business_python_sdk.apis.tags.certificates_api_raw import CertificatesApiRaw


class CertificatesApi(
    DeleteWebhookCa,
    DownloadCaCertificate,
    DownloadWebhookCaCertificate,
    UploadExternalCertificate,
    UploadWebhookCaCertificate,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CertificatesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CertificatesApiRaw(api_client)
