# coding: utf-8

"""
    Transactions API

     The transactions API lets you view your transactions, accounts, and statements. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import unittest

import os
from pprint import pprint
from brex_transactions_python_sdk import BrexTransactions

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        brextransactions = BrexTransactions(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(brextransactions)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
