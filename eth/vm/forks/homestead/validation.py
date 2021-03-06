from eth_utils import (
    ValidationError,
)

from eth.constants import (
    SECPK1_N,
)

from eth.db.account import BaseAccountDB

from eth.rlp.transactions import BaseTransaction

from eth.vm.forks.frontier.validation import (
    validate_frontier_transaction,
)


def validate_homestead_transaction(account_db: BaseAccountDB, transaction: BaseTransaction) -> None:
    if transaction.s > SECPK1_N // 2 or transaction.s == 0:
        raise ValidationError("Invalid signature S value")

    validate_frontier_transaction(account_db, transaction)
