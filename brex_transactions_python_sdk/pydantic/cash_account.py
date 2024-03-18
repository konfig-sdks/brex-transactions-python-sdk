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

from brex_transactions_python_sdk.pydantic.money import Money
from brex_transactions_python_sdk.pydantic.status import Status

class CashAccount(BaseModel):
    # ID of the cash account
    id: str = Field(alias='id')

    name: str = Field(alias='name')

    current_balance: Money = Field(alias='current_balance')

    available_balance: Money = Field(alias='available_balance')

    account_number: str = Field(alias='account_number')

    routing_number: str = Field(alias='routing_number')

    # Whether or not this account is the primary account. There will always be only one primary account.
    primary: bool = Field(alias='primary')

    status: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='status')
    class Config:
        arbitrary_types_allowed = True
