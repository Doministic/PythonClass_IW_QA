# Owner: Dominic Lagle

# Encapsulation
class Bank:
    def __init__(self, account_owner, branch_location):
        self._account_owner = account_owner
        self.__branch_location = branch_location


class BankAccount(Bank):
    def __init__(self, checking_account, savings_account, balance):
        self._checking_account_number = checking_account 
        self._savings_account_number = savings_account
        self._balance = balance
        self._account_owner = "Me"
        self.__branch_location = "Woodland Hills"

    def _deposit(self, total_ammount):
        self._balance += total_ammount
        return self._balance
    
    def __operations_fee(self):
        fee = 15.00
        self._balance -= fee
        return self._balance
    
    def __check_balance_for_fee(self, minimumAmmount):
        if self._balance < minimumAmmount:
            self._balance -= self.__operations_fee()
        return self._balance

    def check_balance(self):
        print(f"your total balance in your account is: {self._balance}")



bankAccount = BankAccount(1, 1, 3200)
bankAccount.check_balance()
bankAccount._deposit(3000)
print(bankAccount._account_owner)
print(bankAccount.__branch_location)

