import json

from src.models import Category, Product
from src.loader import load_categories_from_json


def make_json_file(tmp_path, data):
    file = tmp_path / "products.json"
    file.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return str(file)


def test_load_categories(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "description": "Описание смартфонов",
            "products": [
                {"name": "Телефон", "description": "Хороший телефон", "price": 1000.0, "quantity": 5},
                {"name": "Планшет", "description": "Хороший планшет", "price": 2000.0, "quantity": 3},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Описание телевизоров",
            "products": [
                {"name": "Телевизор", "description": "Большой экран", "price": 5000.0, "quantity": 2},
            ],
        },
    ]

    categories = load_categories_from_json(make_json_file(tmp_path, data))

    assert len(categories) == 2
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Смартфоны"
    assert categories[0].description == "Описание смартфонов"
    assert len(categories[0].products) == 2
    assert categories[1].name == "Телевизоры"
    assert len(categories[1].products) == 1


def test_load_products(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "description": "Описание",
            "products": [
                {"name": "Телефон", "description": "Хороший телефон", "price": 1000.0, "quantity": 5},
            ],
        }
    ]

    categories = load_categories_from_json(make_json_file(tmp_path, data))
    product = categories[0].products[0]

    assert isinstance(product, Product)
    assert product.name == "Телефон"
    assert product.description == "Хороший телефон"
    assert product.price == 1000.0
    assert product.quantity == 5


def test_load_empty_file(tmp_path):
    categories = load_categories_from_json(make_json_file(tmp_path, []))
    assert categories == []