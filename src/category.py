from src.product import Product


class Category:
    name = str # Название категории
    description = str # Описание категории
    products = str # Продукты категории
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1 if description else 0
        Category.product_count += len(products) if products else 0

if __name__ == "__main__":
    product1 = Product("Смартфоны", "Устройства для связи", 171900.00,13)
    product2 = Product("Компьютеры и ноутбуки", "Для работы и игр", 120900.00,7)
    product3 = Product("Гаджеты", "Умные устройства", 169500.00,25)
    product4 = Product("Телевизоры", "Устройства для отображения видео в высоком качестве")
    product5 = Product("Инновационная техника", "Для 3D-печати", 83900.00,9)

    category = Category("Смартфоны", "Apple", [product1, product2, product3, product4])

    print(category.name)
    print(category.description)
    print(category.products)

    print(Category.category_count)
    print(Category.product_count)


