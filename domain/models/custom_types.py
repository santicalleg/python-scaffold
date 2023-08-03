from enum import Enum


class AccountType(Enum):
    SAVING = "saving"
    CURRENT = "current"


class CurrentType(Enum):
    COP = "COP"
    USD = "USD"
