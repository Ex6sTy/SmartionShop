from src.product import Product


def test_product_initialization():
    """
    Тест инициализации объекта Product.
    """
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_string_representation():
    """
    Тест строкового представления объекта Product.
    """
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    expected_str = "Product(name=Iphone 15, price=210000.0, quantity=8)"
    assert str(product) == expected_str


def test_product_negative_price():
    """
    Тест для проверки некорректного значения цены.
    """
    try:
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", -31000.0, 14)
        assert False, "Ожидалось исключение при отрицательной цене"
    except ValueError:
        assert True


def test_product_zero_quantity():
    """
    Тест для проверки нулевого количества.
    """
    product = Product("Samsung Galaxy A14", "64GB, Черный цвет", 15000.0, 0)
    assert product.quantity == 0


def test_product_large_quantity():
    """
    Тест для проверки корректности большого количества.
    """
    product = Product("MacBook Pro 16", "1TB, Silver", 250000.0, 10000)
    assert product.quantity == 10000
