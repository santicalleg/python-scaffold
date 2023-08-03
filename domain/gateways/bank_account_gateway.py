from abc import ABC, abstractmethod


class BankAccountGateway:

    @abstractmethod
    async def get_bank_accounts(self):
        pass

    @abstractmethod
    async def get_bank_account_by_id(self, id):
        pass
