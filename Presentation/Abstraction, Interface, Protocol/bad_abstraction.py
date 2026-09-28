class Payment:
    def authenticate(self):
        print("Authenticating user...")

    def validate_payment(self, amount):
        print(f"Validating ₹{amount}...")

    def process_transaction(self, amount):
        print(f"Processing ₹{amount}...")

    def generate_receipt(self):
        print("Generating receipt...")


payment = Payment()
payment.authenticate()
payment.validate_payment(500)
payment.process_transaction(500)
payment.generate_receipt()
