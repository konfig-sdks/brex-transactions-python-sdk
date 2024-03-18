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

from brex_transactions_python_sdk.type.cash_transaction_type import CashTransactionType
from brex_transactions_python_sdk.type.money import Money

class RequiredCashTransaction(TypedDict):
    # Description of the transaction
    description: str

    id: str

    # ISO 8601 date of when the payment is initiated
    initiated_at_date: date

    # ISO 8601 date of when the payment is posted
    posted_at_date: date

class OptionalCashTransaction(TypedDict, total=False):
    amount: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    type: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Transfer ID to fetch additional metadata about the transaction using `https://developer.brex.com/openapi/payments_api/#operation/getTransfersById`
    transfer_id: typing.Optional[str]

class CashTransaction(RequiredCashTransaction, OptionalCashTransaction):
    pass
