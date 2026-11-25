from src.models import Product, Category  # замените classes на имя вашего модуля


def test_product():
    product = Product("Телефон", "Хороший телефон", 1000.0, 5)
    assert product.name == "Телефон"
    assert product.description == "Хороший телефон"
    assert product.price == 1000.0
    assert product.quantity == 5


def test_category():
    product = Product("Телефон", "Хороший телефон", 1000.0, 5)
    category = Category("Смартфоны", "Описание", [product])
    assert category.name == "Смартфоны"
    assert category.description == "Описание"
    assert category.products == [product]


def test_counters():
    categories_before = Category.category_count
    products_before = Category.product_count

    product1 = Product("Телефон", "Описание", 1000.0, 5)
    product2 = Product("Планшет", "Описание", 2000.0, 3)
    Category("Электроника", "Описание", [product1, product2])

    assert Category.category_count == categories_before + 1
    assert Category.product_count == products_before + 2