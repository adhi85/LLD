'''
    DIP - LOOSELY COUPLED
    1. In this example, Person depends on the abstraction MessageService not a specific EmailService.
    2. You can easily change the implementation of MessageService without changing the Person class.
    3. Which means easily switch between EmailService and SMSService without changing the Person class.

'''

class MessageService:
    def send(self, message):
        pass

class EmailService(MessageService):
    def send(self, message):
        print(f'Email sent: {message}')

class SMSService(MessageService):
    def send(self, message):
        print(f'SMS sent: {message}')

class Person:
    def __init__(self, message_service: MessageService):
        self.message_service = message_service
    
    def send_message(self, message):
        self.message_service.send(message)


''' Example Implementation '''
email_service = EmailService()
person1 = Person(email_service)
person1.send_message('Hello, via Email?')

sms_service = SMSService()
person2 = Person(sms_service)
person2.send_message('Hello, via SMS?')

