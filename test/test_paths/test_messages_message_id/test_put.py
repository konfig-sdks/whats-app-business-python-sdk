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
from whats_app_business_python_sdk.paths.messages_message_id import put
from whats_app_business_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestMessagesMessageID(ApiTestMixin, unittest.TestCase):
    """
    MessagesMessageID unit test stubs
        Mark-Message-As-Read
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''




if __name__ == '__main__':
    unittest.main()
