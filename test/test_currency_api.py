# coding: utf-8

"""
    Billingo API v3

    This is a Billingo API v3 documentation. Our API based on REST software architectural style. API has resource-oriented URLs, accepts JSON-encoded request bodies and returns JSON-encoded responses. To use this API you have to generate a new API key on our [site](https://app.billingo.hu/api-key). After that, you can test your API key on this page.  # noqa: E501

    OpenAPI spec version: 3.0.14
    Contact: hello@billingo.hu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.currency_api import CurrencyApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCurrencyApi(unittest.TestCase):
    """CurrencyApi unit test stubs"""

    def setUp(self):
        self.api = CurrencyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_conversion_rate(self):
        """Test case for get_conversion_rate

        Get currencies exchange rate.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()