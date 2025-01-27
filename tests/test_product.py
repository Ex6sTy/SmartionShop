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
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", -31000.0, 14)



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

def test_product_price_getter(product_data):
    product = Product(**product_data)
    assert product.price == product_data["price"]


def test_product_price_setter_positive():
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = 200.0
    assert product.price == 200.0


def test_product_price_setter_negative():
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = -50.0
    assert product.price == 100.0  # Цена не изменилась


def test_product_new_product_without_duplicates(product_data):
    product = Product.new_product(product_data)
    assert product.name == product_data["name"]
    assert product.price == product_data["price"]
    assert product.quantity == product_data["quantity"]


def test_product_new_product_with_duplicates(product_data):
    existing_products = [
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 30000.0, 10)
    ]
    new_product = Product.new_product(product_data, existing_products)
    assert new_product.quantity == 24
    assert new_product.price == 31000.0  # Выбрана максимальная цена

def test_product_count(temp_json_file):
    """Тест подсчёта количества продуктов."""
    # Сбрасываем счётчики
    Category.category_count = 0
    Category.product_count = 0

    # Загружаем данные из JSON
    Category.load_from_json(temp_json_file)

    # Проверяем общее количество продуктов
    assert Category.product_count == 3

def test_product_str_representation():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    expected_str = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product) == expected_str

def test_product_addition():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # 180000 * 5 + 210000 * 8 = 3,780,000
    expected_sum = 180000 * 5 + 210000 * 8
    assert product1 + product2 == expected_sum
