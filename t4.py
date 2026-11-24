#завдання 4. абстрактні класи та композиція

from abc import ABC, abstractmethod

#компонент для композиції (окремий товар)
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

#абстрактний базовий клас (контракт інтерфейсу)
class Discount(ABC):
    @property
    @abstractmethod
    def discount_name(self):
        pass

    @abstractmethod
    def calculate_discount(self, total_amount):
        pass

    @abstractmethod
    def is_applicable(self, items_count):
        pass

    #конкретний метод у базовому класі
    def show_discount_info(self):
        return f"застосовано знижку: {self.discount_name}"

#конкретний підклас 1 (відношення is-a)
class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    @property
    def discount_name(self):
        return f"відсоткова ({self.percent}%)"

    def calculate_discount(self, total_amount):
        return total_amount * (self.percent / 100)

    def is_applicable(self, items_count):
        # діє, якщо 3 або більше товарів
        return items_count >= 3

#конкретний підклас 2 (відношення is-a)
class FixedDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    @property
    def discount_name(self):
        return f"фіксована ({self.amount} грн)"

    def calculate_discount(self, total_amount):
        return self.amount if total_amount >= self.amount else total_amount

    def is_applicable(self, items_count):
        return items_count >= 1

#клас, що використовує композицію (відношення has-a)
class Order:
    def __init__(self, discount=None):
        # замовлення "має" список товарів та об'єкт знижки
        self.items = []
        self.discount = discount

    def add_item(self, item):
        self.items.append(item)

    #делегування відповідальності компоненту discount
    def get_total_price(self):
        total = sum(item.price for item in self.items)
        if self.discount and self.discount.is_applicable(len(self.items)):
            discount_amount = self.discount.calculate_discount(total)
            total -= discount_amount
            print(self.discount.show_discount_info())
        return total

def main():
    print("перевірка абстрактного класу:")
    try:
        #спроба створити екземпляр абстрактного класу (викличе помилку)
        d = Discount()
    except TypeError as e:
        print(f"перехоплено помилку: {e}")

    print("\nробота композиції та делегування:")
    item1 = Item("мишка", 500)
    item2 = Item("клавіатура", 1500)
    item3 = Item("килимок", 300)

    #замовлення 1: фіксована знижка
    order1 = Order(FixedDiscount(200))
    order1.add_item(item1)
    order1.add_item(item2)
    print("замовлення 1 (2 товари, сума 2000):")
    print(f"до сплати: {order1.get_total_price()} грн\n")

    #замовлення 2: відсоткова знижка (діє лише від 3 товарів)
    order2 = Order(PercentageDiscount(10))
    order2.add_item(item1)
    order2.add_item(item2)
    order2.add_item(item3)
    print("замовлення 2 (3 товари, сума 2300):")
    print(f"до сплати: {order2.get_total_price()} грн")

if __name__ == "__main__":
    main()