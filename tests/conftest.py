import pytest
import json
from src.product import Product
from src.category import Category


@pytest.fixture
def temp_json_file(tmp_path):
    """Создаёт временный JSON-файл с тестовыми данными."""
    data = {
        "categories": [
            {
                "name": "Смартфоны",
                "description": "Устройства для связи",
                "products": [
                    {
                        "name": "Samsung Galaxy S23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    },
                    {
                        "name": "Iphone 15",
                        "description": "512GB, Gray space",
                        "price": 210000.0,
                        "quantity": 8,
                    },
                    {
                        "name": "Xiaomi Redmi Note 11",
                        "description": "1024GB, Синий",
                        "price": 31000.0,
                        "quantity": 14,
                    },
                ],
            },
        ]
    }

    file_path = tmp_path / "products.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)

    return file_path




@pytest.fixture
def sample_products():
    """
    Возвращает список тестовых объектов Product.

    :return: Список продуктов
    """
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def sample_category(sample_products):
    """
    Возвращает тестовый объект Category с продуктами.

    :param sample_products: Фикстура со списком продуктов
    :return: Объект Category
    """
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        sample_products,
    )


@pytest.fixture(autouse=True)
def reset_category_counters():
    """
    Сбрасывает глобальные счётчики перед каждым тестом.
    """
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product_data():
    return {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}

def test_smartphone_addition():
    smartphone1 = Smartphone("iPhone 15", "Флагманский смартфон", 200000.0, 5, 95, "Pro Max", 256, "Silver")
    smartphone2 = Smartphone("Samsung Galaxy S23", "Флагманский смартфон", 180000.0, 8, 90, "Ultra", 512, "Black")
    assert smartphone1 + smartphone2 == 200000.0 * 5 + 180000.0 * 8


def test_addition_different_classes():
    smartphone = Smartphone("iPhone 15", "Флагманский смартфон", 200000.0, 5, 95, "Pro Max", 256, "Silver")
    lawn_grass = LawnGrass("Газонная трава", "Идеальная для садов", 1000.0, 20, "Россия", 7, "Зелёный")
    try:
        smartphone + lawn_grass
    except TypeError as e:
        assert str(e) == "Сложение возможно только между объектами одного и того же типа."
