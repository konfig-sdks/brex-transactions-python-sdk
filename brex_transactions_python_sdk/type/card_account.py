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
from brex_transactions_python_sdk.type.statement_period import StatementPeriod
from brex_transactions_python_sdk.type.status import Status

class RequiredCardAccount(TypedDict):
    # ID of the card account
    id: str

    current_statement_period: StatementPeriod

class OptionalCardAccount(TypedDict, total=False):
    status: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    current_balance: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    available_balance: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    account_limit: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class CardAccount(RequiredCardAccount, OptionalCardAccount):
    pass
