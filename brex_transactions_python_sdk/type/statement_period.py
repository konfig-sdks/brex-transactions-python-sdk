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


class RequiredStatementPeriod(TypedDict):
    # Start date of the statement period
    start_date: date

    # End date of the statement period
    end_date: date

class OptionalStatementPeriod(TypedDict, total=False):
    pass

class StatementPeriod(RequiredStatementPeriod, OptionalStatementPeriod):
    pass
