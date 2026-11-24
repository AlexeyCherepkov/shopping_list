import pytest
from main import Category, Product


@pytest.fixture()
def apple():
    """Сущность яблоко, созданная от класса Product"""
    apple = Product('Яблоко', 'Сочное, красное', 50, 5)
    return apple


@pytest.fixture()
def fruits():
    """Сущность "фрукты", созданная от класса Category"""
    fruits = Category('Фрукты', 'Привезены из СНГ', ['яблоки', 'бананы'])
    return fruits


@pytest.fixture()
def vegetables():
    """Сущность "овощи", созданная от класса Category"""
    vegetables = Category('Овощи', 'Привезены из СНГ', ['огурцы', 'баклажаны'])
    return vegetables


def test_product_init(apple):
    """Тест контруктора Product"""
    assert apple.name == 'Яблоко'
    assert apple.description == 'Сочное, красное'
    assert apple.price == 50
    assert apple.quantity == 5


def test_category_init(fruits):
    """Тест конструктора Category"""
    assert fruits.name == 'Фрукты'
    assert fruits.description == 'Привезены из СНГ'
    assert fruits.products == ['яблоки', 'бананы']


def test_category_counting(vegetables):
    """
    Тест подсчета количества продуктор и категорий
    Первый вызов класса был при тестировании fruits, второй при передаче в тест аргумента vegetables
    """
    assert Category.amount_of_products == 4
    assert Category.amount_of_categories == 2