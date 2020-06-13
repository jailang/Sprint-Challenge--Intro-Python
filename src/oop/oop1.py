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
class Vehicle:
    """
        Base class for all vehicles
    """
    pass


class GroundVehicle(Vehicle):
    """
        Extends Vehicle and becomes the base for all ground vehicles
    """
    pass


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass


class FlightVehicle(Vehicle):
    """
        Extends Vehicle and becomes the base for all flying vehicles
    """
    pass


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass
