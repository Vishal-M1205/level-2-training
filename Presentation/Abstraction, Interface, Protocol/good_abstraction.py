class Payment:
    def __authenticate(self):
        print("Authenticating user...")

    def __validate_payment(self, amount):
        print(f"Validating ₹{amount}...")

    def __process_transaction(self, amount):
        print(f"Processing ₹{amount}...")

    def __generate_receipt(self):
        print("Generating receipt...")

    def pay(self, amount):
        self.__authenticate()
        self.__validate_payment(amount)
        self.__process_transaction(amount)
        self.__generate_receipt()


# Caller only needs to know pay()
payment = Payment()
payment.pay(500)
