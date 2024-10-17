'''
    Good Example Which follows SRP

    User class: Deals only with user-related data and operations.
    EmailService class: Deals exclusively with email operations.

    keeping these two responsibilities separate, the code is more modular, maintainable, and easier to extend.
    Example: to add SMS notifications in the future, create a separate SMSService class without modifying the User or EmailService classes.
'''
class User:
    def __init__(self, name: str, age: int, email: str) -> None:
        self.name = name
        self.age = age
        self.email = email

    def save(self):
        print(f"Saving User")

class EmailService:
    def send_email(self,from_email: str, to_email: str, message: str):
        print(f"sending email from {from_email} to {to_email}, Message: {message}")

user = User('ram', 25, 'ram@email.com')
user.save()

email_service = EmailService()
email_service.send_email(user.email, 'sample@email.com', 'Welcome to our platform')


        