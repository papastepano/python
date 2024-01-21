# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to):
        return self.square_metres > compared_to.square_metres

    def price_difference(self, compared_to):
        total_price_self = self.square_metres * self.price_per_sqm
        total_price_compared_to = compared_to.square_metres * compared_to.price_per_sqm
        return abs(total_price_self - total_price_compared_to)

    def more_expensive(self, compared_to):
        total_price_self = self.price_per_sqm * self.square_metres
        total_price_compared_to = compared_to.price_per_sqm * compared_to.square_metres
        if total_price_self > total_price_compared_to:
            return True
        else:
            return False