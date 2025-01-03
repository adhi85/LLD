'''
    # It follows the Single Responsibility Principle: PaymentProcessor is responsible only for coordinating the payment process, 
    while the PaymentStrategy implementations handle the specific payment logic.
    
    # It also adheres to the Open/Closed Principle: New payment methods can be added without modifying the PaymentProcessor class.
'''

import payment_strategies

class PaymentProcessor:
    def __init__(self, payment_strategy: payment_strategies.PaymentStrategy):
        """ self._payment_strategy references the objects of other PaymentStrategy classes. Its called composition.
            Composition is a design principle where an object is composed of other objects to achieve functionality.
            PaymentProcessor is composed of a PaymentStrategy object, allowing it to delegate payment-specific functionality to that object.
        """
        self._payment_strategy = payment_strategy
    
    def process_payment(self, amount: int) -> None:
        """Delegates the payment process to the respective strategy."""
        self._payment_strategy.pay(amount)

    def set_payment_strategy(self, payment_strategy: payment_strategies.PaymentStrategy) -> None:
        """Allows changing the payment strategy at runtime."""
        self._payment_strategy = payment_strategy

if __name__ == "__main__":

    # Pay using UPI
    upi_payment = payment_strategies.UPIPayment(number="9876543210")
    processor = PaymentProcessor(upi_payment)
    processor.process_payment(100)

    # Pay using Credit Card
    credit_card = payment_strategies.CreditCardPayment(card_number="1234 5678 9012 3456")
    processor.set_payment_strategy(credit_card)
    processor.process_payment(1000)

    # Pay using Bank Transfer
    bank_transfer = payment_strategies.BankTransferPayment(account_number="1234567890")
    processor.set_payment_strategy(bank_transfer)
    processor.process_payment(5000)


