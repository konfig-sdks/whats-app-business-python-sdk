# coding: utf-8

"""
    WhatsApp Business API

    See https://developers.facebook.com/docs/whatsapp

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import whats_app_business_python_sdk
from whats_app_business_python_sdk.paths.certificates_webhooks_ca import delete
from whats_app_business_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCertificatesWebhooksCa(ApiTestMixin, unittest.TestCase):
    """
    CertificatesWebhooksCa unit test stubs
        Delete Webhook CA Certificate
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
