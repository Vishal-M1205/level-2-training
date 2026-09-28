from abc import ABC, abstractmethod


class PaymentInterface(ABC):

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentInterface):
    def authenticate(self):
        print("Authenticating UPI...")

    def pay(self, amount):
        print(f"Paying ₹{amount} through UPI")


class Card(PaymentInterface):
    def authenticate(self):
        print("Validating card...")

    def pay(self, amount):
        print(f"Paying ₹{amount} through Card")


upi = UPI()
upi.authenticate()
upi.pay(500)

card = Card()
card.authenticate()
card.pay(1000)
