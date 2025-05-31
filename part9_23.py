class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"
    
class Room :
    def __init__ (self) :
        self.person_count = 0
        self.person_list = []
        self.total_height = 0

    def is_empty(self) :
        if self.person_count == 0 :     return "True"

        return self.print_contents()
        
    
    def add (self, person: "Person") :
        self.person_count += 1
        self.person_list.append(person)
        self.total_height += person.height

    def print_contents (self) :
        for person in self.person_list :
            print (person)    
        
        print (f"False\nThere are {self.person_count} persons in the room, and their combined height is {self.total_height} cm")

    def shortest (self) :
        if self.is_empty() == "True" :
            return None
        
        short = self.person_list[0]

        for person in self.person_list :
            if person.height < short.height :
                short = person

        return short
    
    def remove_shortest (self) :
        if self.shortest() == None :    return None

        short = self.shortest()

        self.person_count -= 1
        self.total_height -= short.height

        self.person_list.remove (short)

        return short
    
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