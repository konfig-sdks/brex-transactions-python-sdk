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

from brex_transactions_python_sdk.pydantic.card_transaction_card_metadata import CardTransactionCardMetadata
from brex_transactions_python_sdk.pydantic.card_transaction_type import CardTransactionType
from brex_transactions_python_sdk.pydantic.merchant import Merchant
from brex_transactions_python_sdk.pydantic.money import Money

class CardTransaction(BaseModel):
    # Description of the transaction
    description: str = Field(alias='description')

    id: str = Field(alias='id')

    amount: Money = Field(alias='amount')

    # ISO 8601 date string
    initiated_at_date: date = Field(alias='initiated_at_date')

    # ISO 8601 date string
    posted_at_date: date = Field(alias='posted_at_date')

    # ID of the card used for the transaction. Null when type is REWARDS_CREDIT or COLLECTION.
    card_id: typing.Optional[typing.Optional[str]] = Field(None, alias='card_id')

    type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='type')

    merchant: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='merchant')

    card_metadata: typing.Optional[CardTransactionCardMetadata] = Field(None, alias='card_metadata')

    # The expense ID related to the card transaction.
    expense_id: typing.Optional[typing.Optional[str]] = Field(None, alias='expense_id')
    class Config:
        arbitrary_types_allowed = True
