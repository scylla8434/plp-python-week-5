# Define the Car class with a specific move behavior
class Car:
    def move(self):
        print("Driving 🚗")

# Define the Plane class with a different move behavior
class Plane:
    def move(self):
        print("Flying ✈️")

# Define the Boat class with its own move behavior
class Boat:
    def move(self):
        print("Sailing 🚤")

# List containing instances of different vehicle classes
vehicles = [Car(), Plane(), Boat()]

# Iterate through the list and call the move() method on each instance
for vehicle in vehicles:
    vehicle.move()
