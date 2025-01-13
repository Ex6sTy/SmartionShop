from src.product import Product


class Category:
    name = str
    description = str
    products = str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1 if description else 0
        Category.product_count += len(products) if products else 0

if __name__ == "__main__":
    product1 = Product("Apple iPhone 16 Pro Max 1Tb", "Смартфон Apple", 171900.00,13)
    product2 = Product("Apple iPhone 16 Pro 256Gb", "Смартфон Apple", 120900.00,7)
    product3 = Product("Apple iPhone 16 Pro 1Tb", "Смартфон Apple", 169500.00,25)
    product4 = Product("Apple iPhone 16 128Gb", "Смартфон Apple", 83900.00,9)

    category = Category("Смартфон", "Apple", [product1, product2, product3, product4])
    category = Category("Смартфон", "Apple", [product1, product2, product3, product4])

    print(category.name)
    print(category.description)
    print(category.products)

    print(Category.category_count)
    print(Category.product_count)


