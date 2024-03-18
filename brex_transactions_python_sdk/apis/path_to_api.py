import typing_extensions

from brex_transactions_python_sdk.paths import PathValues
from brex_transactions_python_sdk.apis.paths.v2_accounts_card import V2AccountsCard
from brex_transactions_python_sdk.apis.paths.v2_accounts_card_primary_statements import V2AccountsCardPrimaryStatements
from brex_transactions_python_sdk.apis.paths.v2_accounts_cash import V2AccountsCash
from brex_transactions_python_sdk.apis.paths.v2_accounts_cash_primary import V2AccountsCashPrimary
from brex_transactions_python_sdk.apis.paths.v2_accounts_cash_id import V2AccountsCashId
from brex_transactions_python_sdk.apis.paths.v2_accounts_cash_id_statements import V2AccountsCashIdStatements
from brex_transactions_python_sdk.apis.paths.v2_transactions_card_primary import V2TransactionsCardPrimary
from brex_transactions_python_sdk.apis.paths.v2_transactions_cash_id import V2TransactionsCashId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V2_ACCOUNTS_CARD: V2AccountsCard,
        PathValues.V2_ACCOUNTS_CARD_PRIMARY_STATEMENTS: V2AccountsCardPrimaryStatements,
        PathValues.V2_ACCOUNTS_CASH: V2AccountsCash,
        PathValues.V2_ACCOUNTS_CASH_PRIMARY: V2AccountsCashPrimary,
        PathValues.V2_ACCOUNTS_CASH_ID: V2AccountsCashId,
        PathValues.V2_ACCOUNTS_CASH_ID_STATEMENTS: V2AccountsCashIdStatements,
        PathValues.V2_TRANSACTIONS_CARD_PRIMARY: V2TransactionsCardPrimary,
        PathValues.V2_TRANSACTIONS_CASH_ID: V2TransactionsCashId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V2_ACCOUNTS_CARD: V2AccountsCard,
        PathValues.V2_ACCOUNTS_CARD_PRIMARY_STATEMENTS: V2AccountsCardPrimaryStatements,
        PathValues.V2_ACCOUNTS_CASH: V2AccountsCash,
        PathValues.V2_ACCOUNTS_CASH_PRIMARY: V2AccountsCashPrimary,
        PathValues.V2_ACCOUNTS_CASH_ID: V2AccountsCashId,
        PathValues.V2_ACCOUNTS_CASH_ID_STATEMENTS: V2AccountsCashIdStatements,
        PathValues.V2_TRANSACTIONS_CARD_PRIMARY: V2TransactionsCardPrimary,
        PathValues.V2_TRANSACTIONS_CASH_ID: V2TransactionsCashId,
    }
)
