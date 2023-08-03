from domain.gateways.bank_account_gateway import BankAccountGateway


class BankAccountUseCase:

    def __init__(self, bank_account_gateway: BankAccountGateway):
        self.bank_account_gateway = bank_account_gateway

    def get_bank_accounts(self):
        return self.bank_accounts_gateway.get_bank_accounts()

    def get_bank_account_by_id(self, id):
        return self.bank_accounts_gateway.get_by_id(id)
