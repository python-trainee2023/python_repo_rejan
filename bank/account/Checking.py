from bank.account.Account import Account


class Checking(Account):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, withdraw_amount):
        if self.balance + self.overdraft_limit < withdraw_amount:
            raise ValueError('Insufficient funds')

        self.balance -= withdraw_amount
