# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
    
    def __str__(self):
        if self.__cents < 10:
            return f"{self.__euros}.0{self.__cents} eur"
        else:
            return f"{self.__euros}.{self.__cents} eur"

    def __repr__(self) -> str:
        pass

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents
    
    def __gt__(self, another):
        return self.__euros > another.__euros or (self.__euros == another.__euros and self.__cents > another.__cents)
    
    def __lt__(self, another):
        return self.__euros < another.__euros or (self.__euros == another.__euros and self.__cents < another.__cents)
    
    def __ne__(self, another):
        return not self.__eq__(another)
    
    def __add__(self, another):
        euros = self.__euros + another.__euros
        cents = self.__cents + another.__cents
        if cents >= 100:
            euros += 1
            cents -= 100
        return Money(euros, cents)


    def __sub__(self, another):
        if self.__euros < another.__euros or (self.__euros == another.__euros and self.__cents < another.__cents):
            raise ValueError("a negative result is not allowed")
        euros = self.__euros - another.__euros
        cents = self.__cents - another.__cents
        if cents < 0:
            euros -= 1
            cents += 100
        return Money(euros, cents)

if __name__ == "__main__":
    e1 = Money(4, 5)
    print(e1)
    e1.euros = 1000
    print(e1)