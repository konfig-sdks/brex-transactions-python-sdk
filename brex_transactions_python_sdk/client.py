# coding: utf-8
"""
    Transactions API

     The transactions API lets you view your transactions, accounts, and statements. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import typing
import inspect
from datetime import date, datetime
from brex_transactions_python_sdk.client_custom import ClientCustom
from brex_transactions_python_sdk.configuration import Configuration
from brex_transactions_python_sdk.api_client import ApiClient
from brex_transactions_python_sdk.type_util import copy_signature
from brex_transactions_python_sdk.apis.tags.accounts_api import AccountsApi
from brex_transactions_python_sdk.apis.tags.transactions_api import TransactionsApi



class BrexTransactions(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.accounts: AccountsApi = AccountsApi(api_client)
        self.transactions: TransactionsApi = TransactionsApi(api_client)
