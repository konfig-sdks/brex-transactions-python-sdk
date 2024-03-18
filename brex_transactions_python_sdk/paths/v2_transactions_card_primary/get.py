# coding: utf-8

"""
    Transactions API

     The transactions API lets you view your transactions, accounts, and statements. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from brex_transactions_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from brex_transactions_python_sdk.api_response import AsyncGeneratorResponse
from brex_transactions_python_sdk import api_client, exceptions
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

from brex_transactions_python_sdk.model.page_card_transaction import PageCardTransaction as PageCardTransactionSchema

from brex_transactions_python_sdk.type.page_card_transaction import PageCardTransaction

from ...api_client import Dictionary
from brex_transactions_python_sdk.pydantic.page_card_transaction import PageCardTransaction as PageCardTransactionPydantic

from . import path

# Query params


class CursorSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CursorSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class LimitSchema(
    schemas.Int32Base,
    schemas.IntBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneDecimalMixin
):


    class MetaOapg:
        format = 'int32'


    def __new__(
        cls,
        *args: typing.Union[None, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LimitSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class UserIdsSchema(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):


    class MetaOapg:
        items = schemas.StrSchema


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UserIdsSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class PostedAtStartSchema(
    schemas.DateTimeBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date-time'


    def __new__(
        cls,
        *args: typing.Union[None, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PostedAtStartSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class ExpandSchema(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):


    class MetaOapg:
        items = schemas.StrSchema


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ExpandSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'cursor': typing.Union[CursorSchema, None, str, ],
        'limit': typing.Union[LimitSchema, None, decimal.Decimal, int, ],
        'user_ids': typing.Union[UserIdsSchema, list, tuple, None, ],
        'posted_at_start': typing.Union[PostedAtStartSchema, None, str, datetime, ],
        'expand[]': typing.Union[ExpandSchema, list, tuple, None, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_cursor = api_client.QueryParameter(
    name="cursor",
    style=api_client.ParameterStyle.FORM,
    schema=CursorSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_user_ids = api_client.QueryParameter(
    name="user_ids",
    style=api_client.ParameterStyle.FORM,
    schema=UserIdsSchema,
    explode=True,
)
request_query_posted_at_start = api_client.QueryParameter(
    name="posted_at_start",
    style=api_client.ParameterStyle.FORM,
    schema=PostedAtStartSchema,
    explode=True,
)
request_query_expand_ = api_client.QueryParameter(
    name="expand[]",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandSchema,
    explode=True,
)
_auth = [
    'OAuth2',
]
SchemaFor200ResponseBodyApplicationJson = PageCardTransactionSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PageCardTransaction


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PageCardTransaction


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_all_card_transactions_mapped_args(
        self,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
        user_ids: typing.Optional[typing.Optional[typing.List[str]]] = None,
        posted_at_start: typing.Optional[typing.Optional[datetime]] = None,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if cursor is not None:
            _query_params["cursor"] = cursor
        if limit is not None:
            _query_params["limit"] = limit
        if user_ids is not None:
            _query_params["user_ids"] = user_ids
        if posted_at_start is not None:
            _query_params["posted_at_start"] = posted_at_start
        if expand_ is not None:
            _query_params["expand[]"] = expand_
        args.query = _query_params
        return args

    async def _alist_all_card_transactions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
         List transactions for all card accounts. 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_cursor,
            request_query_limit,
            request_query_user_ids,
            request_query_posted_at_start,
            request_query_expand_,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/transactions/card/primary',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_all_card_transactions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
         List transactions for all card accounts. 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_cursor,
            request_query_limit,
            request_query_user_ids,
            request_query_posted_at_start,
            request_query_expand_,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/transactions/card/primary',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListAllCardTransactionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_all_card_transactions(
        self,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
        user_ids: typing.Optional[typing.Optional[typing.List[str]]] = None,
        posted_at_start: typing.Optional[typing.Optional[datetime]] = None,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_card_transactions_mapped_args(
            cursor=cursor,
            limit=limit,
            user_ids=user_ids,
            posted_at_start=posted_at_start,
            expand_=expand_,
        )
        return await self._alist_all_card_transactions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_all_card_transactions(
        self,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
        user_ids: typing.Optional[typing.Optional[typing.List[str]]] = None,
        posted_at_start: typing.Optional[typing.Optional[datetime]] = None,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_card_transactions_mapped_args(
            cursor=cursor,
            limit=limit,
            user_ids=user_ids,
            posted_at_start=posted_at_start,
            expand_=expand_,
        )
        return self._list_all_card_transactions_oapg(
            query_params=args.query,
        )

class ListAllCardTransactions(BaseApi):

    async def alist_all_card_transactions(
        self,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
        user_ids: typing.Optional[typing.Optional[typing.List[str]]] = None,
        posted_at_start: typing.Optional[typing.Optional[datetime]] = None,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> PageCardTransactionPydantic:
        raw_response = await self.raw.alist_all_card_transactions(
            cursor=cursor,
            limit=limit,
            user_ids=user_ids,
            posted_at_start=posted_at_start,
            expand_=expand_,
            **kwargs,
        )
        if validate:
            return PageCardTransactionPydantic(**raw_response.body)
        return api_client.construct_model_instance(PageCardTransactionPydantic, raw_response.body)
    
    
    def list_all_card_transactions(
        self,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
        user_ids: typing.Optional[typing.Optional[typing.List[str]]] = None,
        posted_at_start: typing.Optional[typing.Optional[datetime]] = None,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        validate: bool = False,
    ) -> PageCardTransactionPydantic:
        raw_response = self.raw.list_all_card_transactions(
            cursor=cursor,
            limit=limit,
            user_ids=user_ids,
            posted_at_start=posted_at_start,
            expand_=expand_,
        )
        if validate:
            return PageCardTransactionPydantic(**raw_response.body)
        return api_client.construct_model_instance(PageCardTransactionPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
        user_ids: typing.Optional[typing.Optional[typing.List[str]]] = None,
        posted_at_start: typing.Optional[typing.Optional[datetime]] = None,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_card_transactions_mapped_args(
            cursor=cursor,
            limit=limit,
            user_ids=user_ids,
            posted_at_start=posted_at_start,
            expand_=expand_,
        )
        return await self._alist_all_card_transactions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
        user_ids: typing.Optional[typing.Optional[typing.List[str]]] = None,
        posted_at_start: typing.Optional[typing.Optional[datetime]] = None,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_card_transactions_mapped_args(
            cursor=cursor,
            limit=limit,
            user_ids=user_ids,
            posted_at_start=posted_at_start,
            expand_=expand_,
        )
        return self._list_all_card_transactions_oapg(
            query_params=args.query,
        )

