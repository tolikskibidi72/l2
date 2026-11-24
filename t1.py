#завдання 1. класова ієрархія та поліморфізм

class Transport:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def move(self):
        return "транспорт переміщується"

    def __str__(self):
        return f"транспорт {self.brand}, макс. швидкість {self.max_speed} км/год"


class Car(Transport):
    def __init__(self, brand, max_speed, doors):
        super().__init__(brand, max_speed)
        self.doors = doors

    def move(self):
        return "автомобіль їде по дорозі"

    def __str__(self):
        return f"авто {self.brand} ({self.doors} двері), швидкість {self.max_speed}"


class Boat(Transport):
    def __init__(self, brand, max_speed, boat_type):
        super().__init__(brand, max_speed)
        self.boat_type = boat_type

    def move(self):
        return "човен пливе по воді"

    def __str__(self):
        return f"човен {self.brand} (тип {self.boat_type}), швидкість {self.max_speed}"


class Plane(Transport):
    def __init__(self, brand, max_speed, wingspan):
        super().__init__(brand, max_speed)
        self.wingspan = wingspan

    def move(self):
        return "літак летить у небі"

    def __str__(self):
        return f"літак {self.brand} (розмах крил {self.wingspan}м), швидкість {self.max_speed}"


def main():
    #колекція об'єктів різних класів
    fleet = [
        Car("toyota", 180, 4),
        Boat("yamaha", 80, "моторний"),
        Plane("boeing", 900, 35)
    ]

    print("поліморфний обхід:")
    for vehicle in fleet:
        #викликаємо однаковий метод для різних об'єктів
        print(f"{vehicle}")
        print(f"дія: {vehicle.move()}")

        #демонстрація isinstance
        if isinstance(vehicle, Car):
            print("  (перевірка: це об'єкт класу авто)")

    print("\nперевірка спадковості (issubclass):")
    print(f"чи є Car підкласом Transport: {issubclass(Car, Transport)}")
    print(f"чи є Plane підкласом Boat: {issubclass(Plane, Boat)}")


if __name__ == "__main__":
    main()