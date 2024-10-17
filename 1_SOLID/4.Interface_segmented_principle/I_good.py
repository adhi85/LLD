'''
    None of the classes are forced to implement the methods that they don't need.
'''

class Cooking:
    def cook_food(self):
        pass

class Decorating:
    def decorate_food(self):
        pass

class Serving:
    def serve_customer(self):
        pass

class Cleaning:
    def clean_area(self):
        pass

''' HeadChef does both cooking and decorating '''
class HeadChef(Cooking, Decorating):
    def cook_food(self):
        print("HeadChef: Cooking food")

    def decorate_food(self):
        print("HeadChef: Decorating food")

''' Server only serves customers, so it implements only Serving '''
class Server(Serving):
    def serve_customer(self):
        print("Server: Serving customer")

''' RoomCleaner only cleans, so it implements only Cleaning '''
class RoomCleaner(Cleaning):
    def clean_area(self):
        print("RoomCleaner: Cleaning area")
