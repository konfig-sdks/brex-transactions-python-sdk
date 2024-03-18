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


class Merchant(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "raw_descriptor",
            "mcc",
        }
        
        class properties:
            raw_descriptor = schemas.StrSchema
            mcc = schemas.StrSchema
            __annotations__ = {
                "raw_descriptor": raw_descriptor,
                "mcc": mcc,
            }
    
    raw_descriptor: MetaOapg.properties.raw_descriptor
    mcc: MetaOapg.properties.mcc
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raw_descriptor"]) -> MetaOapg.properties.raw_descriptor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mcc"]) -> MetaOapg.properties.mcc: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["raw_descriptor", "mcc", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raw_descriptor"]) -> MetaOapg.properties.raw_descriptor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mcc"]) -> MetaOapg.properties.mcc: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["raw_descriptor", "mcc", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        raw_descriptor: typing.Union[MetaOapg.properties.raw_descriptor, str, ],
        mcc: typing.Union[MetaOapg.properties.mcc, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Merchant':
        return super().__new__(
            cls,
            *args,
            raw_descriptor=raw_descriptor,
            mcc=mcc,
            _configuration=_configuration,
            **kwargs,
        )
