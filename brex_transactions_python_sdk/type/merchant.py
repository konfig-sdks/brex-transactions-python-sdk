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


class RequiredMerchant(TypedDict):
    # Merchant descriptor
    raw_descriptor: str

    # https://en.wikipedia.org/wiki/Merchant_category_code
    mcc: str

class OptionalMerchant(TypedDict, total=False):
    pass

class Merchant(RequiredMerchant, OptionalMerchant):
    pass
