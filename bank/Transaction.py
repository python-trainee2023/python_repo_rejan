def deposit(account, balance):
    account.balance += balance


def withdrawal(account, balance):
    account.balance -= balance


def balanceEnquiry(account):
    return account.balance
