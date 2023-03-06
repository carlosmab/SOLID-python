# code is OPEN for extensions
# code is CLOSED for modifications

# Allows polymorphism

# Analysis
# If we need to add a new payment method (Bitcoin, paypal...)
# it's necessary to modify the PaymentProcessor class, that is bad 
# according this principle

# Solution
# Define a subclass for each payment type
# creating and abstract payment processor class 
# So if we need a new payment method we don't have to change Order, or PaymentProcessor classes

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
    def pay(self, order, security_code): ...

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

# So if we need a new payment method we
# don't have to change Order, or PaymentProcessor classes i.e:
class PayPalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing PayPal payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
    

order = Order()
processor = DebitPaymentProcessor()

order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())

processor.pay(order, "0372846")