class RealProperty:
    def __init__(
        self, rooms: int, square_meters: int, price_per_sqm: int, description: str
    ):
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm
        self.description = description

    def bigger(self, compared_to):
        return self.square_meters > compared_to.square_meters

    def price_difference(self, compared_to):
        # Function abs returns absolute value
        difference = abs(
            (self.price_per_sqm * self.square_meters)
            - (compared_to.price_per_sqm * compared_to.square_meters)
        )
        return difference

    def more_expensive(self, compared_to):
        difference = (self.price_per_sqm * self.square_meters) - (
            compared_to.price_per_sqm * compared_to.square_meters
        )
        return difference > 0

    def __repr__(self):
        return (
            f"RealProperty(rooms = {self.rooms}, square_meters = {self.square_meters}, "
            + f"price_per_sqm = {self.price_per_sqm}, description = {self.description})"
        )
    
def cheaper_properties(properties: list, reference: RealProperty) :
    return [(property.description, property.price_difference(reference)) for property in properties if reference.more_expensive(property)]


if __name__ == "__main__":
    a1 = RealProperty(1, 16, 5500, "Central studio")
    a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
    a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
    a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
    a5 = RealProperty(4, 105, 1700, "Loft in a small town")
    a6 = RealProperty(25, 1200, 2500, "Countryside mansion")

    properties = [a1, a2, a3, a4, a5, a6]

    print(cheaper_properties(properties, a3))