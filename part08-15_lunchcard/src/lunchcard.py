# Write your solution here:
class LunchCard:
    def __init__(self, balance: int):
        self.balance = balance

    def __str__(self) -> str:
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60
            return True
        else:
            return False

    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60
            return True
        else:
            return False

    def deposit_money(self, amount: int):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def main():
        peters_card = LunchCard(20)
        graces_card = LunchCard(30)
        peters_card.eat_special()
        graces_card .eat_lunch()
        print(f"Peter: The balance is {peters_card.balance:.1f} euros")
        print(f"Grace: The balance is {graces_card.balance:.1f} euros")
        peters_card.deposit_money(20)
        graces_card .eat_special()
        print(f"Peter: The balance is {peters_card.balance:.1f} euros")
        print(f"Grace: The balance is {graces_card.balance:.1f} euros")
        peters_card.eat_lunch()
        peters_card.eat_lunch()
        graces_card .deposit_money(50)
        print(f"Peter: The balance is {peters_card.balance:.1f} euros")
        print(f"Grace: The balance is {graces_card.balance:.1f} euros")

LunchCard.main()