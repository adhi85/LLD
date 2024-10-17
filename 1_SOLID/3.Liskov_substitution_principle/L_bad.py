'''
    If class B is a subclass of class A, you should be able to substitute A with B without breaking the 
    behavior of your code. The subclass must adhere to the contract defined by the parent class and not override methods 
    in a way that changes their expected behavior.
'''

class Bird:
    def fly(self):
        print("I can fly")

class Crow(Bird):
    def fly(self):
        print("Crow can fly")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostrich can't fly")
    
def make_bird_fly(bird: Bird):
    bird.fly()

crow = Crow()
ostrich = Ostrich()

make_bird_fly(crow)
make_bird_fly(ostrich) # This will raise an exception