from src.product import Product


def test_product_initialization():
    """Тест корректной инициализации продукта."""
    product = Product("Test Product", "Test Description", 100.0, 10)

    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_quantity_update():
    """Тест обновления количества продукта."""
    product = Product("Test Product", "Test Description", 100.0, 10)

    # Уменьшаем количество
    product.quantity -= 2
    assert product.quantity == 8

    # Увеличиваем количество
    product.quantity += 5
    assert product.quantity == 13
