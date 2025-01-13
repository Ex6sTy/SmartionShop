class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name # Бренд
        self.description = description # Описание товара
        self.price = price #  Цена
        self.quantity = quantity # Количество


if __name__ == "__main__":
    product = Product("Apple iPhone 16 Pro Max", "Флагман с передовой камерой", 150000.00, 15)


    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)