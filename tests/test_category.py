import pytest
from src.category import Category


def test_load_from_json(temp_json_file):
    """
    Тест загрузки данных из JSON.

    :param temp_json_file: Фикстура с временным JSON-файлом
    """
    categories = Category.load_from_json(temp_json_file)

    # Проверяем общее количество категорий
    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert categories[0].description == "Устройства для связи"
    assert len(categories[0].products) == 2

    # Проверяем продукты в первой категории
    assert categories[0].products[0].name == "Apple iPhone 16 Pro Max"
    assert categories[0].products[1].name == "Samsung Galaxy S23 Ultra"

    # Проверяем вторую категорию
    assert categories[1].name == "Гаджеты"
    assert len(categories[1].products) == 1
    assert categories[1].products[0].name == "Apple Watch Ultra 2"


def test_category_count(temp_json_file):
    """
    Тест подсчёта количества категорий.

    :param temp_json_file: Фикстура с временным JSON-файлом
    """
    # Сбрасываем счётчики
    Category.category_count = 0
    Category.product_count = 0

    # Загружаем данные из JSON
    categories = Category.load_from_json(temp_json_file)

    # Проверяем количество категорий
    assert len(categories) == 2
    assert Category.category_count == 2


def test_product_count(temp_json_file):
    """
    Тест подсчёта количества продуктов.

    :param temp_json_file: Фикстура с временным JSON-файлом
    """
    # Сбрасываем счётчики
    Category.category_count = 0
    Category.product_count = 0

    # Загружаем данные из JSON
    Category.load_from_json(temp_json_file)

    # Проверяем общее количество продуктов
    assert Category.product_count == 3


def test_category_initialization(sample_category):
    """
    Тест инициализации категории.

    :param sample_category: Фикстура с тестовой категорией
    """
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Устройства для связи"
    assert len(sample_category.products) == 3
    assert sample_category.products[0].name == "Apple iPhone 16 Pro Max"
