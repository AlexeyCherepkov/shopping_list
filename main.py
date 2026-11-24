import json
import os

BASE_DIR = str(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "products.json")

class Product:
    """Класс для представления продукта"""
    name: str
    description: str
    price: int | float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории"""
    name: str
    description: str
    products: list

    amount_of_categories = 0
    amount_of_products = 0


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.amount_of_categories += 1
        Category.amount_of_products += len(products)


def load_categories_from_json(file_path: str=DATA_DIR) -> list:
    """Читает JSON-файл и создаёт объекты Category и Product."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []

    for category_data in data:
        products = []

        for product_data in category_data['products']:
            product = Product(
                product_data['name'],
                product_data['description'],
                product_data['price'],
                product_data['quantity']
            )
            products.append(product)

        category = Category(
            category_data['name'],
            category_data['description'],
            products
        )
        categories.append(category)

    return categories