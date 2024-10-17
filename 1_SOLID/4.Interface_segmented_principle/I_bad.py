'''
    Interface segregation principle (ISP) 
    clients should not be forced to depend on interfaces they do not use
    INTERFACES SHOULD BE SUCH THAT THE CLIENT SHOULD NOT IMPLEMENT UNNECESSARY FUNCTIONS THEY DO NOT NEED
'''

class Employee:
    def serve_customer(self):
        pass

    def clean_area(self):
        pass

    def cook_food(self):
        pass

'''
    Cook has methods it doesn't use (clean_area, serve_customer) and throws exceptions for them.
'''
class Cook(Employee):
    def cook_food(self):
        print("Cook: Cooking food")
    
    def clean_area(self):
        # Not the cook's job
        raise Exception("Cook: I don't clean work area")
    def serve_customer(self):
        # Not the cook's job
        raise Exception("Cook: I don't serve customers")
    