from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    '''An interface for each mode of payment'''

    @abstractmethod
    def pay(self, amount: int) -> None:
        '''Each class will provide it's own implementation of payment'''
        pass


class UPIPayment(PaymentStrategy):
    def __init__(self, number: str):
        self.receiving_upi_id = number
        
    convenience_charge_percentage = 0

    def pay(self, amount) -> None:
        total_amount = amount + (self.convenience_charge_percentage/100 * amount)
        print(f"Total amount {total_amount} sent to UPI id: {self.receiving_upi_id}")

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number
    
    convenience_charge_percentage = 20

    def pay(self, amount) -> None:
        total_amount = amount + (self.convenience_charge_percentage/100 * amount)
        print(f"Processing payment of {total_amount} using Credit Card: {self.card_number}")

class BankTransferPayment(PaymentStrategy):
    def __init__(self, account_number: str):
        self.account_number = account_number

    convenience_charge_percentage = 5

    def pay(self, amount) -> None:
        total_amount = amount + (self.convenience_charge_percentage/100 * amount)
        print(f"Processing payment of {total_amount} using Bank Transfer for account number: {self.account_number}")

