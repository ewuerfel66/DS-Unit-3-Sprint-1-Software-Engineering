# Imports
import random as rand

# Instantiate class for products
class Product:
    # Init function
    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = rand.randint(1000000, 9999999)

    # Classifies products by theft risk
    def stealability(self):
        stealability = self.price / self.weight
        if stealability < 0.5:
            return "Not so stealable. . ."
        elif 0.5 <= stealability < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    # Classifies products by explosion risk        
    def explode(self):
        risk = self.flammability * self.weight
        if risk < 10:
            return ". . .fizzle"
        elif 10 <= risk < 50:
            return ". . .boom!"
        else:
            return "BABOOM!!"

class BoxingGlove(Product):
    # Init function
    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 10
        self.flammability = 0.5
        self.identifier = rand.randint(1000000, 9999999)

    # Override explode function
    def explode(self):
        return ". . .it's a glove."

    # Punch function
    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"