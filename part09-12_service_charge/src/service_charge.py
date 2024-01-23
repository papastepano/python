# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name: str, number: int, balance: float):
        self.__name = name
        self.__number = number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance -= self.__balance * 0.01

    def deposit(self, amount: float):
        if amount >= 0:
            self.__balance += amount
        self.__service_charge()
    
    def withdraw(self, amount: float):
        if self.__balance >= amount >= 0:
            self.__balance -= amount
        self.__service_charge()