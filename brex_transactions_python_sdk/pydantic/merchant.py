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


class Merchant(BaseModel):
    # Merchant descriptor
    raw_descriptor: str = Field(alias='raw_descriptor')

    # https://en.wikipedia.org/wiki/Merchant_category_code
    mcc: str = Field(alias='mcc')
    class Config:
        arbitrary_types_allowed = True
