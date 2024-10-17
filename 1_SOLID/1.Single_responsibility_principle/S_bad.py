#  Single Responsibility Principle (SRP) 

'''
    Bad Example Which doesnot follow SRP
    It has two responsibilities
    1. Save user to database
    2. Send email to user
    It has two different reasons to change: User data and email logic.
'''
class User:
    def __init_(self,name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email
    
    def save(self):
        print('User saved')
    
    def send_email(self, to_email: str):
        print(f'Email sent: {to_email}')
    


