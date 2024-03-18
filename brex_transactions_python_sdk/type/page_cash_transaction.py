# coding: utf-8

"""
    Transactions API

     The transactions API lets you view your transactions, accounts, and statements. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from brex_transactions_python_sdk.type.cash_transaction import CashTransaction

class RequiredPageCashTransaction(TypedDict):
    items: typing.List[CashTransaction]

class OptionalPageCashTransaction(TypedDict, total=False):
    next_cursor: typing.Optional[str]

class PageCashTransaction(RequiredPageCashTransaction, OptionalPageCashTransaction):
    pass
