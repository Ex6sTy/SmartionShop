from src.product import Product
from src.category import Category


def create_products():
    """Создаёт тестовые продукты."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return [product1, product2, product3]


def create_categories(products):
    """Создаёт тестовые категории."""
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products,
    )

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    return [category1, category2]


def main():
    """Основная функция программы."""
    products = create_products()

    # Вывод продуктов
    for product in products:
        print(product.name, product.description, product.price, product.quantity)

    categories = create_categories(products)

    # Вывод категорий
    for category in categories:
        print(category.name, category.description, len(category.products))

    # Глобальные счётчики
    print(Category.category_count)
    print(Category.product_count)


if __name__ == "__main__":
    main()
