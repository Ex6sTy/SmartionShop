import json
import os
from src.product import Product


class Category:
    name = str
    description = str
    products = []
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products if isinstance(products, list) else []
        Category.category_count += 1 if description else 0
        Category.product_count += sum(product.quantity for product in self.products)

    def __str__(self):
        product_list = ", ".join([product.name for product in self.products])
        return f"Category: {self.name}, Description: {self.description}, Products: [{product_list}]"

    @staticmethod
    def load_from_json(file_path):
        # Проверяем существование файла
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден!")

        # Загружаем JSON
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        categories = []
        for category_data in data["categories"]:
            products = [
                Product(
                    product["name"],
                    product["description"],
                    product["price"],
                    product["quantity"],
                )
                for product in category_data["products"]
            ]
            category = Category(category_data["name"], category_data["name"], products)
            categories.append(category)

        return categories


if __name__ == "__main__":
    # Используем путь относительно текущего файла
    file_path = os.path.join(os.path.dirname(__file__), "../products.json")
    categories = Category.load_from_json(file_path)

    for category in categories:
        print(category)

    print(f"Total Categories: {Category.category_count}")
    print(f"Total Products: {Category.product_count}")
