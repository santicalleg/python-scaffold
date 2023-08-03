from domain.models.bank_account import BankAccount
from domain.gateways.bank_account_gateway import BankAccountGateway
from domain.models.custom_types import AccountType, CurrentType


class LocalBankAccount(BankAccountGateway):

    async def get_bank_accounts(self):
        return [BankAccount(id, "John", CurrentType.COP, 1000, AccountType.CURRENT)]

    async def get_bank_account_by_id(self, id):
        return BankAccount(id, "John with Id", CurrentType.USD, 3000, AccountType.SAVING)
