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

class Statement(BaseModel):
    id: str = Field(alias='id')

    period: StatementPeriod = Field(alias='period')

    start_balance: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='start_balance')

    end_balance: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='end_balance')
    class Config:
        arbitrary_types_allowed = True
