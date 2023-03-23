## Information expert
## Where to insert new functionality?
## If we need to compute the total price 
## we have to add a method in Sale class

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
        return self.quantity * self.product.price

@dataclass
class Sale:
    items : list[SaleLineItem] = field(default_factory=list)
    time: datetime = field(default=datetime.now())
    

def main() -> None: 
    headset = ProductDescription(price=5000, description="Gaming headset")
    keyboard = ProductDescription(price=7500, description="Mechanical gaming keyboard")
    
    # SalesLineItem class have a close responsibility with Sale,
    # so this objects should be created in Sale
    row1 = SaleLineItem(product=headset, quantity=2)
    row2 = SaleLineItem(product=keyboard, quantity=3)
    
    sale = Sale([row1, row2])
    
    print(sale)

main()