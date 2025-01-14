from src.category import Category
from src.product import Product


def test_main_manual_category_and_products():
    """
    Тест ручного создания объектов Category и Product.
    """
    # Создаём продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаём категорию
    category = Category(
        "Смартфоны",
        "Современные устройства для связи и развлечений",
        [product1, product2, product3],
    )

    # Проверяем категорию
    assert category.name == "Смартфоны"
    assert category.description == "Современные устройства для связи и развлечений"
    assert len(category.products) == 3

    # Проверяем продукты
    assert category.products[0].name == "Samsung Galaxy S23 Ultra"
    assert category.products[1].name == "Iphone 15"
    assert category.products[2].name == "Xiaomi Redmi Note 11"


def test_main_json_loading(temp_json_file):
    """
    Тест загрузки категорий и продуктов из JSON.
    """
    # Загружаем категории из файла
    categories = Category.load_from_json(temp_json_file)

    # Проверяем, что категории загрузились корректно
    assert len(categories) == 1  # Ожидаем одну категорию
    category = categories[0]
    assert category.name == "Смартфоны"
    assert category.description == "Устройства для связи"
    assert len(category.products) == 3

    # Проверяем продукты в категории
    product_names = [product.name for product in category.products]
    assert "Samsung Galaxy S23 Ultra" in product_names
    assert "Iphone 15" in product_names
    assert "Xiaomi Redmi Note 11" in product_names


def test_main_global_counters(temp_json_file):
    """
    Тест проверки глобальных счётчиков категорий и продуктов.
    """
    # Сбрасываем глобальные счётчики
    Category.category_count = 0
    Category.product_count = 0

    # Загружаем категории из JSON
    Category.load_from_json(temp_json_file)

    # Проверяем значения глобальных счётчиков
    assert Category.category_count == 1  # Одна категория
    assert Category.product_count == 3  # Три продукта


def test_main_product_string_representation():
    """
    Тест строкового представления продуктов.
    """
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    expected_str = "Product(name=Samsung Galaxy S23 Ultra, price=180000.0, quantity=5)"
    assert str(product) == expected_str
