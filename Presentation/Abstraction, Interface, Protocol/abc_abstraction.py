from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount: int):
        pass

    # *  __isabstractmethod__ = True

    def generate_receipt(self):
        print("Generating payment receipt...")


class UPI(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")


class Card(Payment):
    def pay(self, amount):
        print(f"Processing card payment of ₹{amount}")


upi = UPI()
upi.pay(500)
upi.generate_receipt()

card = Card()
card.pay(1000)
card.generate_receipt()
