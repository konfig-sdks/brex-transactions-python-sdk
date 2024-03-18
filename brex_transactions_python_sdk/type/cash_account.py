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

from brex_transactions_python_sdk.type.money import Money
from brex_transactions_python_sdk.type.status import Status

class RequiredCashAccount(TypedDict):
    # ID of the cash account
    id: str

    name: str

    current_balance: Money

    available_balance: Money

    account_number: str

    routing_number: str

    # Whether or not this account is the primary account. There will always be only one primary account.
    primary: bool

class OptionalCashAccount(TypedDict, total=False):
    status: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class CashAccount(RequiredCashAccount, OptionalCashAccount):
    pass
