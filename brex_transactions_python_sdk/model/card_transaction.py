# coding: utf-8

"""
    Transactions API

     The transactions API lets you view your transactions, accounts, and statements. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from brex_transactions_python_sdk import schemas  # noqa: F401


class CardTransaction(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "amount",
            "initiated_at_date",
            "description",
            "posted_at_date",
            "id",
        }
        
        class properties:
            description = schemas.StrSchema
            id = schemas.StrSchema
        
            @staticmethod
            def amount() -> typing.Type['Money']:
                return Money
            initiated_at_date = schemas.DateSchema
            posted_at_date = schemas.DateSchema
            
            
            class card_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'card_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class type(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_1 = schemas.AnyTypeSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            CardTransactionType,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'type':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class merchant(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_1 = schemas.AnyTypeSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            Merchant,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'merchant':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def card_metadata() -> typing.Type['CardTransactionCardMetadata']:
                return CardTransactionCardMetadata
            
            
            class expense_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expense_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "description": description,
                "id": id,
                "amount": amount,
                "initiated_at_date": initiated_at_date,
                "posted_at_date": posted_at_date,
                "card_id": card_id,
                "type": type,
                "merchant": merchant,
                "card_metadata": card_metadata,
                "expense_id": expense_id,
            }
    
    amount: 'Money'
    initiated_at_date: MetaOapg.properties.initiated_at_date
    description: MetaOapg.properties.description
    posted_at_date: MetaOapg.properties.posted_at_date
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initiated_at_date"]) -> MetaOapg.properties.initiated_at_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["posted_at_date"]) -> MetaOapg.properties.posted_at_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["card_id"]) -> MetaOapg.properties.card_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchant"]) -> MetaOapg.properties.merchant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["card_metadata"]) -> 'CardTransactionCardMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expense_id"]) -> MetaOapg.properties.expense_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "amount", "initiated_at_date", "posted_at_date", "card_id", "type", "merchant", "card_metadata", "expense_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> 'Money': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initiated_at_date"]) -> MetaOapg.properties.initiated_at_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["posted_at_date"]) -> MetaOapg.properties.posted_at_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["card_id"]) -> typing.Union[MetaOapg.properties.card_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchant"]) -> typing.Union[MetaOapg.properties.merchant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["card_metadata"]) -> typing.Union['CardTransactionCardMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expense_id"]) -> typing.Union[MetaOapg.properties.expense_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "amount", "initiated_at_date", "posted_at_date", "card_id", "type", "merchant", "card_metadata", "expense_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: 'Money',
        initiated_at_date: typing.Union[MetaOapg.properties.initiated_at_date, str, date, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        posted_at_date: typing.Union[MetaOapg.properties.posted_at_date, str, date, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        card_id: typing.Union[MetaOapg.properties.card_id, None, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        merchant: typing.Union[MetaOapg.properties.merchant, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        card_metadata: typing.Union['CardTransactionCardMetadata', schemas.Unset] = schemas.unset,
        expense_id: typing.Union[MetaOapg.properties.expense_id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CardTransaction':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            initiated_at_date=initiated_at_date,
            description=description,
            posted_at_date=posted_at_date,
            id=id,
            card_id=card_id,
            type=type,
            merchant=merchant,
            card_metadata=card_metadata,
            expense_id=expense_id,
            _configuration=_configuration,
            **kwargs,
        )

from brex_transactions_python_sdk.model.card_transaction_card_metadata import CardTransactionCardMetadata
from brex_transactions_python_sdk.model.card_transaction_type import CardTransactionType
from brex_transactions_python_sdk.model.merchant import Merchant
from brex_transactions_python_sdk.model.money import Money