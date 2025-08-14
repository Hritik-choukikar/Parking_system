from abc import ABC,abstractmethod
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class Cash(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Amount ₹{amount} paid via Cash.")

class CreditCard(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Amount ₹{amount} paid via Credit Card.")
