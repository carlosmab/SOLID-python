import sqlite3
import tkinter as tk
from dataclasses import dataclass
from tkinter import simpledialog


TITLE = "Products list"
DELETE_BTN_TEXT = "Delete product"
ADD_BTN_TEXT = "Add product"


@dataclass(kw_only=True)
class Product:
    """Product information."""
    
    name: str
    price: float
    
    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

    def __repr__(self):
        return f"{self.name} (${self.price:.2f})"


class Model:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("products.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "create table if not exists products (name text, price real)"
        )
        
    def add_product(self, product: Product):
        self.cursor.execute(
            "insert into products values (?, ?)",
            (product.name, product.price)    
        ) 
        self.connection.commit()
    
    def delete_product(self, product_name: str):
        self.cursor.execute("delete from products where name = ?", (product_name,) )
        self.connection.commit()
    
    def get_products(self) -> list[tuple[str, float]]:
        products: list[tuple[str, float]] = [
            (row[0], row[1])
            for row in self.cursor.execute("select name, price from products")
        ]
        return products
    

class App(tk.Tk):
    def __init__(self, model: Model) -> None:
        super().__init__()
        self.model = model
        self.title(TITLE)
        self.geometry("500x300")
        self.create_ui()
        self.update_products_list()
        
    def create_ui(self) -> None:
        self.frame = tk.Frame(self, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.product_list = tk.Listbox(
            self.frame,
            height=10,
            activestyle="none",
        )
        
        
           