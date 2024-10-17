'''
    This is a good example of Liskov Substitution Principle
    The Liskov Substitution Principle states that objects of a superclass shall be 
        replaceable with objects of its subclasses without breaking the application.
    
    In this example, the FlyingBird class is a subclass of Bird class.
    The Crow class is a subclass of FlyingBird class.
    The Ostrich class is a subclass of Bird class.

    Only inititialize common attributes and methods in the parent class.
'''
class Bird:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def eat(self):
        print(f"Bird: {self.name} eats")

class FlyingBird(Bird):
    def fly(self):
        print(f"Bird:  {self.name} can fly")

class Crow(FlyingBird):
    
    def fly(self):
        print(f"Crow: {self.name} can fly")

class Ostrich(Bird):

    def run(self):
        print(f"Ostrich: {self.name} can run")

def make_bird_fly(bird: FlyingBird):
    bird.fly()

crow = Crow("Ramuttan")
ostrich = Ostrich("Jasuu")

make_bird_fly(crow)
ostrich.run()