from product import Product

class Category:
    name = str  # Название категории
    description = str  # Описание категории
    products = []  # Продукты категории
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
            self.name = name  # Название категории
            self.description = description  # Описание категории
            self.products = products if isinstance(products, list) else []  # Список продуктов
            Category.category_count += 1 if description else 0
            Category.product_count += sum(product.quantity for product in self.products)

    def __str__(self):
            product_list = ", ".join([product.name for product in self.products])
            return f"Category: {self.name}, Description: {self.description}, Products: [{product_list}]"

if __name__ == "__main__":
    # Создаём продукты
    product1 = Product("Apple iPhone 16 Pro Max", "Флагман с передовой камерой", 150000.00, 15)
    product2 = Product("Dell XPS 15", "Мощный ноутбук для работы и игр", 120000.00, 7)
    product3 = Product("Apple Watch Ultra 2", "Умные часы для экстремальных тренировок", 95000.00, 25)
    product4 = Product("Samsung Neo QLED 8K", "Высокое качество изображения", 450000.00, 5)
    product5 = Product("BambuLab P1S", "Скорость печати и автоматизация", 100000.00, 9)

    # Создаём категорию
    category = Category("Смартфоны", "Устройства для связи", [product1, product2, product3])

    print(category)
    print(f"Total Categories: {Category.category_count}")
    print(f"Total Products: {Category.product_count}")
