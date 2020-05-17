# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# this is the base class
# ======================
class Vehicle:
    def __init__(self, make, **kwargs):
        self.make = make
# ======================
# this is the base class


class FlightVehicle(Vehicle):
    def __init__(self, wing_type, **kwargs):
        super().__init__(kwargs)
        self.wing_type = wing_type


class GroundVehicle(Vehicle):
    def __init__(self, tire_type, **kwargs):
        super().__init__(kwargs)
        self.tire_type = tire_type


class Car(GroundVehicle):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.type = "car"

    def __str__(self):
        return f"The {self.make} {self.type} has {self.tire_type} wheels and can be seen stuck in traffic"


class Motorcycle(GroundVehicle):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.type = "motorcycle"

    def __str__(self):
        return f"The {self.make} {self.type} has {self.tire_type} wheels and can be seen splitting lanes"


class Airplane(FlightVehicle):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.type = "airplane"

    def __str__(self):
        return f"The {self.make} {self.type} has {self.wing_type} wings and can be seen soaring through the skies"


class Starship(FlightVehicle):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.type = "starship"

    def __str__(self):
        return f"The {self.make} {self.type} has {self.wing_type} wings and can be seen bending space and time"
