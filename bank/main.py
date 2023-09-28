from bank.account.Saving import Saving
from bank.account.Checking import Checking
from bank.Transaction import deposit, withdrawal, balanceEnquiry

# Create accounts
saving_account = Saving(32131231, "test", 1000, 0.8)
checking_account = Checking(3213213, "super test", 1000, 100)

# Transactions with accounts
deposit(saving_account, 1000)
deposit(checking_account, 2100)

rem_balance_saving = balanceEnquiry(saving_account)
print(f"Remaining balance: {rem_balance_saving}")

rem_balance_checking = balanceEnquiry(checking_account)
print(f"Remaining balance: {rem_balance_checking}")
