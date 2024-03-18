# coding: utf-8

"""
    Transactions API

     The transactions API lets you view your transactions, accounts, and statements. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import unittest
from unittest.mock import patch

import urllib3

import brex_transactions_python_sdk
from brex_transactions_python_sdk.paths.v2_accounts_card_primary_statements import get
from brex_transactions_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2AccountsCardPrimaryStatements(ApiTestMixin, unittest.TestCase):
    """
    V2AccountsCardPrimaryStatements unit test stubs
         List primary card account statements.  
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
