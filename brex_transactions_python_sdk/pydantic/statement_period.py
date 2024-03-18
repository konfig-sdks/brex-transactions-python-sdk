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


class StatementPeriod(BaseModel):
    # Start date of the statement period
    start_date: date = Field(alias='start_date')

    # End date of the statement period
    end_date: date = Field(alias='end_date')
    class Config:
        arbitrary_types_allowed = True
