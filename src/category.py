import json
from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """
        Инициализация категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список объектов Product
        """
        self.name = name
        self.description = description
        self.products = products if isinstance(products, list) else []

        # Увеличиваем глобальный счётчик категорий
        Category.category_count += 1

        # Увеличиваем глобальный счётчик продуктов
        Category.product_count += len(self.products)

    @staticmethod
    def load_from_json(file_path):
        """
        Читает JSON-файл и преобразует данные в объекты Category и Product.

        :param file_path: Путь к JSON-файлу
        :return: Список объектов Category
        """
        # Сбрасываем счётчики перед загрузкой
        Category.category_count = 0
        Category.product_count = 0

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        categories = []
        for category_data in data["categories"]:
            # Преобразуем продукты
            products = [
                Product(
                    product["name"],
                    product.get("description", "Описание отсутствует"),
                    product["price"],
                    product["quantity"],
                )
                for product in category_data["products"]
            ]

            # Создаём объект категории
            category = Category(
                category_data["name"],
                category_data.get("description", "Описание категории отсутствует"),
                products,
            )
            categories.append(category)

        return categories
