# Base class representing a general Superhero
class Superhero:
    def __init__(self, name, alias, power):
        # Encapsulated attributes (using a single underscore to indicate protected nature)
        self._name = name
        self._alias = alias
        self._power = power

    def display_info(self):
        # Display common information about the superhero
        print(f"Superhero Name: {self._name}")
        print(f"Alias: {self._alias}")
        print(f"Primary Power: {self._power}")

    def use_power(self):
        # A method meant to be overridden by subclasses for a custom power action.
        print(f"{self._alias} uses their power: {self._power}!")

# Subclass representing a superhero with advanced technology
class TechSuperhero(Superhero):
    def __init__(self, name, alias, power, gadget):
        # Call the constructor of the Superhero class to initialize base attributes
        super().__init__(name, alias, power)
        self._gadget = gadget  # Specific attribute for TechSuperhero

    # Overriding the display_info method to include gadget information
    def display_info(self):
        super().display_info()  # Call the base class method to display common info
        print(f"Gadget: {self._gadget}")

    # Overriding the use_power method to incorporate the gadget in the action
    def use_power(self):
        print(f"{self._alias} activates their {self._gadget} to unleash {self._power}!")

# Create instances of the Superhero and TechSuperhero classes
if __name__ == "__main__":
    # Instance of Superhero
    hero1 = Superhero("Clark Kent", "Superman", "Super strength and flight")
    print("---- Superhero ----")
    hero1.display_info()
    hero1.use_power()

    print("\n---- TechSuperhero ----")
    # Instance of TechSuperhero with an extra attribute for gadget
    hero2 = TechSuperhero("Tony Stark", "Iron Man", "Advanced combat and engineering", "Arc Reactor Suit")
    hero2.display_info()
    hero2.use_power()
