import json
import os

from src.models import Category, Product

BASE_DIR = str(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "products.json")


def load_categories_from_json(file_path: str = DATA_DIR) -> list:
    """Читает JSON-файл и создаёт объекты Category и Product."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []

    for category_data in data:
        products = []

        for product_data in category_data["products"]:
            product = Product(
                product_data["name"],
                product_data["description"],
                product_data["price"],
                product_data["quantity"],
            )
            products.append(product)

        category = Category(
            category_data["name"], category_data["description"], products
        )
        categories.append(category)

    return categories
