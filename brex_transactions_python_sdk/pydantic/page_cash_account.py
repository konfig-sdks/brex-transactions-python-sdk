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

from brex_transactions_python_sdk.pydantic.cash_account import CashAccount

class PageCashAccount(BaseModel):
    items: typing.List[CashAccount] = Field(alias='items')

    next_cursor: typing.Optional[typing.Optional[str]] = Field(None, alias='next_cursor')
    class Config:
        arbitrary_types_allowed = True
