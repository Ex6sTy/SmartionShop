import pytest
from src.category import Category
from src.product import Product


def test_load_from_json(temp_json_file):
    """
    Тест загрузки данных из JSON-файла.
    """
    categories = Category.load_from_json(temp_json_file)

    # Проверяем, что категории загрузились корректно
    assert len(categories) == 1  # Ожидаем одну категорию
    assert categories[0].name == "Смартфоны"
    assert categories[0].description == "Устройства для связи"

    # Проверяем количество продуктов в категории
    assert len(categories[0].products) == 3  # Ожидаем три продукта
    assert categories[0].products[0].name == "Samsung Galaxy S23 Ultra"
    assert categories[0].products[0].price == 180000.0
    assert categories[0].products[0].quantity == 5


def test_category_initialization(sample_category):
    """
    Тест инициализации категории.
    """
    assert sample_category.name == "Смартфоны"
    assert sample_category.description.startswith("Смартфоны, как средство")
    assert len(sample_category.products) == 3


def test_global_counters(temp_json_file):
    """
    Тест работы глобальных счётчиков категорий и продуктов.
    """
    # Сбрасываем глобальные счётчики
    Category.category_count = 0
    Category.product_count = 0

    # Загружаем данные из JSON
    Category.load_from_json(temp_json_file)

    # Проверяем значения глобальных счётчиков
    assert Category.category_count == 1  # Одна категория
    assert Category.product_count == 3  # Три продукта


def test_str_method(sample_category):
    """
    Тест строкового представления категории.
    """
    expected = "Category(name=Смартфоны, products=[Samsung Galaxy S23 Ultra, Iphone 15, Xiaomi Redmi Note 11])"
    assert str(sample_category) == expected


def test_category_without_products():
    """
    Тест создания категории без продуктов.
    """
    empty_category = Category("Пустая категория", "Нет продуктов", [])
    assert empty_category.name == "Пустая категория"
    assert empty_category.description == "Нет продуктов"
    assert len(empty_category.products) == 0


def test_category_add_product(sample_category, product_data):
    new_product = Product(**product_data)
    sample_category.add_product(new_product)
    assert "Xiaomi Redmi Note 11" in sample_category.products

def test_category_str_representation(sample_category):
    expected_str = "Смартфоны, количество продуктов: 27 шт."  # 5 + 8 + 14 = 27
    assert str(sample_category) == expected_str

def test_category_iteration(sample_category):
    products = [p.name for p in sample_category]
    assert products == ["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]
