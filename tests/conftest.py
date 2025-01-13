import pytest
import json
from src.category import Category
from src.product import Product


@pytest.fixture
def temp_json_file(tmp_path):
    """
    Создаёт временный JSON-файл с тестовыми данными.

    :param tmp_path: Временная директория для создания файла
    :return: Путь к созданному JSON-файлу
    """
    data = {
        "categories": [
            {
                "name": "Смартфоны",
                "description": "Устройства для связи",
                "products": [
                    {
                        "name": "Apple iPhone 16 Pro Max",
                        "description": "Флагман с передовой камерой",
                        "price": 150000.00,
                        "quantity": 15
                    },
                    {
                        "name": "Samsung Galaxy S23 Ultra",
                        "description": "Высокая производительность и мощная камера",
                        "price": 110000.00,
                        "quantity": 20
                    }
                ]
            },
            {
                "name": "Гаджеты",
                "description": "Умные устройства для повседневной жизни",
                "products": [
                    {
                        "name": "Apple Watch Ultra 2",
                        "description": "Для экстремальных тренировок",
                        "price": 95000.00,
                        "quantity": 18
                    }
                ]
            }
        ]
    }

    # Создание временного JSON-файла
    file = tmp_path / "products.json"
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f)

    return file


@pytest.fixture
def sample_products():
    """
    Возвращает список тестовых объектов Product.

    :return: Список продуктов
    """
    return [
        Product("Apple iPhone 16 Pro Max", "Флагман с передовой камерой", 150000.00, 15),
        Product("Samsung Galaxy S23 Ultra", "Высокая производительность и мощная камера", 110000.00, 20),
        Product("Xiaomi 13 Pro", "Стильный дизайн и быстрая зарядка", 85000.00, 30),
    ]


@pytest.fixture
def sample_category(sample_products):
    """
    Возвращает тестовый объект Category с продуктами.

    :param sample_products: Фикстура со списком продуктов
    :return: Объект Category
    """
    return Category("Смартфоны", "Устройства для связи", sample_products)
