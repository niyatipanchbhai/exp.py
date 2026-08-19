from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UpiPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CashPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


print("Select Payment Method")
print("1. Credit Card")
print("2. UPI")
print("3. Cash")

choice = int(input("Enter your choice: "))
amount = float(input("Enter amount: ₹"))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = UpiPayment()
elif choice == 3:
    strategy = CashPayment()
else:
    print("Invalid choice")
    exit()

processor = PaymentProcessor(strategy)
processor.process_payment(amount)