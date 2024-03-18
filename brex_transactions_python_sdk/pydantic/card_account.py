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
from brex_transactions_python_sdk.pydantic.statement_period import StatementPeriod
from brex_transactions_python_sdk.pydantic.status import Status

class CardAccount(BaseModel):
    # ID of the card account
    id: str = Field(alias='id')

    current_statement_period: StatementPeriod = Field(alias='current_statement_period')

    status: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='status')

    current_balance: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='current_balance')

    available_balance: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='available_balance')

    account_limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='account_limit')
    class Config:
        arbitrary_types_allowed = True
