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


CashTransactionType = Literal["PAYMENT", "DIVIDEND", "FEE", "ADJUSTMENT", "INTEREST", "CARD_COLLECTION", "REWARDS_REDEMPTION", "RECEIVABLES_OFFERS_ADVANCE", "FBO_TRANSFER", "RECEIVABLES_OFFERS_REPAYMENT", "RECEIVABLES_OFFERS_COLLECTION", "BREX_OPERATIONAL_TRANSFER", "INTRA_CUSTOMER_ACCOUNT_BOOK_TRANSFER", "BOOK_TRANSFER", "CRYPTO_BRIDGE"]
