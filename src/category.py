import json
import os
from src.product import Product


class Category:
    """
    Класс для описания категории продуктов.
    """

    # Глобальные счётчики
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
        Category.category_count += 1

    @staticmethod
    def load_from_json(file_path):
        """
        Читает JSON-файл и преобразует данные в объекты Category и Product.

        :param file_path: Путь к JSON-файлу
        :return: Список объектов Category
        """
        # Сбрасываем глобальные счётчики перед загрузкой
        Category.category_count = 0
        Category.product_count = 0

        # Проверяем, существует ли файл
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден.")

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        categories = []
        for category_data in data["categories"]:
            # Создаём продукты для категории
            products = [
                Product(
                    product["name"],
                    product.get("description", "Описание отсутствует"),
                    product["price"],
                    product["quantity"],
                )
                for product in category_data["products"]
            ]

            # Увеличиваем глобальный счётчик продуктов
            Category.product_count += len(products)

            # Создаём объект категории
            category = Category(
                category_data["name"],
                category_data.get("description", "Описание категории отсутствует"),
                products,
            )
            categories.append(category)

        return categories

    def __str__(self):
        """
        Строковое представление категории.
        """
        product_list = ", ".join([product.name for product in self.products])
        return f"Category(name={self.name}, products=[{product_list}])"


# if __name__ == "__main__":
#     # Определяем путь к JSON-файлу
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_dir, "../products.json")
#
#     try:
#         # Загружаем категории из файла
#         categories = Category.load_from_json(file_path)
#         print("Категории успешно загружены!")
#
#         # Вывод категорий и продуктов
#         for idx, category in enumerate(categories, start=1):
#             print(f"\nКатегория {idx}: {category.name}")
#             print(f"Описание: {category.description}")
#             print("Продукты:")
#             for product in category.products:
#                 print(f"- {product.name} ({product.price} руб., {product.quantity} шт.)")
#
#         # Вывод глобальных счётчиков
#         print(f"\nОбщее количество категорий: {Category.category_count}")
#         print(f"Общее количество продуктов: {Category.product_count}")
#
#     except FileNotFoundError as e:
#         print(e)
#     except json.JSONDecodeError as e:
#         print(f"Ошибка чтения JSON-файла: {e}")
#     except Exception as e:
#         print(f"Неожиданная ошибка: {e}")
#