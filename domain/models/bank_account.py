from domain.models.custom_types import AccountType, CurrentType


class BankAccount:
    def __init__(self, id, username, currency: CurrentType, balance, account_type: AccountType):
        self.id = id
        self.username = username
        self.currency = currency.value
        self.balance = balance
        self.account_type = account_type.value

    def __str__(self) -> str:
        return f"Account {self.username}, {self.balance}, {self.currency}, {self.account_type}"

    def __repr__(self) -> str:
        return f"<Account('{self.username}', {self.balance}, {self.currency}, {self.account_type})>"
