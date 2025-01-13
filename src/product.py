class Product:
    def __init__(self, name, description, price, quantity):
        """
        Инициализация продукта.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество на складе
        """
        self.name = name  # Название продукта
        self.description = description  # Описание продукта
        self.price = price  # Цена продукта
        self.quantity = quantity  # Количество продукта на складе

    def __str__(self):
        """Возвращает строковое представление продукта."""
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    def decrease_quantity(self, amount):
        """
        Уменьшает количество продукта на складе.

        :param amount: Количество для уменьшения
        """
        if amount > self.quantity:
            raise ValueError("Нельзя уменьшить количество ниже 0.")
        self.quantity -= amount

    def increase_quantity(self, amount):
        """
        Увеличивает количество продукта на складе.

        :param amount: Количество для увеличения
        """
        if amount < 0:
            raise ValueError("Количество для увеличения должно быть положительным.")
        self.quantity += amount
