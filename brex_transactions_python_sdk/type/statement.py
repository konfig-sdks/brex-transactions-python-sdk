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

class RequiredStatement(TypedDict):
    id: str

    period: StatementPeriod

class OptionalStatement(TypedDict, total=False):
    start_balance: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    end_balance: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class Statement(RequiredStatement, OptionalStatement):
    pass
