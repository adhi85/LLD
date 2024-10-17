'''
    Dependency Inversion Principle (DIP) statest that high-level modules should not depend on low-level modules. Both should depend on abstractions. 
    Class should depend on interfaces, not on concrete classes


    WITHOUT DIP - TIGHTLY COUPLED
    1. In this example, Person class is dependent on EmailService class.
    2. Person class should depend on an interface, not on a concrete class.
    3. Otherwise, if EmailService class changes, Person class will also have to change.
    4. If person want to send message using SMS Instead of Email, then Person class will have to change whiich violates DIP.
'''

class EmailService:
    def send(self, message: str):
        print(f'Email sent: {message}')

class Person:
    def __init__(self):
        self.email_service = EmailService()
    
    def send_message(self, message: str):
        self.email_service.send(message)
