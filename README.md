<div align="left">

[![Visit Brex](./header.png)](https://brex.com)

# Brex<a id="brex"></a>


The transactions API lets you view your transactions, accounts, and statements.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`brextransactions.accounts.get_cash_account`](#brextransactionsaccountsget_cash_account)
  * [`brextransactions.accounts.list_card_accounts`](#brextransactionsaccountslist_card_accounts)
  * [`brextransactions.accounts.list_cash_accounts`](#brextransactionsaccountslist_cash_accounts)
  * [`brextransactions.accounts.list_cash_statements`](#brextransactionsaccountslist_cash_statements)
  * [`brextransactions.accounts.list_primary_card_statements`](#brextransactionsaccountslist_primary_card_statements)
  * [`brextransactions.accounts.status`](#brextransactionsaccountsstatus)
  * [`brextransactions.transactions.list_all_card_transactions`](#brextransactionstransactionslist_all_card_transactions)
  * [`brextransactions.transactions.list_by_id`](#brextransactionstransactionslist_by_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Brex&serviceName=Transactions&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from brex_transactions_python_sdk import BrexTransactions, ApiException

brextransactions = BrexTransactions(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    #  Get cash account by ID
    get_cash_account_response = brextransactions.accounts.get_cash_account(
        id="id_example",
    )
    print(get_cash_account_response)
except ApiException as e:
    print("Exception when calling AccountsApi.get_cash_account: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from brex_transactions_python_sdk import BrexTransactions, ApiException

brextransactions = BrexTransactions(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        #  Get cash account by ID
        get_cash_account_response = await brextransactions.accounts.aget_cash_account(
            id="id_example",
        )
        print(get_cash_account_response)
    except ApiException as e:
        print("Exception when calling AccountsApi.get_cash_account: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from brex_transactions_python_sdk import BrexTransactions, ApiException

brextransactions = BrexTransactions(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    #  Get cash account by ID
    get_cash_account_response = brextransactions.accounts.raw.get_cash_account(
        id="id_example",
    )
    pprint(get_cash_account_response.body)
    pprint(get_cash_account_response.body["id"])
    pprint(get_cash_account_response.body["name"])
    pprint(get_cash_account_response.body["current_balance"])
    pprint(get_cash_account_response.body["available_balance"])
    pprint(get_cash_account_response.body["account_number"])
    pprint(get_cash_account_response.body["routing_number"])
    pprint(get_cash_account_response.body["primary"])
    pprint(get_cash_account_response.body["status"])
    pprint(get_cash_account_response.headers)
    pprint(get_cash_account_response.status)
    pprint(get_cash_account_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountsApi.get_cash_account: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `brextransactions.accounts.get_cash_account`<a id="brextransactionsaccountsget_cash_account"></a>


This endpoint returns the cash account associated with the provided ID with its status.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cash_account_response = brextransactions.accounts.get_cash_account(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CashAccount`](./brex_transactions_python_sdk/pydantic/cash_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/accounts/cash/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brextransactions.accounts.list_card_accounts`<a id="brextransactionsaccountslist_card_accounts"></a>


This endpoint lists all accounts of card type.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_card_accounts_response = brextransactions.accounts.list_card_accounts()
```

#### 🔄 Return<a id="🔄-return"></a>

[`AccountsListCardAccountsResponse`](./brex_transactions_python_sdk/pydantic/accounts_list_card_accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/accounts/card` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brextransactions.accounts.list_cash_accounts`<a id="brextransactionsaccountslist_cash_accounts"></a>


This endpoint lists all the existing cash accounts with their status.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_cash_accounts_response = brextransactions.accounts.list_cash_accounts()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PageCashAccount`](./brex_transactions_python_sdk/pydantic/page_cash_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/accounts/cash` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brextransactions.accounts.list_cash_statements`<a id="brextransactionsaccountslist_cash_statements"></a>


This endpoint lists all finalized statements for the cash account by ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_cash_statements_response = brextransactions.accounts.list_cash_statements(
    id="id_example",
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### cursor: `Optional[str]`<a id="cursor-optionalstr"></a>

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PageStatement`](./brex_transactions_python_sdk/pydantic/page_statement.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/accounts/cash/{id}/statements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brextransactions.accounts.list_primary_card_statements`<a id="brextransactionsaccountslist_primary_card_statements"></a>


This endpoint lists all finalized statements for the primary card account.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_primary_card_statements_response = (
    brextransactions.accounts.list_primary_card_statements(
        cursor="string_example",
        limit=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cursor: `Optional[str]`<a id="cursor-optionalstr"></a>

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PageStatement`](./brex_transactions_python_sdk/pydantic/page_statement.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/accounts/card/primary/statements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brextransactions.accounts.status`<a id="brextransactionsaccountsstatus"></a>


This endpoint returns the primary cash account with its status. There will always be only one primary account.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
status_response = brextransactions.accounts.status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CashAccount`](./brex_transactions_python_sdk/pydantic/cash_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/accounts/cash/primary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brextransactions.transactions.list_all_card_transactions`<a id="brextransactionstransactionslist_all_card_transactions"></a>


This endpoint lists all settled transactions for all card accounts.
Regular users may only fetch their own "PURCHASE","REFUND" and "CHARGEBACK" settled transactions.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_card_transactions_response = (
    brextransactions.transactions.list_all_card_transactions(
        cursor="string_example",
        limit=1,
        user_ids=["string_example"],
        posted_at_start="\n2022-12-12T23:59:59.999\n",
        expand_=["string_example"],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cursor: `Optional[str]`<a id="cursor-optionalstr"></a>

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

##### user_ids: List[`str`]<a id="user_ids-liststr"></a>

##### posted_at_start: `Optional[datetime]`<a id="posted_at_start-optionaldatetime"></a>

 Shows only transactions with a `posted_at_date` on or after this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6) 

##### expand_: List[`str`]<a id="expand_-liststr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PageCardTransaction`](./brex_transactions_python_sdk/pydantic/page_card_transaction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/transactions/card/primary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brextransactions.transactions.list_by_id`<a id="brextransactionstransactionslist_by_id"></a>


This endpoint lists all transactions for the cash account with the selected ID.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_id_response = brextransactions.transactions.list_by_id(
    id="id_example",
    cursor="string_example",
    limit=1,
    posted_at_start="\n2022-12-12T23:59:59.999\n",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### cursor: `Optional[str]`<a id="cursor-optionalstr"></a>

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

##### posted_at_start: `Optional[datetime]`<a id="posted_at_start-optionaldatetime"></a>

 Shows only transactions with a `posted_at_date` on or after this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6) 

#### 🔄 Return<a id="🔄-return"></a>

[`PageCashTransaction`](./brex_transactions_python_sdk/pydantic/page_cash_transaction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/transactions/cash/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
