# Interface segregation

# Multiple interfaces it's better than
# one general purpose interface

# Analysis
# If we need 2-factor authentication we can 
# implemented in the PaymentProcessor class,
# but not every payment method allows this feature
# there is a problem with the implementation of this method
# because we have to implement in subclasses that doesn't need it

# Solution
# Create a subclass inherits from PaymentProcessor with the 
# required abstract method to implement the feature
# Now we have different interfaces for different features

# Solution 2
# Use composition: creating and authorizer class for sms
# Separating behavior 

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
    
    
 # Using Inheritance   
class PaymentProcessor_SMS(PaymentProcessor):    
    @abstractmethod
    def auth_sms(self, code): ...


class DebitPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, security_code):
        self.security_code = security_code
    
    def auth_sms(self, code):
        print(f"Verifying SMS code = {code}")
        self.verified = True
    
    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized!")
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


# Using Composition
class SMSAuth:
    authorized = False
    
    def verify_code(self, code):
        print(f"Verifying SMS code = {code}")
        self.authorized = True
    
    def is_authorized(self):
        return self.authorized
    
    
class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email, authorizer: SMSAuth):
        self.authorizer = authorizer
        self.email = email
        
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized!")
        print("Processing PayPal payment type")
        print(f"Verifying email: {self.email}")
        order.status = "paid"
    

order = Order()
processor_debit = DebitPaymentProcessor("65465466")

order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())

print("\n Debit with inheritance")
processor_debit.auth_sms("4565")
processor_debit.pay(order)

print("\n Paypal with composition")
authorizer = SMSAuth()
processor_paypal = PayPalPaymentProcessor("email@email.com", authorizer)
authorizer.verify_code("4564")
processor_paypal.pay(order)

