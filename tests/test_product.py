import pytest
from src.product import Product


def test_product_initialization():
    """
    Тест корректной инициализации продукта.
    """
    product = Product("Apple iPhone 16 Pro Max", "Флагман с передовой камерой", 150000.00, 15)

    assert product.name == "Apple iPhone 16 Pro Max"
    assert product.description == "Флагман с передовой камерой"
    assert product.price == 150000.00
    assert product.quantity == 15


def test_product_str_representation():
    """
    Тест строкового представления продукта.
    """
    product = Product("Apple iPhone 16 Pro Max", "Флагман с передовой камерой", 150000.00, 15)
    assert str(product) == "Product(name=Apple iPhone 16 Pro Max, price=150000.0, quantity=15)"


def test_decrease_quantity():
    """
    Тест уменьшения количества продукта.
    """
    product = Product("Apple iPhone 16 Pro Max", "Флагман с передовой камерой", 150000.00, 15)

    product.decrease_quantity(5)
    assert product.quantity == 10

    # Попытка уменьшить количество ниже нуля
    with pytest.raises(ValueError, match="Нельзя уменьшить количество ниже 0."):
        product.decrease_quantity(20)


def test_increase_quantity():
    """
    Тест увеличения количества продукта.
    """
    product = Product("Apple iPhone 16 Pro Max", "Флагман с передовой камерой", 150000.00, 15)

    product.increase_quantity(5)
    assert product.quantity == 20

    # Попытка увеличить количество на отрицательное значение
    with pytest.raises(ValueError, match="Количество для увеличения должно быть положительным."):
        product.increase_quantity(-5)
