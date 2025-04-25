class BankAccount:
    def __init__(self, accN, bsb, balance):
        self.__account_number = accN
        self.__bsb = bsb
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance must be positive.")

    balance = property(get_balance, set_balance)

    def __eq__(self, other):
        return isinstance(other, BankAccount) and self.__bsb == other.__bsb and self.__balance == other.__balance



class Person:
    def __init__(self, fname, lname):
        self.__first_name = fname
        self.__last_name = lname
        self.__account = None

    def open_account(self, accN, bsb, balance):
        self.__account = BankAccount(accN, bsb, balance)

    def deposit_money(self, amount):
        if amount > 0:
            self.__account.balance += amount
        else:
            print("Deposit amount must be positive")

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_account(self):
        return self.__account

    first_name = property(get_first_name)
    last_name = property(get_last_name)
    bank_account = property(get_account)

    def __eq__(self, other):
        return isinstance(other, Person) and self.__first_name[0] == other.__first_name[0] and self.__last_name == other.__last_name

    def __str__(self):
        if self.__account:
            return f"{self.__first_name} {self.__last_name} has a balance of {self.__account.balance}"
        else:
            return f"{self.__first_name} {self.__last_name} has no account"
