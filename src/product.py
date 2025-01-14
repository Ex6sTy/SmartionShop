class Product:
    """
    Класс для описания продукта.
    """

    def __init__(self, name, description, price, quantity):
        """
        Инициализация продукта.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество продукта
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

    def __str__(self):
        """
        Строковое представление продукта.
        """
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"


# product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
# print(product)  # Output: Product(name=Samsung Galaxy S23 Ultra, price=180000.0, quantity=5)
