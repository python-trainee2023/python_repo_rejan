from bank.account.Account import  Account


class Saving(Account):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def deposit_interest(self):
        self.balance += self.balance * self.interest_rate


