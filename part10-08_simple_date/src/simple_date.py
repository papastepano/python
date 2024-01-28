# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
        self.combined = int(f"{year}{month:02d}{day:02d}")


    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __gt__(self, other: "SimpleDate") -> bool:
        if self.combined > other.combined:
            return True
        else:
            return False

    def __le__(self, other: "SimpleDate") -> bool:
        if self.combined <= other.combined:
            return True
        else:
            return False

    def __lt__(self, other: "SimpleDate") -> bool:
        if self.combined < other.combined:
            return True
        else:
            return False
        

    def __ne__(self, other: "SimpleDate") -> bool:
        if self.combined != other.combined:
            return True
        else:
            return False

    def __eq__(self, other: "SimpleDate") -> bool:
        if self.combined == other.combined:
            return True
        else:
            return False
        
    def __add__(self, days: int) -> "SimpleDate":
        total_days = self.day + days

        new_day = total_days % 30
        new_month = self.month + (total_days // 30)

        if new_day == 0:
            new_day = 30
            new_month -= 1

        new_year = self.year + (new_month - 1) // 12
        new_month = new_month % 12 if new_month % 12 != 0 else 12

        return SimpleDate(new_day, new_month, new_year)

    def __sub__(self, other: "SimpleDate") -> int:
        total_days = self.year*360 + self.month*30 + self.day
        other_days = other.year*360 + other.month*30 + other.day

        return abs(total_days - other_days)


if __name__ == "__main__":
    
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)