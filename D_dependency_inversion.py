# Dependency Inversion

#  When a class depends on abstraction 
#  of other concrete subclasses

# Analysis
# Payments are depending of a specific authorizer

# Solution
# Create an abstract class for implements authorizers
# Now we can add easily a new authorization method



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


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool: ...
    
    
class SMSAuth(Authorizer):
    authorized = False
    
    def verify_code(self, code):
        print(f"Verifying SMS code = {code}")
        self.authorized = True
    
    def is_authorized(self):
        return self.authorized
    

class NotARobot(Authorizer):
    authorized = False
    
    def not_a_robot(self):
        print("Are you a robot? Naaa....")
        self.authorized = True
        
    def is_authorized(self):
        return self.authorized   


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order): ...
    
    

class DebitPaymentProcessor(PaymentProcessor):
    # passing a general authorizer
    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer
    
    
    def pay(self, order):
        if not self.authorizer.is_authorized():
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

    
    
class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email = email
        
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized!")
        print("Processing PayPal payment type")
        print(f"Verifying email: {self.email}")
        order.status = "paid"
    

order = Order()

order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())


print("\n Paypal with composition")
authorizer = NotARobot()
processor_paypal = PayPalPaymentProcessor("email@email.com", authorizer)
authorizer.not_a_robot()
processor_paypal.pay(order)

