from src.main import create_products, create_categories
from src.category import Category


def test_create_products():
    """Тест создания продуктов."""
    products = create_products()
    assert len(products) == 3

    assert products[0].name == "Samsung Galaxy S23 Ultra"
    assert products[1].name == "Iphone 15"
    assert products[2].name == "Xiaomi Redmi Note 11"


def test_create_categories():
    """Тест создания категорий."""
    products = create_products()
    categories = create_categories(products)

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert categories[1].name == "Телевизоры"

    assert len(categories[0].products) == 3
    assert len(categories[1].products) == 1


def test_global_counters():
    """Тест работы глобальных счётчиков."""
    # Сбрасываем счётчики
    Category.category_count = 0
    Category.product_count = 0

    products = create_products()
    create_categories(products)

    assert Category.category_count == 2
    assert Category.product_count == 4
