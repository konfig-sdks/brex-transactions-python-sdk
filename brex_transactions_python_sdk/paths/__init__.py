# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from brex_transactions_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V2_ACCOUNTS_CARD = "/v2/accounts/card"
    V2_ACCOUNTS_CARD_PRIMARY_STATEMENTS = "/v2/accounts/card/primary/statements"
    V2_ACCOUNTS_CASH = "/v2/accounts/cash"
    V2_ACCOUNTS_CASH_PRIMARY = "/v2/accounts/cash/primary"
    V2_ACCOUNTS_CASH_ID = "/v2/accounts/cash/{id}"
    V2_ACCOUNTS_CASH_ID_STATEMENTS = "/v2/accounts/cash/{id}/statements"
    V2_TRANSACTIONS_CARD_PRIMARY = "/v2/transactions/card/primary"
    V2_TRANSACTIONS_CASH_ID = "/v2/transactions/cash/{id}"
