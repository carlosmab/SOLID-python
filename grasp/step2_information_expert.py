## Information expert
## Where to insert new calculations, libs, modules for information?
## If we need calculate total 
## we add a property method in Sale class

# Where is simpler to compute?



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
    
    @property
    def total_price(self) -> int:
        return self.product.price * self.quantity


@dataclass
class Sale:
    items : list[SaleLineItem] = field(default_factory=list)
    time: datetime = field(default=datetime.now())
    
    @property
    def total_price(self) -> int:
        return sum((item.total_price for item in self.items))
        
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
    
    print(sale.total_price)
    
main()