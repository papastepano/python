# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)
    
    def is_empty(self):
        return len(self.people) == 0


    def print_contents(self):
        print("There are", len(self.people), "persons in the room, and their combined height is", sum([person.height for person in self.people]), "cm.")

        for person in self.people:
            print(f"{person}" + " (height: " + str(person.height) + "cm)")

    def shortest(self):
        if self.is_empty():
            return None
        shortest = self.people[0]
        for person in self.people:
            if person.height < shortest.height:
                shortest = person
        return shortest

    def remove_shortest(self):
        if self.is_empty():
            return None
        shortest = self.shortest()
        self.people.remove(shortest)
        return shortest



if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()