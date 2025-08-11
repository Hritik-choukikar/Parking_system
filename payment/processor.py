class PaymentProcessor:
    def process(self, amount):
        raise NotImplementedError

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        print(f" ₹{amount} paid via Credit Card")

class CashProcessor(PaymentProcessor):
    def process(self, amount):
        print(f" ₹{amount} collected in Cash")
