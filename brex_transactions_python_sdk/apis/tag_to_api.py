import typing_extensions

from brex_transactions_python_sdk.apis.tags import TagValues
from brex_transactions_python_sdk.apis.tags.accounts_api import AccountsApi
from brex_transactions_python_sdk.apis.tags.transactions_api import TransactionsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
    }
)
