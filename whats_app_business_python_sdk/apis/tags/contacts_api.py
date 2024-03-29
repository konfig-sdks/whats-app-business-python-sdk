# coding: utf-8

"""
    WhatsApp Business API

    See https://developers.facebook.com/docs/whatsapp

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from whats_app_business_python_sdk.paths.contacts.post import CreateContact
from whats_app_business_python_sdk.apis.tags.contacts_api_raw import ContactsApiRaw


class ContactsApi(
    CreateContact,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ContactsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ContactsApiRaw(api_client)
