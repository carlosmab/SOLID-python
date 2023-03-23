## Applying creator principle
## Define when it's better to create an object
## taking into account the single responsibility principle


from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ProductDescription:
    price: int
    description: str


@dataclass
class SaleLineItem:
    product: ProductDescription
    quantity: int


@dataclass
class Sale:
    items : list[SaleLineItem] = field(default_factory=list)
    time: datetime = field(default=datetime.now())
    
    def add_line_item(self, product: ProductDescription, quantity: int):
        self.items.append(SaleLineItem(product=product, quantity=quantity))
        

def main() -> None: 
    headset = ProductDescription(price=5000, description="Gaming headset")
    keyboard = ProductDescription(price=7500, description="Mechanical gaming keyboard")
    
    # The add_line_item method in Sales prevents that main function creates objects
    # those are closely related to Sales
    sale = Sale()
    sale.add_line_item(product=headset, quantity=2)
    sale.add_line_item(product=keyboard, quantity=3)
    
    print(sale)
    

main()