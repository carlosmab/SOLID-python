# Liskov substitution

# Whe having objects 
# We should be able to substitute these 
# with subtypes or subclasses
# without altering the correctness of the program,
# then you need to define the constructor arguments
# to keep inheritance flexible

# Analysis
# If any payment method doesn't need a security 
# code, but something else,
# the code breaks, we have to change the implementation
# of the payment processor

# Solution
# Remove the security code param of the pay method
# Add an initializer in each subclass with the specific security requirement 

from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"
    
    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
        
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order): ...


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
    
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email
        
    def pay(self, order):
        print("Processing PayPal payment type")
        print(f"Verifying email: {self.email}")
        order.status = "paid"
    

order = Order()
processor = PayPalPaymentProcessor( "ca@email.com")


order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())

processor.pay(order)
