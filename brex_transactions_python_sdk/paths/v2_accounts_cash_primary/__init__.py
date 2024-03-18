# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from brex_transactions_python_sdk.paths.v2_accounts_cash_primary import Api

from brex_transactions_python_sdk.paths import PathValues

path = PathValues.V2_ACCOUNTS_CASH_PRIMARY