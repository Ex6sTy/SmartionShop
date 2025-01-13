from src.category import Category


def test_load_from_json(temp_json_file):
    """Тест загрузки данных из JSON."""
    categories = Category.load_from_json(temp_json_file)

    # Проверяем количество категорий
    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert categories[1].name == "Гаджеты"

    # Проверяем количество продуктов в первой категории
    assert len(categories[0].products) == 2
    assert categories[0].products[0].name == "Apple iPhone 16 Pro Max"
    assert categories[0].products[1].name == "Samsung Galaxy S23 Ultra"

    # Проверяем количество продуктов во второй категории
    assert len(categories[1].products) == 1
    assert categories[1].products[0].name == "Apple Watch Ultra 2"


def test_category_count(temp_json_file):
    """Тест подсчёта количества категорий."""
    # Сбрасываем счётчики
    Category.category_count = 0
    Category.product_count = 0

    # Загружаем данные из JSON
    Category.load_from_json(temp_json_file)

    # Проверяем количество категорий
    assert Category.category_count == 2


def test_product_count(temp_json_file):
    """Тест подсчёта количества продуктов."""
    # Сбрасываем счётчики
    Category.category_count = 0
    Category.product_count = 0

    # Загружаем данные из JSON
    Category.load_from_json(temp_json_file)

    # Проверяем общее количество продуктов
    assert Category.product_count == 3
