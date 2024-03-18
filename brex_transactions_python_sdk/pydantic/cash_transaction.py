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
from pydantic import BaseModel, Field, RootModel

from brex_transactions_python_sdk.pydantic.cash_transaction_type import CashTransactionType
from brex_transactions_python_sdk.pydantic.money import Money

class CashTransaction(BaseModel):
    # Description of the transaction
    description: str = Field(alias='description')

    id: str = Field(alias='id')

    # ISO 8601 date of when the payment is initiated
    initiated_at_date: date = Field(alias='initiated_at_date')

    # ISO 8601 date of when the payment is posted
    posted_at_date: date = Field(alias='posted_at_date')

    amount: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='amount')

    type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='type')

    # Transfer ID to fetch additional metadata about the transaction using `https://developer.brex.com/openapi/payments_api/#operation/getTransfersById`
    transfer_id: typing.Optional[typing.Optional[str]] = Field(None, alias='transfer_id')
    class Config:
        arbitrary_types_allowed = True
