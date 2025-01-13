import pytest
import json


@pytest.fixture
def temp_json_file(tmp_path):
    """Создаёт временный JSON-файл с тестовыми данными."""
    data = {
        "categories": [
            {
                "name": "Смартфоны",
                "products": [
                    {
                        "name": "Apple iPhone 16 Pro Max",
                        "description": "Флагман с передовой камерой",
                        "price": 150000.00,
                        "quantity": 15,
                    },
                    {
                        "name": "Samsung Galaxy S23 Ultra",
                        "description": "Высокая производительность и мощная камера",
                        "price": 110000.00,
                        "quantity": 20,
                    },
                ],
            },
            {
                "name": "Гаджеты",
                "products": [
                    {
                        "name": "Apple Watch Ultra 2",
                        "description": "Для экстремальных тренировок",
                        "price": 95000.00,
                        "quantity": 18,
                    }
                ],
            },
        ]
    }
    file = tmp_path / "products.json"
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file
