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
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        """
        Возвращает цену продукта.
        """
        return self.__price

    @price.setter
    def price(self, new_price):
        """
        Устанавливает новую цену продукта с проверкой.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirm = input(
                f"Вы уверены, что хотите снизить цену с {self.__price} до {new_price}? (y/n): "
            )
            if confirm.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data, products_list=None):
        """
        Создаёт продукт на основе данных в словаре.
        Если продукт с таким именем существует, обновляет количество и выбирает максимальную цену.
        """
        if products_list:
            for product in products_list:
                if product.name == product_data["name"]:
                    product.quantity += product_data["quantity"]
                    product.price = max(product.price, product_data["price"])
                    return product

        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    def test_price_reduction_confirmation(monkeypatch):
        """
        Тест подтверждения снижения цены.
        """
        product = Product("Test Product", "Description", 100.0, 10)

        # Имитация ввода "y"
        monkeypatch.setattr("builtins.input", lambda _: "y")
        product.price = 50.0
        assert product.price == 50.0

        # Имитация ввода "n"
        monkeypatch.setattr("builtins.input", lambda _: "n")
        product.price = 30.0
        assert product.price == 50.0  # Цена не изменилась

    def __add__(self, other):
        """
        Переопределение оператора сложения.
        Возвращает полную стоимость двух продуктов на складе.
        """
        if not isinstance(other, Product):
            raise TypeError("Сложение возможно только между объектами Product.")
        return self.price * self.quantity + other.price * other.quantity


# product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
# print(product)  # Output: Product(name=Samsung Galaxy S23 Ultra, price=180000.0, quantity=5)
