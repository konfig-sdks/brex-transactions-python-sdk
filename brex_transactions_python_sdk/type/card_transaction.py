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

from brex_transactions_python_sdk.type.card_transaction_card_metadata import CardTransactionCardMetadata
from brex_transactions_python_sdk.type.card_transaction_type import CardTransactionType
from brex_transactions_python_sdk.type.merchant import Merchant
from brex_transactions_python_sdk.type.money import Money

class RequiredCardTransaction(TypedDict):
    # Description of the transaction
    description: str

    id: str

    amount: Money

    # ISO 8601 date string
    initiated_at_date: date

    # ISO 8601 date string
    posted_at_date: date

class OptionalCardTransaction(TypedDict, total=False):
    # ID of the card used for the transaction. Null when type is REWARDS_CREDIT or COLLECTION.
    card_id: typing.Optional[str]

    type: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    merchant: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    card_metadata: CardTransactionCardMetadata

    # The expense ID related to the card transaction.
    expense_id: typing.Optional[str]

class CardTransaction(RequiredCardTransaction, OptionalCardTransaction):
    pass
