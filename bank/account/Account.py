class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, balance):
        if balance < 1:
            raise ValueError(f'Deposit amount should be at least Rs 1 or more')
        self.balance += balance

    def withdraw(self, withdraw_amount):
        if self.balance < withdraw_amount:
            raise ValueError('Insufficient funds')

    def view_balance(self):
        if self.balance < 0:
            raise ValueError('Account freezed!')
        return self.balance

